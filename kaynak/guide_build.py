"""Generate the dated guide from content.py; no third-party runtime dependencies."""
from pathlib import Path
import html
import json
import re
import hashlib
import struct
from datetime import date
from urllib.parse import urlsplit
from content import (GUIDE_DATE, GUIDE_UPDATED, GUIDE_INTRO, GUIDE_CHAPTERS, GUIDE_APPENDICES,
                     GUIDE_SOURCES, GUIDE_FEATURES, GUIDE_ITEM_MAP, GUIDE_FIGURES,
                     GUIDE_PATHS, GUIDE_FLOWS, GUIDE_EXAMPLES, GUIDE_ROUTE, GUIDE_ARTIFACTS, SECTIONS)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / 'rehber'
PAGE_SLUGS = {c['slug'] for c in GUIDE_CHAPTERS + GUIDE_APPENDICES} | {'kapsam', 'esleme', 'kaynaklar'}


def resolve_sources(text):
    return re.sub(r'\(source:([\w-]+)\)', lambda m: '(' + GUIDE_SOURCES[m[1]]['url'] + ')', text)


def figure_label(f):
    return {'official':'OpenAI’nin resmî arayüz gösterimi', 'example':'Kurgu örnek HTML’nin gerçek tarayıcı görüntüsü', 'artifact':'Kurgu veriden üretilmiş gerçek çıktı'}[f['kind']]

def teaching_next(slug):
    route=[p['slug'] for p in GUIDE_ROUTE]
    if slug not in route: return ''
    index=route.index(slug)
    if index==len(route)-1: return '\n\n**Eğitim rotası tamamlandı.** Konu ayrıntıları için [içindekilere dön](README.md).\n'
    item=GUIDE_ROUTE[index+1]
    return f'\n\n**Eğitimde sıradaki:** [{item["title"]}]({item["slug"]}.md)\n'

def figure_html(key):
    f = GUIDE_FIGURES[key]
    width, height = struct.unpack('>II', (OUT/f['file']).read_bytes()[16:24])
    esc = lambda s: html.escape(s, quote=True)
    label = figure_label(f)
    lesson='<ol class="figure-lesson">'+''.join('<li><strong>'+esc(a)+'</strong> '+esc(b)+'</li>' for a,b in f['lesson'])+'</ol>'
    return (f'<figure class="app-figure figure-{f["kind"]}"><a class="figure-open" href="{esc(f["file"])}" '
            f'aria-label="{esc(f["title"])} — görseli tam boyutta aç">'
            f'<img src="{esc(f["file"])}" alt="{esc(f["alt"])}" width="{width}" height="{height}" loading="lazy" decoding="async"></a>'
            f'<figcaption><strong>{esc(f["title"])}</strong> {esc(f["caption"])} '
            f'{lesson}<span class="figure-source">{label} · '
            f'<a href="{esc(f["source"])}">Kaynak</a> · {f["checked"]} · Görsele tıklayarak büyüt.</span></figcaption></figure>')


def flow_html(key):
    f=GUIDE_FLOWS[key]
    return ('<figure class="lesson-flow"><figcaption>'+html.escape(f['title'])+'</figcaption><ol>'+''.join(
        '<li><strong>'+html.escape(a)+'</strong><span>'+html.escape(b)+'</span></li>' for a,b in f['steps'])+'</ol></figure>')


def markdown_output(text):
    """Use the same figure metadata and explicit anchors in GitHub Markdown."""
    def figure(m):
        f=GUIDE_FIGURES[m[1]]
        label=figure_label(f)
        return (f'![{f["alt"]}]({f["file"]})\n\n**{f["title"]}.** {f["caption"]} '
                f'[Tam boyut]({f["file"]}) · {label} · '
                f'[Kaynak]({f["source"]}) · {f["checked"]}.\n\n'+
                '\n'.join(f'{n}. **{a}:** {b}' for n,(a,b) in enumerate(f['lesson'],1)))
    text=re.sub(r'^\[FIGURE:([a-z-]+)\]$',figure,text,flags=re.M)
    def flow(m):
        f=GUIDE_FLOWS[m[1]]
        return '**'+f['title']+'**\n\n'+'\n'.join(f'{n}. **{a}:** {b}' for n,(a,b) in enumerate(f['steps'],1))
    text=re.sub(r'^\[FLOW:([a-z-]+)\]$',flow,text,flags=re.M)
    # Match renderer IDs so cross-links work both in GitHub and the HTML site.
    seen={}; fence=False; lines=[]
    for line in text.splitlines():
        if line.startswith('```'):fence=not fence
        if not fence and re.match(r'^#{1,6} ',line):
            slug=slugify(line.lstrip('#').strip());seen[slug]=seen.get(slug,0)+1
            anchor=slug if seen[slug]==1 else slug+'-'+str(seen[slug])
            lines.extend([f'<a id="{anchor}"></a>',''])
        lines.append(line)
    return '\n'.join(lines)


def slugify(text):
    text = text.lower().translate(str.maketrans('çğıöşü', 'cgiosu'))
    return re.sub(r'[^a-z0-9]+', '-', text).strip('-')


def href_for_html(url):
    base, sep, fragment = url.partition('#')
    if base == '../codex-kontrol-listesi.md':
        base = '../index.html'
    elif base == 'README.md':
        base = 'index.html'
    elif base.endswith('.md') and base[:-3] in PAGE_SLUGS:
        base = base[:-3] + '.html'
    return base + (sep + fragment if sep else '')


def inline(text):
    tokens = []
    def stash(value):
        tokens.append(value)
        return f'\x00{len(tokens)-1}\x00'
    text = re.sub(r'`([^`]+)`', lambda m: stash('<code>' + html.escape(m[1]) + '</code>'), text)
    def link(m):
        url = href_for_html(m[2])
        if urlsplit(url).scheme not in ('', 'https', 'http'):
            raise ValueError('Unsafe link: ' + url)
        return stash('<a href="' + html.escape(url, quote=True) + '">' + html.escape(m[1]) + '</a>')
    text = re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)', link, text)
    text = html.escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Multiple passes allow a link label to contain an already protected code span.
    while '\x00' in text:
        text = re.sub(r'\x00(\d+)\x00', lambda m: tokens[int(m[1])], text)
    return text


def render_markdown(markdown):
    """Small fail-closed renderer for the authored subset, with escaped text/code."""
    lines = markdown.splitlines(); out = []; headings = []; seen = {}; n = 0
    def starts_block(line):
        return not line.strip() or line.startswith(('#', '|', '>', '```', '- ', '[FIGURE:', '[FLOW:')) or bool(re.match(r'^\d+\. ', line))
    while n < len(lines):
        line = lines[n]
        if not line.strip(): n += 1; continue
        if line.startswith('[FLOW:'):
            match=re.fullmatch(r'\[FLOW:([a-z-]+)\]',line)
            if not match or match[1] not in GUIDE_FLOWS: raise ValueError('Unknown flow: '+line)
            out.append(flow_html(match[1])); n += 1
        elif line.startswith('[FIGURE:'):
            match=re.fullmatch(r'\[FIGURE:([a-z-]+)\]',line)
            if not match or match[1] not in GUIDE_FIGURES: raise ValueError('Unknown figure: '+line)
            out.append(figure_html(match[1])); n += 1
        elif line.startswith('```'):
            code=[]; n += 1
            while n < len(lines) and not lines[n].startswith('```'):
                code.append(lines[n]); n += 1
            if n == len(lines): raise ValueError('Unclosed code fence')
            out.append('<pre><code>' + html.escape('\n'.join(code)) + '</code></pre>'); n += 1
        elif re.match(r'^#{1,6} ', line):
            level=len(line)-len(line.lstrip('#')); title=line[level+1:]
            slug=slugify(title); seen[slug]=seen.get(slug,0)+1
            anchor=slug if seen[slug]==1 else slug+'-'+str(seen[slug])
            out.append(f'<h{level} id="{anchor}">{inline(title)}</h{level}>')
            if level==2: headings.append((anchor,title))
            n += 1
        elif line.startswith('|'):
            rows=[]
            while n<len(lines) and lines[n].startswith('|'):
                rows.append([c.strip() for c in lines[n].strip().strip('|').split('|')]); n += 1
            if len(rows)<2 or not all(re.fullmatch(r':?-+:?',c) for c in rows[1]):
                raise ValueError('Invalid table header')
            count=len(rows[0]); assert all(len(r)==count for r in rows), 'Mismatched table columns'
            out.append('<p class="table-hint">Tablonun devamını görmek için yatay kaydır.</p><div class="table-scroll" role="region" tabindex="0" aria-label="Kaydırılabilir karşılaştırma tablosu"><table><thead><tr>'+''.join('<th scope="col">'+inline(c)+'</th>' for c in rows[0])+'</tr></thead><tbody>')
            out.extend('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in row)+'</tr>' for row in rows[2:]); out.append('</tbody></table></div>')
        elif line.startswith('>'):
            block=[]
            while n<len(lines) and lines[n].startswith('>'):
                block.append(lines[n].lstrip('>').strip()); n += 1
            out.append('<blockquote><p>'+inline(' '.join(block))+'</p></blockquote>')
        elif line.startswith('- ') or re.match(r'^\d+\. ',line):
            ordered=not line.startswith('- '); tag='ol' if ordered else 'ul'; rows=[]
            pattern=r'^\d+\. ' if ordered else r'^- '
            while n<len(lines) and re.match(pattern,lines[n]):
                rows.append('<li>'+inline(re.sub(pattern,'',lines[n]))+'</li>'); n += 1
            out.append(f'<{tag}>'+''.join(rows)+f'</{tag}>')
        else:
            paragraph=[line]; n += 1
            while n<len(lines) and not starts_block(lines[n]): paragraph.append(lines[n]); n += 1
            out.append('<p>'+inline(' '.join(paragraph))+'</p>')
    return '\n'.join(out), headings


def validate_guide():
    assert len(GUIDE_CHAPTERS)==18
    assert [c['number'] for c in GUIDE_CHAPTERS]==list(range(1,19))
    all_pages=GUIDE_CHAPTERS+GUIDE_APPENDICES
    assert len({p['slug'] for p in all_pages})==len(all_pages)
    assert len(GUIDE_PATHS)==3 and {p['slug'] for p in GUIDE_PATHS}<={p['slug'] for p in GUIDE_APPENDICES}
    for name,body in GUIDE_EXAMPLES.items():
        assert Path(name).name==name and Path(name).suffix in {'.md','.csv','.html'} and body
    used_flows=set(re.findall(r'\[FLOW:([^]]+)\]', '\n'.join(p['body'] for p in all_pages)))
    assert used_flows==set(GUIDE_FLOWS)
    for flow in GUIDE_FLOWS.values(): assert flow['title'] and len(flow['steps'])==4
    ids={i['id'] for s in SECTIONS for i in s['items']}
    assert set(GUIDE_ITEM_MAP)==ids and len(ids)==107
    assert set(GUIDE_ITEM_MAP.values()) <= PAGE_SLUGS
    assert len({f['id'] for f in GUIDE_FEATURES})==len(GUIDE_FEATURES)
    for f in GUIDE_FEATURES:
        assert f['target'] in PAGE_SLUGS and f['source'] in GUIDE_SOURCES
        assert f['condition'] and f['status']
    for p in all_pages:
        assert p['body'].strip()
        assert len(p['body'].split()) >= 250, p['slug']
        for key in re.findall(r'\(source:([\w-]+)\)',p['body']): assert key in GUIDE_SOURCES, key
    used=set(re.findall(r'\[FIGURE:([^]]+)\]', '\n'.join(p['body'] for p in all_pages)))
    assert used==set(GUIDE_FIGURES), 'Every figure must be used and declared'
    for f in GUIDE_FIGURES.values():
        asset=(OUT/f['file']).resolve()
        assert asset.is_relative_to((OUT/'assets').resolve()) and asset.suffix=='.png'
        assert asset.read_bytes()[:8]==b'\x89PNG\r\n\x1a\n'
        assert hashlib.sha256(asset.read_bytes()).hexdigest()==f['sha256']
        assert f['alt'] and f['caption'] and f['title'] and date.fromisoformat(f['checked']) <= date.fromisoformat(GUIDE_UPDATED)
        assert len(f['lesson'])==3 and all(a and b for a,b in f['lesson'])
        assert f['kind'] in {'official','example','artifact'}
        if f['kind']=='official':assert f['source'].startswith('https://learn.chatgpt.com/docs/')
        elif f['kind']=='example':assert f['source'].startswith('ornekler/') and f['source'][9:] in GUIDE_EXAMPLES
        else:assert f['source'] in GUIDE_ARTIFACTS or (f['source'].startswith('ornekler/') and f['source'][9:] in GUIDE_EXAMPLES)
    assert len({p['slug'] for p in GUIDE_ROUTE})==len(GUIDE_ROUTE)
    assert {p['slug'] for p in GUIDE_ROUTE} <= PAGE_SLUGS
    for name,meta in GUIDE_ARTIFACTS.items():
        asset=(OUT/name).resolve()
        assert asset.is_relative_to((OUT/'ornekler').resolve())
        assert hashlib.sha256(asset.read_bytes()).hexdigest()==meta['sha256']
    return ids


def page_html(title, markdown, current, prev=None, next_=None):
    rendered, heads=render_markdown(markdown)
    active_attr = 'aria-current="page"'
    journeys=[p for p in GUIDE_APPENDICES if 'journey' in p]
    references=[p for p in GUIDE_APPENDICES if 'journey' not in p]
    nav='<div class="nav-group">ÖRNEK İŞLER</div>'+''.join(f'<a {active_attr if c["slug"]==current else ""} href="{c["slug"]}.html">{c["journey"]}. {html.escape(c["title"])}</a>' for c in journeys)
    nav+='<div class="nav-group">KONU REHBERİ</div>'+''.join(f'<a {active_attr if c["slug"]==current else ""} href="{c["slug"]}.html">{c.get("number", "Ek")}. {html.escape(c["title"])}</a>' for c in GUIDE_CHAPTERS+references)
    nav += '<a href="kapsam.html">Özellik envanteri</a><a href="esleme.html">107 madde eşlemesi</a><a href="kaynaklar.html">Kaynaklar ve sınırlar</a>'
    local='<details class="page-toc"><summary>Bu sayfada</summary><ul>'+''.join(f'<li><a href="#{a}">{html.escape(t)}</a></li>' for a,t in heads)+'</ul></details>' if heads else ''
    moves=[]
    if prev: moves.append(f'<a rel="prev" href="{prev["slug"]}.html">← {html.escape(prev["title"])}</a>')
    if next_: moves.append(f'<a rel="next" href="{next_["slug"]}.html">{html.escape(next_["title"])} →</a>')
    css=(HERE/'style.css').read_text()+'\n'+(HERE/'guide.css').read_text()
    return f'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)} · Codex rehberi</title><meta name="description" content="Gerçek deneyimler, kaynaklı açıklamalar ve kurgu senaryolarla Türkçe Codex uygulaması rehberi."><style>{css}</style></head>
<body class="guide"><a class="skip" href="#icerik">İçeriğe geç</a><header class="topbar"><a class="brand" href="index.html"><span class="brandmark" aria-hidden="true">›_</span>Codex <span class="brandlight">/ derinlemesine rehber</span></a><a class="top-source" href="../index.html">107 madde ↗</a></header>
<div class="layout"><aside class="sidebar"><div class="eyebrow">İÇİNDEKİLER</div><nav aria-label="Rehber bölümleri">{nav}</nav></aside><main id="icerik"><nav class="breadcrumb" aria-label="Sayfa yolu"><a href="index.html">Rehber</a> / <a href="{current+'.md' if current!='index' else 'README.md'}">Markdown</a></nav><div class="eyebrow">İÇERİK GÜNCELLEMESİ · {GUIDE_UPDATED}</div><h1>{html.escape(title)}</h1>{local}<article class="prose">{rendered}</article><nav class="page-next" aria-label="Sıralı okuma">{''.join(moves)}</nav><footer><span>© 2026 Ratipcan Uysal · Metin: <a href="../LICENSE">CC BY 4.0</a><br>Arayüz görselleri: OpenAI; bu lisansa dahil değildir.<br>Bağımsız rehber; resmî OpenAI yayını değildir.</span><a href="kaynaklar.html">Kaynak ve erişim sınırları</a></footer></main></div></body></html>'''


def build_guide():
    validate_guide(); OUT.mkdir(exist_ok=True)
    (OUT/'ornekler').mkdir(exist_ok=True)
    for name,body in GUIDE_EXAMPLES.items():(OUT/'ornekler'/name).write_text(body)
    lookup={i['id']:i for s in SECTIONS for i in s['items']}
    titles={c['slug']:c['title'] for c in GUIDE_CHAPTERS+GUIDE_APPENDICES}
    pages=[]
    for index,c in enumerate(GUIDE_CHAPTERS+GUIDE_APPENDICES):
        related=[id for id,target in GUIDE_ITEM_MAP.items() if target==c['slug']]
        body=resolve_sources(c['body'])+teaching_next(c['slug'])
        if related:
            body+='\n\n## Kontrol listesinde karşılığı\n\n'
            body+='\n'.join(f'- [{id} {lookup[id]["title"]}](../codex-kontrol-listesi.md#{lookup[id]["anchor"]})' for id in related)
        pages.append({**c,'body':body})
    feature_md='''Envanter birimi, kullanıcıya dönük yetenek veya ilişkili özellik ailesidir. Resmî belgelerde tespit edilen masaüstü yetenekleri ve kullanım kararını etkileyen komşu yüzeyler kapsanır. Her satırın açıklaması/erişim sınırı ilgili bölümde bulunur. Hesaba özel görünmeyen dağıtımlar ve üçüncü taraf plugin'lerin bütün iç komutları için evrensel eksiksizlik iddiası yoktur.

**Kanıt türü:** Aşağıdaki ürün bilgileri 29 Ekim 2026'da açılan resmî belgelere dayanır. Bu rehber için özellikler tek tek canlı çalıştırılmadı. Rehber sitesinin testleri, Codex özelliklerinin tamamının çalıştırıldığı anlamına gelmez. Masaüstünün 28 sabit slash komutu ayrıca [komut ekinde](komutlar.md) tek tek açıklanır.

| Kimlik | Özellik / kullanım | Koşul ve sınır | Açıklama | Resmî kaynak |
|---|---|---|---|---|
'''
    for f in GUIDE_FEATURES:
        src=GUIDE_SOURCES[f['source']]
        feature_md+=f'| {f["id"]} | {f["name"]} | {f["condition"]} | [{titles[f["target"]]}]({f["target"]}.md) | [{src["title"]}]({src["url"]}) |\n'
    pages.append(dict(slug='kapsam',title=f'{len(GUIDE_FEATURES)} özellik ailesinin kapsam envanteri',body=feature_md))
    mapping_md='''Mevcut 107 maddenin kimliği, bağlantı çapası ve içeriği korunur. Her madde aşağıda bir ana açıklamaya bağlanır; ilgili bölümden kontrol listesine geri dönülebilir. Dar teknik konular ileri eklerde ve özgün maddede ayrıntılı kalır. Bu eşleme, bilgiyi kaldırıp yerine yalnız genel bölüm adı koymak için kullanılmaz.

| Madde | Korunan konu | Ayrıntılı açıklama |
|---|---|---|
'''
    for id,slug in GUIDE_ITEM_MAP.items():
        i=lookup[id]
        mapping_md+=f'| [{id}](../codex-kontrol-listesi.md#{i["anchor"]}) | {i["title"]} | [{titles[slug]}]({slug}.md) |\n'
    pages.append(dict(slug='esleme',title='107 maddenin rehberle eşlemesi',body=mapping_md))
    source_md='''Ürün açıklamaları ile deneyimden çıkan öneriler farklı kanıtlardır. Aşağıdaki resmî sayfalar indirilip rehberin ilgili iddiaları için gerekli bölümleri incelendi. Listenin tamamını baştan sona satır satır denetlediğimiz veya her davranışı çalıştırdığımız iddia edilmez. Menü adları resmî belgedeki adları izler; kurulu sürüm ve hesabında ayrıca farklılık olabilir.

**Kontrol tarihleri:** Her kaynağın tarihi aşağıdaki dizinde ayrı gösterilir. Kaynak URL'si, indirme durumu ve içerik SHA-256 özeti [kaynak manifestinde](kaynak-manifest.json) kayıtlıdır. SHA-256, kontrol edilen dosya sürümünü ayırt eder; doğruluğunu veya gelecekte değişmeyeceğini garanti etmez. Kaynakların tam metin kopyaları bu depoda yayımlanmaz.

Gerçek vaka kayıtlarının kapsamı [deneyim ekinde](deneyimler.md); kurgu öğretim örnekleri [senaryo ekinde](senaryolar.md) açıklanır. Özel proje dosyaları ve ham sohbetler kamuya eklenmez. Tarihli ürün bilgisi ile kendi iş akışı önerimizi aynı kesinlikle sunmayız.

## Kaynak dizini

| Resmî sayfa | Kontrol tarihi |
|---|---|
'''
    for src in GUIDE_SOURCES.values(): source_md+=f'| [{src["title"]}]({src["url"]}) | {src["checked"]} |\n'
    source_md+='\n## Arayüz görselleri ve atıf\n\nAltı resmî arayüz gösterimi OpenAI belgelerinden içerikleri değiştirilmeden alındı. İki önce/sonra görüntüsü kurgu HTML sayfalarının gerçek tarayıcı çekimidir. Üç yeni görsel, düzenlenebilir Atölye sunumunun önce/sonra görünümünü ve CSV verisinden hesaplanan grafiği gösterir. Bunlar Codex uygulamasının oturum ekranı değildir. Her görselin türü ve kaynağı altında yazılıdır. Yanlarındaki Nereye bak / Ne yap / Ne gör açıklamaları bizim öğretim yorumumuzdur. Kaynak ve dosya özeti [görsel manifestinde](gorsel-manifest.json) kayıtlıdır. OpenAI ve diğer hak sahiplerine ait görseller metnin CC BY 4.0 lisansına dahil değildir. Rehber için yazılmış örnek dosyalar ve onların ekran görüntüleri rehber lisansını izler.\n\n'
    source_md+='| Görsel | Resmî sayfa | Kayıt tarihi |\n|---|---|---|\n'
    for f in GUIDE_FIGURES.values():source_md+=f'| [{f["title"]}]({f["file"]}) | [Kaynak]({f["source"]}) | {f["checked"]} |\n'
    source_md+='''
## Yapılan ve yapılmayan doğrulama

İçerik üretimi, iç bağlantılar, 107 madde eşlemesi ve web davranışı depo testleriyle kontrol edilir. Son koşumun sonucu [doğrulama raporunda](../DOGRULAMA.md) bulunur. Kod örneklerinin hepsini çalıştırmak, gerçek gönderim yapmak, otomasyon kurmak veya hesap izinlerini değiştirmek bu içerik işinin parçası değildir.

Yerel çıktı, uzak depoya gönderim ve canlı yayın ayrı durumlardır. Eski kontrol listesinin geçmiş yayın kanıtı, bu yeni rehberin yayımlandığı anlamına gelmez. Bu sürümün teslim durumu da aynı doğrulama raporunda ayrıca belirtilir.
'''
    pages.append(dict(slug='kaynaklar',title='Kaynaklar, kanıt türleri ve güncellik',body=source_md))
    intro=GUIDE_INTRO+'\n## Tam içindekiler\n\n'+'\n'.join(f'{c["number"]}. [{c["title"]}]({c["slug"]}.md)' for c in GUIDE_CHAPTERS)+'\n\n## Ekler ve hızlı erişim\n\n'+'\n'.join(f'- [{p["title"]}]({p["slug"]}.md)' for p in pages[18:] if 'journey' not in p)+'\n\n[107 maddelik hızlı kontrol listesine dön](../codex-kontrol-listesi.md) · [Tek dosyada rehberi indir](tam-rehber.md)\n'
    (OUT/'README.md').write_text('# Codex’i Derinlemesine Kullanma Rehberi\n\n'+markdown_output(intro))
    (OUT/'index.html').write_text(page_html('Codex’i Derinlemesine Kullanma Rehberi',intro,'index',next_=GUIDE_ROUTE[0]))
    full=['# Codex’i Derinlemesine Kullanma Rehberi',GUIDE_INTRO]
    for index,p in enumerate(pages):
        prev=GUIDE_CHAPTERS[index-1] if 0<index<18 else None
        next_=GUIDE_CHAPTERS[index+1] if index<17 else None
        if 'journey' in p:
            pos=p['journey']-1
            prev=GUIDE_PATHS[pos-1] if pos>0 else None
            next_=GUIDE_PATHS[pos+1] if pos<2 else GUIDE_ROUTE[4]
        navigation='\n\n[İçindekiler](README.md)'
        if prev: navigation+=f' · [← {prev["title"]}]({prev["slug"]}.md)'
        if next_: navigation+=f' · [{next_["title"]} →]({next_["slug"]}.md)'
        title=(str(p['number'])+'. ' if 'number' in p else '')+p['title']
        (OUT/(p['slug']+'.md')).write_text(f'# {title}\n\nİçerik güncellemesi: {GUIDE_UPDATED}. Kaynak kontrol tarihleri kaynak dizinindedir.\n\n'+markdown_output(p['body'])+navigation+'\n')
        (OUT/(p['slug']+'.html')).write_text(page_html(title,p['body'],p['slug'],prev,next_))
        full += ['\n# '+title,markdown_output(p['body'])]
    (OUT/'tam-rehber.md').write_text('\n\n'.join(full)+'\n')
    (OUT/'kaynak-manifest.json').write_text(json.dumps(dict(initial_checked=GUIDE_DATE,updated=GUIDE_UPDATED,sources=GUIDE_SOURCES),ensure_ascii=False,indent=2)+'\n')
    (OUT/'kapsam.json').write_text(json.dumps(dict(date=GUIDE_DATE,features=GUIDE_FEATURES,item_map=GUIDE_ITEM_MAP),ensure_ascii=False,indent=2)+'\n')
    (OUT/'gorsel-manifest.json').write_text(json.dumps(dict(date=GUIDE_UPDATED,figures=GUIDE_FIGURES),ensure_ascii=False,indent=2)+'\n')
    (OUT/'cikti-manifest.json').write_text(json.dumps(GUIDE_ARTIFACTS,ensure_ascii=False,indent=2)+'\n')
    return dict(chapters=18,appendices=len(pages)-18,features=len(GUIDE_FEATURES),mapped=len(GUIDE_ITEM_MAP))

if __name__=='__main__': print(build_guide())

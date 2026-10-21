"""Python 3 standard library only. Run from any directory."""
from pathlib import Path
import json
import re
from content import SOURCES, SECTIONS, TOP_TEN

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATE = '21 Ekim 2026'
URL = 'https://ratipcan-uysal.github.io/codex-kontrol-listesi/'
REPO = 'https://github.com/ratipcan-uysal/codex-kontrol-listesi'
ORIGINAL = 'https://github.com/ratipcan-uysal/claude-code-kontrol-listesi'

def validate(sections, sources, top):
    items = [i for s in sections for i in s['items']]
    ids = [i['id'] for i in items]
    anchors = [i['anchor'] for i in items]
    assert len(ids) == len(set(ids)), 'duplicate item ID'
    assert len(anchors) == len(set(anchors)), 'duplicate anchor'
    for n, section in enumerate(sections, 1):
        assert section['number'] == n
        for j, i in enumerate(section['items'], 1):
            assert i['id'] == f'{n}.{j}' and i['anchor'] == f'm-{n}-{j}'
            assert all(isinstance(i.get(k), str) and i[k].strip() for k in
                       ('title','why','how','example','verify','surface','kind','reviewed'))
            assert type(i['basic']) is bool
            assert i['source'] in sources
    assert len(top) == 10 and len(set(top)) == 10 and set(top) <= set(ids)
    assert all(url.startswith('https://') for _, url in sources.values())
    return items

def build():
    items = validate(SECTIONS, SOURCES, TOP_TEN)
    basic = sum(i['basic'] for i in items)
    counts = {'sections':len(SECTIONS), 'items':len(items), 'basic':basic, 'advanced':len(items)-basic}
    stats = f"{len(SECTIONS)} bölüm · {len(items)} madde · {basic} temel · {len(items)-basic} ileri"
    payload = dict(sections=SECTIONS, sources=SOURCES, topTen=TOP_TEN, version=1,
                   updated='2026-10-21', revision=2)
    replacements = {
        '__CSS__':(HERE/'style.css').read_text(), '__JS__':(HERE/'app.js').read_text(),
        '__DATA__':json.dumps(payload, ensure_ascii=False).replace('</', '<\\/'),
        '__TOTAL__':str(len(items)), '__BASIC__':str(basic), '__ADVANCED__':str(len(items)-basic),
        '__DATE__':DATE, '__REPO__':REPO, '__URL__':URL, '__STATS__':stats,
    }
    html = (HERE/'template.html').read_text()
    for key,value in replacements.items():
        html = html.replace(key,value)
    assert not re.search(r'__[A-Z]+__', html), 'unresolved template token'
    (ROOT/'index.html').write_text(html, encoding='utf-8')
    md = ['# Codex kullanım kontrol listesi', '', f'**{stats} · {DATE}**', '',
          f'[Etkileşimli rehberi aç]({URL}) · [Değişiklikler](GUNCELLEMELER.md) · [Kaynak denetimi](KAYNAKLAR.md)', '',
          'Codex ile çalışırken bağlamı, görev sınırını, araçları ve doğrulamayı düzenlemek için Türkçe bir rehber. Her maddede neden, nasıl, örnek ve doğrulama bulunur.', '',
          '## Kullanım', '',
          '- İlk turda aşağıdaki on maddeyle başla; her gelişmiş ayarı kurmak zorunda değilsin.',
          '- Etkileşimli sayfada arama, temel/ileri ve yapılmamış filtreleri vardır. İşaretler yalnız o tarayıcıda tutulur; JSON ile yedeklenir.',
          '- Eski ChatGPT Sites sürümündeki işaretler otomatik taşınmaz. Oradan JSON dışa aktarıp yeni sayfada içe alabilirsin.',
          '- Örnekler kendiliğinden çalışmaz. Yol ve dosya adlarını kendi projenle eşleştir; kurulu istemcinin yardımını kontrol et.',
          '- Ürün bilgisi ile editoryal iş akışı önerisi her maddede ayrılır. Kaynaklar dayanak ve ileri okuma içindir; önerilerin tamamı resmî OpenAI kuralı değildir.', '',
          '## Önce bu on madde', '']
    lookup = {i['id']:i for i in items}
    md += [f"{n}. **{id}** {lookup[id]['title']}" for n,id in enumerate(TOP_TEN,1)]
    md += ['', '## Kapsam ve sürüm', '',
           '21 Ekim 2026 tarihli resmî belge kontrolü. CLI eğik çizgi komutları interaktif terminal içindir; masaüstü, IDE ve web yüzeylerinde aynı komutun bulunduğunu varsayma.', '',
           'Bu denetimde PATH üzerindeki CLI 0.132.0, masaüstüyle gelen CLI 0.163.0-alpha.10.2 olarak gözlendi. Seçili bayraklar güncel ikilinin --help çıktısıyla kontrol edildi. Tüm örneklerin canlı koşum, hesap erişimi veya işletim sistemi uyumluluğu test edilmedi.', '',
           'Hook ve izin profili desteği değişebilir. Bir dosyanın varlığı, ayarın yüklendiğini veya güvenlik sınırının uygulandığını kanıtlamaz.', '']
    for s in SECTIONS:
        md += [f"## {s['number']}. {s['title']}", '', s['intro'], '']
        for i in s['items']:
            md += [f"### {i['id']} {i['title']}", '',
                   f"**{'Temel' if i['basic'] else 'İleri'} · {i['surface']} · {i['kind']}**", '',
                   f"**Neden:** {i['why']}", '', f"**Nasıl:** {i['how']}", '',
                   '```text',i['example'],'```','',f"**Doğrula:** {i['verify']}",'']
            if i['note']: md += [i['note'],'']
            name,url = SOURCES[i['source']]
            md += [f'Kaynak: [{name}]({url})','']
    md += ['## Kaynak, atıf ve lisans', '',
           f'Ratipcan Uysal’ın [Claude Code kontrol listesinin]({ORIGINAL}) Codex için yeniden yazılmış ve genişletilmiş sürümüdür. Resmî OpenAI yayını değildir.', '',
           'Copyright © 2026 Ratipcan Uysal. [CC BY 4.0](LICENSE). Kod, içerik ve değişiklikler bu depoda incelenebilir.', '',
           '## Katkı ve yerel çalıştırma', '',
           'İçeriğin tek kaynağı `kaynak/content.py` dosyasıdır. Üretilen HTML ve Markdown dosyalarını doğrudan düzenlemek yerine kaynağı güncelle.', '',
           '```sh', 'python3 kaynak/build.py', 'python3 kaynak/test_build.py', 'python3 -m http.server 8000 --bind 127.0.0.1', '```', '',
           'Tarayıcıda `http://127.0.0.1:8000` aç. Derleme için Python 3 standart kütüphanesi yeterlidir; npm kurulumu gerekmez. Düzeltme önerilerinde madde kimliği, kaynak bağlantısı ve gerekçeyi ekle.', '']
    text = '\n'.join(md)
    (ROOT/'README.md').write_text(text, encoding='utf-8')
    (ROOT/'codex-kontrol-listesi.md').write_text(text, encoding='utf-8')
    evidence = ['# Kaynak ve kapsam denetimi', '', f'Tarih: {DATE}. İçerik: {stats}.', '',
                'Resmî OpenAI sayfalarının güncel birleşik kılavuzu indirilip ilgili bölümler okunmuştur. Aşağıdaki bağlantılar maddelerin dayanaklarını gösterir. Apple ve Git bağlantıları kendi platform belgeleridir.', '',
                'Ürün davranışı, yerel CLI yardım doğrulaması ve editoryal öneri farklı kanıtlardır. Web sayfasının çalışması, örneklerdeki bütün Codex davranışlarının çalıştırıldığı anlamına gelmez.', '',
                '| Kaynak | Bağlı maddeler |', '|---|---|']
    for key,(name,url) in SOURCES.items():
        ids = [i['id'] for i in items if i['source']==key]
        if ids: evidence.append(f"| [{name}]({url}) | {', '.join(ids)} |")
    evidence += ['', '## Sınırlar', '',
                 '- CLI yardım kontrolü: 0.163.0-alpha.10.2 için sandbox, onay, exec JSONL/son mesaj/şema, review, MCP ve plugin komutlarının arayüzü.',
                 '- NOT_RUN: gerçek model karşılaştırması, tüm hook/izin senaryoları, zamanlanmış görev koşumları ve rehberdeki mobil örnekler.',
                 '- Sayfa işlevleri ve yayın kontrolü ayrı olarak [doğrulama raporunda](DOGRULAMA.md) kaydedilir.', '']
    (ROOT/'KAYNAKLAR.md').write_text('\n'.join(evidence), encoding='utf-8')
    print(json.dumps(counts, ensure_ascii=False))

if __name__ == '__main__':
    build()

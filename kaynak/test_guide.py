"""Guide coverage, renderer safety, navigation and single-source invariants."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote,urlsplit
from unittest.mock import patch
import hashlib
import json
import re
import unittest
import csv
import io
from decimal import Decimal
from datetime import date
from collections import Counter
from content import GUIDE_ROUTE,GUIDE_ARTIFACTS,GUIDE_UPDATED,GUIDE_CHAPTERS,GUIDE_APPENDICES,GUIDE_FEATURES,GUIDE_ITEM_MAP,GUIDE_SOURCES,GUIDE_FIGURES,GUIDE_PATHS,GUIDE_FLOWS,GUIDE_EXAMPLES,SECTIONS
from guide_build import ROOT,OUT,build_guide,validate_guide,render_markdown,slugify,inline,markdown_output

class Links(HTMLParser):
    def __init__(self): super().__init__(); self.ids=[]; self.links=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.append(attrs['id'])
        if tag=='a' and 'href' in attrs: self.links.append(attrs['href'])

class GuideTests(unittest.TestCase):
    def test_all_107_ids_and_anchors(self):
        counts=[7,7,7,4,6,7,6,7,7,3,6,6,5,6,4,4,5,4,6]
        expected={f'{n}.{j}':f'm-{n}-{j}' for n,count in enumerate(counts,1) for j in range(1,count+1)}
        actual={i['id']:i['anchor'] for s in SECTIONS for i in s['items']}
        self.assertEqual(expected,actual)
        self.assertEqual(set(expected),validate_guide())

    def test_missing_item_mapping_rejected(self):
        broken=dict(GUIDE_ITEM_MAP);del broken['1.1']
        with patch('guide_build.GUIDE_ITEM_MAP',broken),self.assertRaises(AssertionError):validate_guide()

    def test_unknown_feature_target_rejected(self):
        broken=[dict(f) for f in GUIDE_FEATURES];broken[0]['target']='missing'
        with patch('guide_build.GUIDE_FEATURES',broken),self.assertRaises(AssertionError):validate_guide()

    def test_sources_official_dated_and_successful(self):
        for s in GUIDE_SOURCES.values():
            self.assertIn(urlsplit(s['url']).netloc,{'learn.chatgpt.com','developers.openai.com','platform.openai.com'})
            self.assertEqual(s['status'],200)
            self.assertEqual(date.fromisoformat(s['checked']).isoformat(),s['checked'])
            self.assertLessEqual(date.fromisoformat(s['checked']),date.fromisoformat(GUIDE_UPDATED))
            self.assertRegex(s['sha256'],r'^[a-f0-9]{64}$')

    def test_all_28_app_commands_explained(self):
        body=next(p['body'] for p in GUIDE_APPENDICES if p['slug']=='komutlar')
        app_table=body.split('### Goals:')[0]
        commands=re.findall(r'^\| `(/[^`]+)`',app_table,re.M)
        expected='approve archive chat cloud cloud-environment compact fast feedback fork goal ide-context init local mcp memories model new pet pin plan project reasoning rename review side status usage worktree'.split()
        self.assertEqual(set(commands),{'/'+c for c in expected})
        self.assertEqual(len(commands),28)

    def test_renderer_escapes_code_and_rejects_unsafe_link(self):
        rendered,_=render_markdown('```html\n<script>alert(1)</script>\n```')
        self.assertNotIn('<script>',rendered)
        self.assertIn('&lt;script&gt;',rendered)
        with self.assertRaises(ValueError):inline('[bad](javascript:alert)')
        with self.assertRaises(ValueError):render_markdown('```text\nunclosed')

    def test_duplicate_headings_receive_unique_ids(self):
        rendered,_=render_markdown('## Başlık\n\n## Başlık')
        self.assertIn('id="baslik"',rendered);self.assertIn('id="baslik-2"',rendered)

    def test_html_local_links_and_anchors(self):
        for p in OUT.rglob('*.html'):
            page=Links();page.feed(p.read_text());self.assertEqual(len(page.ids),len(set(page.ids)),p.name)
            for url in page.links:
                u=urlsplit(url)
                if u.scheme or u.netloc:continue
                target=(p.parent/unquote(u.path)).resolve() if u.path else p
                self.assertTrue(target.exists(),f'{p.name}: {url}')
                if u.fragment and target.suffix=='.html':
                    other=Links();other.feed(target.read_text())
                    # Checklist articles are rendered from canonical JSON by app.js.
                    ids=set(other.ids)
                    if target==ROOT/'index.html':ids|={i['anchor'] for s in SECTIONS for i in s['items']}
                    self.assertIn(unquote(u.fragment),ids,f'{p.name}: {url}')

    def test_markdown_local_links_and_anchors(self):
        for p in OUT.rglob('*.md'):
            text=p.read_text()
            for url in re.findall(r'\]\(([^\s)]+)\)',text):
                u=urlsplit(url)
                if u.scheme or u.netloc:continue
                target=(p.parent/unquote(u.path)).resolve() if u.path else p
                self.assertTrue(target.exists(),f'{p.name}: {url}')
                if u.fragment and target.suffix=='.md':
                    t=target.read_text(); anchors=set(re.findall(r'<a id="([^"]+)"',t))
                    anchors|={slugify(x) for x in re.findall(r'^#{1,6} (.+)',t,re.M)}
                    self.assertIn(unquote(u.fragment),anchors,f'{p.name}: {url}')

    def test_every_page_generated_and_no_private_content(self):
        for p in GUIDE_CHAPTERS+GUIDE_APPENDICES:
            self.assertTrue((OUT/(p['slug']+'.md')).exists())
            self.assertTrue((OUT/(p['slug']+'.html')).exists())
        for path in OUT.rglob('*'):
            if not path.is_file() or path.suffix not in {'.md','.html','.json','.csv'}:continue
            text=path.read_text()
            self.assertNotRegex(text,r'source:|/Users/|rollout_summaries/|\.codex/sessions/|@[a-z0-9.-]+\.(?:com|net)\b')
            self.assertNotRegex(text,r'__[A-Z]+__')

    def test_figures_have_same_attribution_and_asset_in_both_formats(self):
        for key,f in GUIDE_FIGURES.items():
            token=f'[FIGURE:{key}]'
            rendered,_=render_markdown(token)
            md=markdown_output(token)
            self.assertIn('<figcaption>',rendered)
            self.assertIn(f['source'],rendered);self.assertIn(f['source'],md)
            self.assertIn(f'src="{f["file"]}"',rendered)
            self.assertIn(f']({f["file"]})',md)
            self.assertIn('loading="lazy"',rendered)
            self.assertIn('aria-label=',rendered)
            self.assertNotIn('[FIGURE:',rendered+md)
        with self.assertRaises(ValueError):render_markdown('[FIGURE:unknown]')

    def test_figure_asset_escape_and_changed_bytes_rejected(self):
        broken={k:dict(v) for k,v in GUIDE_FIGURES.items()}
        broken['projects']['file']='../index.html'
        with patch('guide_build.GUIDE_FIGURES',broken),self.assertRaises(AssertionError):validate_guide()
        broken['projects']=dict(GUIDE_FIGURES['projects'],sha256='0'*64)
        with patch('guide_build.GUIDE_FIGURES',broken),self.assertRaises(AssertionError):validate_guide()

    def test_github_markdown_has_matching_explicit_anchors(self):
        text='## Görünüm\n\n## Görünüm\n\n```text\n## Inside code\n```'
        md=markdown_output(text)
        html,_=render_markdown(text)
        anchors=re.findall(r'<a id="([^"]+)"',md)
        self.assertEqual(anchors,['gorunum','gorunum-2'])
        for a in anchors:self.assertIn(f'id="{a}"',html)

    def test_teaching_flows_have_parity_and_reject_unknown(self):
        self.assertEqual(len(GUIDE_PATHS),3)
        for key,f in GUIDE_FLOWS.items():
            token=f'[FLOW:{key}]';rendered,_=render_markdown(token);md=markdown_output(token)
            for label,text in f['steps']:
                self.assertIn(text,rendered);self.assertIn(text,md)
            self.assertNotIn('[FLOW:',rendered+md)
        with self.assertRaises(ValueError):render_markdown('[FLOW:unknown]')

    def test_example_data_preserves_identity_and_unknown_payment(self):
        raw=list(csv.DictReader(io.StringIO(GUIDE_EXAMPLES['katilim-ham.csv'])))
        clean=list(csv.DictReader(io.StringIO(GUIDE_EXAMPLES['katilim-temiz.csv'])))
        self.assertEqual(len(raw),6);self.assertEqual(len(clean),6)
        self.assertEqual(len({x['kayit_id'] for x in clean}),6)
        for a,b in zip(raw,clean):
            self.assertEqual({k:v for k,v in a.items() if k!='tahsilat_tl'},{k:v for k,v in b.items() if k!='tahsilat_tl'})
            if not a['tahsilat_tl']:self.assertEqual(b['tahsilat_tl'],'')
            else:self.assertEqual(Decimal(a['tahsilat_tl'].replace(' TL','').replace(',','.')),Decimal(b['tahsilat_tl']))
        self.assertEqual(sum(Decimal(x['tahsilat_tl']) for x in clean if x['tahsilat_tl']),Decimal(1800))
        self.assertEqual(Counter(x['durum'] for x in clean),{'katıldı':3,'iptal':2,'bekliyor':1})

    def test_examples_are_generated_from_canonical_source(self):
        for name,body in GUIDE_EXAMPLES.items():self.assertEqual((OUT/'ornekler'/name).read_text(),body)
        self.assertEqual(GUIDE_EXAMPLES['sayfa-once.html'].replace('width:440px','width:100%'),GUIDE_EXAMPLES['sayfa-sonra.html'])

    def test_no_markdown_left_in_rendered_prose(self):
        for p in OUT.glob('*.html'):
            text=p.read_text().split('<article class="prose">')[1].split('</article>')[0]
            self.assertNotRegex(text,r'\]\(|\*\*|```|\x00',p.name)

    def test_second_week_keeps_new_status_and_missing_amount(self):
        from example_data import summarize
        actual=summarize(GUIDE_EXAMPLES['katilim-hafta-2.csv'])
        self.assertEqual(actual,dict(rows=3,counts={'yedek':1,'katıldı':1,'bekliyor':1},missing=['K08'],total=Decimal(600),unknown=[('K07','yedek')]))
        duplicate=GUIDE_EXAMPLES['katilim-hafta-2.csv']+'K07,İkinci,yedek,100\n'
        with self.assertRaises(ValueError):summarize(duplicate)
        chart=list(csv.DictReader(io.StringIO(GUIDE_EXAMPLES['katilim-grafik.csv'])))
        self.assertEqual([(r['durum'],int(r['kayit_sayisi'])) for r in chart],[('katıldı',3),('iptal',2),('bekliyor',1)])

    def test_editable_deck_and_artifact_identity(self):
        import zipfile
        import xml.etree.ElementTree as ET
        for name,m in GUIDE_ARTIFACTS.items():self.assertEqual(hashlib.sha256((OUT/name).read_bytes()).hexdigest(),m['sha256'])
        ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
        with zipfile.ZipFile(OUT/'ornekler/atolye-karar.pptx') as z:
            slides=[n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide[0-9]+.xml',n)]
            self.assertEqual(len(slides),3)
            table=ET.fromstring(z.read('ppt/slides/slide2.xml')).findall('.//a:tbl',ns)
            self.assertEqual(len(table),1)
            strings=[t.text for t in table[0].findall('.//a:t',ns)]
            for x in ['Kayıt A','Kayıt B','Kayıt C','2.500 TL']:self.assertIn(x,strings)

    def test_teaching_route_has_one_next_step_and_no_restart(self):
        for i,p in enumerate(GUIDE_ROUTE):
            md=(OUT/(p['slug']+'.md')).read_text()
            if i<len(GUIDE_ROUTE)-1:
                self.assertIn('**Eğitimde sıradaki:** ['+GUIDE_ROUTE[i+1]['title']+']('+GUIDE_ROUTE[i+1]['slug']+'.md)',md)
            else:self.assertIn('Eğitim rotası tamamlandı.',md)
        self.assertNotIn('01-olanaklar',[p['slug'] for p in GUIDE_ROUTE])
        # Inserting a teaching stop must not turn the final journey's footer into a self-link.
        last_journey=(OUT/'is-sayfa.md').read_text().split('[İçindekiler](README.md)')[-1]
        self.assertNotIn('(is-sayfa.md)',last_journey)
        self.assertIn('(10-baglantilar-skills.md)',last_journey)

    def test_deterministic_generation(self):
        def digest():return {str(p.relative_to(OUT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.rglob('*') if p.is_file()}
        before=digest();build_guide();self.assertEqual(before,digest())

if __name__=='__main__':unittest.main()

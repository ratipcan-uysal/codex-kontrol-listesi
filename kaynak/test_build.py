"""Publication invariants, including negative cases. No third-party dependencies."""
import copy
import re
import unittest
from pathlib import Path
from build import validate
from content import SECTIONS, SOURCES, TOP_TEN

class ContentTests(unittest.TestCase):
    def test_valid_content(self):
        items = validate(SECTIONS, SOURCES, TOP_TEN)
        self.assertEqual((len(SECTIONS), len(items), sum(i['basic'] for i in items)), (19, 107, 25))

    def test_duplicate_id_rejected(self):
        broken = copy.deepcopy(SECTIONS)
        broken[0]['items'][1]['id'] = broken[0]['items'][0]['id']
        with self.assertRaisesRegex(AssertionError, 'duplicate item ID'):
            validate(broken, SOURCES, TOP_TEN)

    def test_missing_verification_rejected(self):
        broken = copy.deepcopy(SECTIONS)
        broken[0]['items'][0]['verify'] = ''
        with self.assertRaises(AssertionError):
            validate(broken, SOURCES, TOP_TEN)

    def test_unknown_source_rejected(self):
        broken = copy.deepcopy(SECTIONS)
        broken[0]['items'][0]['source'] = 'missing'
        with self.assertRaises(AssertionError):
            validate(broken, SOURCES, TOP_TEN)

    def test_existing_identifiers_preserved(self):
        old_counts = [6,6,7,4,5,6,6,5,6,3,6,6,5,4,4,4,5,4,5]
        ids = {i['id'] for s in SECTIONS for i in s['items']}
        self.assertEqual(sum(old_counts), 97)
        for n, count in enumerate(old_counts, 1):
            self.assertTrue({f'{n}.{j}' for j in range(1,count+1)} <= ids)

    def test_markdown_html_same_items(self):
        root = Path(__file__).resolve().parents[1]
        md = (root/'codex-kontrol-listesi.md').read_text()
        html = (root/'index.html').read_text()
        self.assertEqual(md, (root/'README.md').read_text())
        self.assertEqual(len(re.findall(r'^### \d+\.\d+ ', md, re.M)), 107)
        self.assertNotRegex(html, r'__[A-Z]+__')
        for s in SECTIONS:
            for i in s['items']:
                self.assertIn(i['title'], md)
                self.assertIn(i['title'], html)

if __name__ == '__main__':
    unittest.main()

"""Export canonical data for the optional Artifact Tool renderer."""
from pathlib import Path
import sys,json
from content import GUIDE_DECK,GUIDE_EXAMPLES
from example_data import summarize
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
(out/'deck.json').write_text(json.dumps(GUIDE_DECK,ensure_ascii=False))
(out/'chart.json').write_text(json.dumps(list(summarize(GUIDE_EXAMPLES['katilim-ham.csv'])['counts'].items()),ensure_ascii=False))

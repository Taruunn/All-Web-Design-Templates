import sys, os
from playwright.sync_api import sync_playwright
# usage: render.py in.svg out.png [scale] [transparent]
inp, out = sys.argv[1], sys.argv[2]
scale = float(sys.argv[3]) if len(sys.argv)>3 else 1
transparent = len(sys.argv)>4
import re
svg=open(inp).read()
W=float(re.search(r'width="([\d.]+)"',svg).group(1)); H=float(re.search(r'height="([\d.]+)"',svg).group(1))
with sync_playwright() as p:
    exe=os.environ.get('CHROMIUM_PATH')
    b=p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
    pg=b.new_page(viewport={'width':int(W),'height':int(H)}, device_scale_factor=scale)
    pg.set_content(f'<html><body style="margin:0;background:transparent">{svg}</body></html>')
    pg.screenshot(path=out, omit_background=transparent, clip={'x':0,'y':0,'width':W,'height':H})
    b.close()

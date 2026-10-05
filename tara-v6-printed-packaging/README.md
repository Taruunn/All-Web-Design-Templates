# tara V6: printed packaging options D and E

Two printed options added to the V6 packaging set on the TARA Fine Jewels canvas, alongside A Midnight, B Moonlight and C Wish.

- **D · Garden**: Moon lid printed with a fine-line botanical (Vanda Miss Joaquim orchid, frangipani, fan palm, gold-foil persimmons, one sunbird) around a gold arched window that holds the logo. Midnight base.
- **E · Heirloom**: fabric keepsake case for heavy Indian pieces. Midnight cotton-silk printed with the Star Jaali (an ogee lattice with the tara star in every cell), rattan handle, Orchid tassel with a gold star charm.

## Files

- `artwork/` vector artwork: `garden-lid.svg` (1000 × 1000 lid), `garden-print.svg` (tissue and wrap layout), `star-jaali-print.svg` (fabric layout), `star-jaali-tile.svg` (seamless repeat tile, 192 × 268).
- `mockups/` the rendered JPGs used on the canvas boards.
- `src/` the Python that draws everything. `python3 src/scenes_d2.py` and `python3 src/scenes_e.py` write the SVGs, and `python3 src/render.py in.svg out.png` rasterises one with Chromium (needs `pip install playwright pillow`; set `CHROMIUM_PATH` to use a specific Chromium).

Gold is drawn as a gradient so it previews like foil. For print, the printer should pull every gold element onto its own foil layer. Palm green `#A7B19F` is a new print-only colour. Everything else uses the V6 palette.

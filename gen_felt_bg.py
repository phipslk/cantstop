"""Dunkler Casino-Filz-Hintergrund mit goldenen Zierlinien, fuer Panel und
Spielbrett-Rand. Chunkiges Retro-Pixel-Rendering (grobe Bloecke statt
Photoreal-Glaetten), damit es zum restlichen Spiel passt.
"""
import random
from PIL import Image, ImageDraw, ImageFilter

def clamp(v): return max(0, min(255, int(v)))

def felt_texture(W, H, base=(13, 58, 34), seed=1, block=3):
    random.seed(seed)
    img = Image.new("RGB", (W, H), base)
    px = img.load()
    for by in range(0, H, block):
        for bx in range(0, W, block):
            n = random.randint(-10, 10)
            col = (clamp(base[0]+n), clamp(base[1]+n*1.3), clamp(base[2]+n*0.6))
            for y in range(by, min(by+block, H)):
                for x in range(bx, min(bx+block, W)):
                    px[x, y] = col
    # sehr feines Rauschen obendrauf fuer Stoff-Anmutung
    for _ in range(W * H // 6):
        x = random.randrange(W); y = random.randrange(H)
        n = random.randint(-14, 14)
        r, g, b = px[x, y]
        px[x, y] = (clamp(r+n), clamp(g+n), clamp(b+n))
    return img

def vignette(img, strength=90):
    W, H = img.size
    v = Image.new("L", (W, H), 0)
    dv = ImageDraw.Draw(v)
    dv.ellipse([-W*0.25, -H*0.25, W*1.25, H*1.25], fill=255)
    v = v.filter(ImageFilter.GaussianBlur(min(W, H) * 0.12))
    dark = Image.new("RGB", (W, H), (0, 0, 0))
    return Image.composite(img, dark, v.point(lambda p: 255 - int((255-p) * strength/255)))

GOLD = (214, 168, 74)
GOLD_HI = (255, 224, 150)
GOLD_LO = (120, 84, 24)

def draw_gold_frame(d, x0, y0, x1, y1, inset=10, w=3):
    # Doppelte Zierlinie GENAU am inset - das definiert die Grenze des
    # nutzbaren Innenbereichs, an die sich der Hollywood-Code exakt haelt
    # (panelMargin/boardMargin muessen mit diesem inset uebereinstimmen).
    d.rectangle([x0+inset-4, y0+inset-4, x1-inset+4, y1-inset+4], outline=GOLD_LO)
    d.rectangle([x0+inset-2, y0+inset-2, x1-inset+2, y1-inset+2], outline=GOLD_HI)
    d.rectangle([x0+inset,   y0+inset,   x1-inset,   y1-inset],   outline=GOLD)

def corner_flourish(d, cx, cy, flip_x=1, flip_y=1, size=22):
    s = size
    pts = []
    for t in range(0, 91, 6):
        import math
        rad = math.radians(t)
        x = cx + flip_x * s * math.sin(rad)
        y = cy + flip_y * s * (1 - math.cos(rad))
        pts.append((x, y))
    d.line(pts, fill=GOLD, width=2)
    d.ellipse([cx-3, cy-3, cx+3, cy+3], fill=GOLD_HI)

def make_panel_bg(W=300, H=555):
    img = felt_texture(W, H, seed=7)
    img = vignette(img, strength=70)
    d = ImageDraw.Draw(img)
    # inset=8, wie beim Board - der Rahmen sass vorher bei 14 und wirkte dadurch
    # deutlich kleiner/eingerueckter als der Board-Rahmen (naeher am Bildrand
    # gesetzt bei nur 8). Gleicher inset -> Rahmen wirkt links/rechts gleich
    # gross. Inhalt startet weiterhin bei panelMargin=22, jetzt mit 14px statt
    # 8px Luft zur Linie - unkritisch, nur mehr Abstand.
    draw_gold_frame(d, 0, 0, W-1, H-1, inset=8)
    return img

def make_board_bg(W=510, H=555):
    img = felt_texture(W, H, seed=3)
    img = vignette(img, strength=60)
    d = ImageDraw.Draw(img)
    draw_gold_frame(d, 0, 0, W-1, H-1, inset=8)   # unveraendert, Board-Layout ist eng bemessen
    return img

if __name__ == "__main__":
    out = r"C:\Users\Philipp\AppData\Local\Temp\claude\C--Users-Philipp-OneDrive-Dokumente-claude\ae39f59a-7fca-4682-9b9e-d192f8e20b4e\scratchpad"
    panel = make_panel_bg()
    board = make_board_bg()
    panel.save(f"{out}/panel_bg.png")
    board.save(f"{out}/board_bg.png")

    # Mockup: beide nebeneinander wie im Spiel (Board links, Panel rechts)
    mock = Image.new("RGB", (810, 555))
    mock.paste(board, (0, 0))
    mock.paste(panel, (508, 0))
    mock.save(f"{out}/bg_mockup_full.png")
    print("gespeichert:", panel.size, board.size)

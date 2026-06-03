"""
Groundwork icon generator — Cornerstone (isometric cube)
4x supersampling with PIL
Produces: groundwork-icon-512.png, groundwork-icon-192.png, groundwork-icon-32.png
"""
from PIL import Image, ImageDraw
import math

def lerp_color(c1, c2, t):
    return tuple(int(a * (1 - t) + b * t) for a, b in zip(c1, c2))

def make_icon(size, scale=4):
    s = size * scale
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    bg = (12, 21, 38, 255)
    radius = int(s * 0.22)
    d.rounded_rectangle([0, 0, s-1, s-1], radius=radius, fill=bg)

    # Cube vertex positions (from the SVG, normalized to 96x96 grid)
    # Top face:   (48,16) (82,35) (48,54) (14,35)
    # Left face:  (14,35) (48,54) (48,84) (14,65)
    # Right face: (82,35) (48,54) (48,84) (82,65)
    def v(nx, ny):
        return (int(nx / 96 * s), int(ny / 96 * s))

    top   = [v(48,16), v(82,35), v(48,54), v(14,35)]
    left  = [v(14,35), v(48,54), v(48,84), v(14,65)]
    right = [v(82,35), v(48,54), v(48,84), v(82,65)]

    green = (52, 211, 153)
    bg3   = (12, 21, 38)

    # Pre-blend green onto dark bg at each opacity level
    def blend(g, b, alpha):
        return tuple(int(b[i]*(1-alpha) + g[i]*alpha) for i in range(3)) + (255,)

    d.polygon(top,   fill=blend(green, bg3, 0.92))
    d.polygon(right, fill=blend(green, bg3, 0.65))
    d.polygon(left,  fill=blend(green, bg3, 0.42))

    # Thin edge lines to crisp up faces at larger sizes
    if size >= 192:
        edge = blend(green, bg3, 0.20)
        lw = max(1, s // 256)
        for poly in [top, left, right]:
            pts = poly + [poly[0]]
            for i in range(len(pts)-1):
                d.line([pts[i], pts[i+1]], fill=edge, width=lw)

    img = img.resize((size, size), Image.LANCZOS)
    return img

for sz in [512, 192, 32]:
    icon = make_icon(sz, scale=4)
    fname = f"groundwork-icon-{sz}.png"
    icon.save(fname)
    print(f"Saved {fname}")

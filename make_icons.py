"""Membuat icon-192.png, icon-512.png, apple-touch-icon.png: kapal tanker LNG (lambung biru-merah, tabung LNG putih bertulisan LNG) di atas gradasi biru (sama dengan latar menu) + gelombang. Tanpa pustaka luar."""
import math, zlib, struct

def inside(poly, x, y):
    c = False
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c

def wave(y0, amp=2.2, w=100.0, th=2.6, x0=8, x1=92, n=48):
    top = [(x0 + (x1 - x0) * i / n, y0 + amp * math.sin(i / n * 2 * math.pi * 2.5)) for i in range(n + 1)]
    return top + [(x, y + th) for x, y in reversed(top)]

WHITE = (255, 255, 255); SKY = (125, 211, 252); DEEP = (14, 47, 110)
BLUE = (29, 78, 216); RED = (185, 28, 28); GREEN = (22, 163, 74); GREY = (229, 231, 235)

def rect(x, y, w, h): return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]

def capsule(x, y, w, h, n=10):
    r = h / 2; pts = []
    for i in range(n + 1):
        t = -math.pi / 2 + math.pi * i / n; pts.append((x + w - r + r * math.cos(t), y + r + r * math.sin(t)))
    for i in range(n + 1):
        t = math.pi / 2 + math.pi * i / n; pts.append((x + r + r * math.cos(t), y + r + r * math.sin(t)))
    return pts

def letters(x, y, h=5.0, w=4.4, t=1.1, gap=1.4):
    # huruf L N G dari persegi/poligon tebal
    out = []
    out += [rect(x, y, t, h), rect(x, y + h - t, w, t)]                                   # L
    x += w + gap
    out += [rect(x, y, t, h), rect(x + w - t, y, t, h), [(x, y), (x + 1.3, y), (x + w, y + h), (x + w - 1.3, y + h)]]  # N
    x += w + gap
    out += [rect(x, y, w, t), rect(x, y, t, h), rect(x, y + h - t, w, t), rect(x + w - t, y + h / 2, t, h / 2), rect(x + w / 2, y + h / 2 - t / 2, w / 2, t)]  # G
    return [(DEEP, p) for p in out]

# urutan = tumpukan, yang belakangan menimpa yang awal. Koordinat 0..100
SHAPES = [
    (SKY, wave(70, amp=1.6, th=2.0)), (SKY, wave(77, amp=1.6, th=2.0)),
    (RED, [(9, 46), (89, 46), (86, 63), (20, 63)]),                              # lambung bawah
    (BLUE, [(9, 46), (89, 46), (87.1, 57), (16.1, 57)]),                         # lambung atas
    (GREEN, rect(11, 42.5, 60, 3.5)),                                            # dek
    (WHITE, rect(72, 30, 16, 16)),                                               # bangunan atas
    (WHITE, rect(74, 23.5, 12, 6.5)), (DEEP, rect(75, 25.5, 10, 2.6)),           # anjungan + jendela
    (WHITE, rect(79.6, 14, 1.4, 9.5)),                                           # tiang
    (WHITE, rect(14, 35, 1.6, 11)), (GREY, rect(20, 40, 9, 3)),                  # tiang haluan, pipa
    (WHITE, capsule(36, 34, 24, 10)),                                            # tabung LNG (diperkecil)
] + letters(39.4, 36.5)

def bg(px, py, size):
    # gradasi radial seperti latar menu: terang di tengah atas, gelap di tepi
    dx = (px / size - 0.5) / 1.2; dy = (py / size - 0.2) / 0.9
    t = min(1.0, math.sqrt(dx * dx + dy * dy) / 0.95)
    stops = [(0.0, (26, 79, 184)), (0.45, (14, 47, 110)), (1.0, (8, 20, 46))]
    for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
        if t <= t1:
            u = (t - t0) / (t1 - t0)
            return tuple(c0[i] + (c1[i] - c0[i]) * u for i in range(3))
    return stops[-1][1]

def render(size):
    ss = 3
    rows = []
    for py in range(size):
        row = bytearray([0])
        for px in range(size):
            base = bg(px, py, size)
            acc = [0.0, 0.0, 0.0]
            for sy in range(ss):
                for sx in range(ss):
                    x = (px + (sx + .5) / ss) / size * 100
                    y = (py + (sy + .5) / ss) / size * 100
                    col = base
                    for c, poly in SHAPES:
                        if inside(poly, x, y): col = c
                    for i in range(3): acc[i] += col[i]
            row += bytes(int(a / (ss * ss)) for a in acc)
        rows.append(bytes(row))
    raw = b"".join(rows)
    def chunk(t, d):
        c = struct.pack(">I", len(d)) + t + d
        return c + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")

for name, s in (("icon-192.png", 192), ("icon-512.png", 512), ("apple-touch-icon.png", 180)):
    open(name, "wb").write(render(s))
    print(name)

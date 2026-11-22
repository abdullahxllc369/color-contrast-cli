"""Calculate the relative luminance contrast ratio for two opaque sRGB colors."""
import argparse
import re

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('colors', nargs=2)
a = p.parse_args()

def luminance(color):
    if not re.fullmatch(r'#?[0-9a-fA-F]{6}', color):
        p.error('Use six hex digits per color.')
    rgb = bytes.fromhex(color.lstrip('#'))
    channels = [v / 255 for v in rgb]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in channels]
    return sum(c * w for c, w in zip(linear, (0.2126, 0.7152, 0.0722)))

dark, light = sorted(map(luminance, a.colors))
print(f'{(light + 0.05) / (dark + 0.05):.2f}:1')

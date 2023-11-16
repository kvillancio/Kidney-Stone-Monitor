# -*- coding: utf-8 -*-
import math

COLORS = (
    (246,233,204),
    (247,235,235),
    (241,215,224),
    (229,191,214),
    (248,178,28),
    (249,192,89),
    (249,210,93),
    (229,197,1),
    (194,187,8),
    (171,179,16),
    (95,250,219)
)

##this code came from stack overflow by mVCHr and edited by Adam Jenca
def closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diff = math.sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]








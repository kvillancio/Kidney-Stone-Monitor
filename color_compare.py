import math

# COLORS = (
#     (246,233,204),
#     (247,235,235),
#     (241,215,224),
#     (229,191,214),
#     (248,178,28),
#     (249,192,89),
#     (249,210,93),
#     (229,197,1),
#     (194,187,8),
#     (171,179,16),
#     (95,250,219)
# )

##this code came from stack overflow by mVCHr and edited by Adam Jenca
def closest_color(cal_strip, pH_strip, cal_chart):
    r_cal, g_cal, b_cal = cal_strip
    r_pH, g_pH, b_pH = pH_strip
    color_diffs_calcium = []
    for color in cal_chart:
        cr, cg, cb = color
        color_diff = math.sqrt((r_cal - cr)**2 + (g_cal - cg)**2 + (b_cal - cb)**2)
        color_diffs_calcium.append((color_diff, color))
    
    color_diffs_pH = []
    for color in cal_chart:
        ce, cf, cj = color
        color_diff = math.sqrt((r_pH - cr)**2 + (g_pH - cg)**2 + (b_pH - cb)**2)
        color_diffs_pH.append((color_diff, color))
        closest_calcium = min(color_diffs_calcium)[1]
        closest_pH = min(color_diffs_pH)[1]
        return color_diffs_calcium.index(closest_calcium), color_diffs_pH.index(closest_pH)








import math

def closest_color(cal_strip, pH_strip, chart_ph, chart_ca):
    r_cal, g_cal, b_cal = cal_strip
    r_pH, g_pH, b_pH = pH_strip
    color_diffs_calcium = []
    for color in chart_ca:
        cr, cg, cb = color
        print(cr)
        print(cg)
        print(cb)
        color_diff = math.sqrt((r_cal - cr)**2 + (g_cal - cg)**2 + (b_cal - cb)**2)
        color_diffs_calcium.append((color_diff, color))
    
    color_diffs_pH = []
    for color in chart_ph:
        ce, cf, cj = color
        color_diff = math.sqrt((r_pH - ce)**2 + (g_pH - cf)**2 + (b_pH - cj)**2)
        color_diffs_pH.append((color_diff, color))
    
    closest_calcium = min(color_diffs_calcium) #[1]
    closest_pH = min(color_diffs_pH) #[1]
    
    return color_diffs_calcium.index(closest_calcium), color_diffs_pH.index(closest_pH)

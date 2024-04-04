# import libraries
from PIL import Image
import cv2
import numpy as np

# import function scripts
import chart_location as chart
import test_strip_finder as strip
import color_compare as compare
# import scaling

filename = '1mb_test.jpg'

# locate strip
strip_ph = strip.ph_strip_finder(filename)
strip_ca = strip.calc_strip_finder(filename)

# locate calibration chart
img = cv2.imread(filename)
[chart_ph,chart_ca] = chart.ph_and_ca_calibration_finder(img)

# compare colors
[diff_ph, diff_ca]=compare.comp(strip_ca, strip_ph,chart_ph,chart_ca)



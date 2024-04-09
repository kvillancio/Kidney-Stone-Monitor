# import libraries
from PIL import Image
import cv2
import numpy as np

# import function scripts
import chart_location as chart
import test_strip_finder as strip
import color_compare as compare
import pH_calcium_values as values
#import scaling_ca as scale

filename = 'test3.jpg'

# locate strip
strip_ph = strip.ph_strip_finder(filename)
strip_ca = strip.calc_strip_finder(filename)
print(strip_ph)
print(strip_ca)

# locate calibration chart
img = cv2.imread(filename)
[chart_ph,chart_ca] = chart.get_ph_and_ca_calibration_values(filename)
print(chart_ph)
print(chart_ca)

# compare colors
[index_ca, index_ph]=compare.closest_color(strip_ca, strip_ph,chart_ph,chart_ca)

print(index_ph)
print(index_ca)


#use index to get ca and ph values
[ph_value,ca_value]=values.pH_calcium_values(index_ph,index_ca)




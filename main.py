# import libraries
from PIL import Image
import cv2
import numpy as np

# import function scripts
import mapper
import scanner
import location_script
import color_compare
import pH_calcium_values

filename = input('Filename: ')

# scan and crop image
scanned_img = scanner.scan(filename)

# locate strip and calibration
[strip_ph, strip_ca] = location_script.strip(scanned_img)
[cal_ph, cal_ca] = location_script.cal(scanned_img)

# compare colors
ph_comp = color_compare.comp(strip_ph, cal_ph)
ca_comp = color_compare.comp(strip_ca, cal_ca)

# find pH and calcium values
[pH, calc] = pH_calcium_values.vals(ph_comp, ca_comp)

print('Results from urine sample:')
print('pH: ' + pH)
print('Calcium concentration: ' + calc + ' mmol/day')

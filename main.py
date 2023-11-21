# import all function scripts

from PIL import Image
import cv2
import numpy as np

import mapper
import scanner
import location_script
import color_compare
import pH_calcium_values

filename = input('Filename: ')

# scan and crop image
scanned_img = scanner.scan(filename)

# locate calibration

# locate strip

# compare colors

# find pH and calcium values
print('Results from urine sample:')
print('pH: ' + pH)
print('Calcium concentration: ' + calc + ' mmol/day')

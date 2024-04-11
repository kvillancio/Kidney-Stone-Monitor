# import libraries
from PIL import Image
import cv2
import numpy as np

# import function scripts
import chart_location_v2 as chart
import test_strip_finder_v2 as strip
import color_compare as compare
import pH_calcium_values as values
#import scaling_ca as scale

filename ='scanned_lighting_1_1.png'

# locate strip
[strip_ph, strip_ca] = strip.get_strip_values(filename)
print(f'pH strip square rgb value: {strip_ph}')
print(f'Ca strip square rgb value: {strip_ca}')

# locate calibration chart
img = cv2.imread(filename)
[chart_ph,chart_ca] = chart.ph_and_ca_calibration_finder(filename)
print('\nAverage pH Calibration Chart RGB Values:')
i = 1
for item in chart_ph:
    print(f'{i}. {item}')  
    i += 1
print('\nAverage Ca Calibration Chart RGB Values:')
i = 1
for item in chart_ca:
    print(f'{i}. {item}')  
    i += 1


# compare colors
[index_ca, index_ph]=compare.closest_color(strip_ca, strip_ph, chart_ph,chart_ca)



#use index to get ca and ph values
[ph_value,ca_value]=values.pH_calcium_values(index_ph,index_ca)

import cv2
import numpy as np
import matplotlib.pyplot as plt

def ph_strip_finder(filename):
    # Load image
    img = cv2.imread(filename)
    
    # Get image dimensions
    h, w, _ = img.shape
    
    # Status variable for loop
    status = 0
    
    # Loop to detect dark line next to pH square
    for x in range(250,w):
        for y in range(h):
            col = img[y, x, :]
            if col[0] <= 100:  # x > 500 is for the dust particle
                status = 1
                break
        if status == 1:
            break
    
    # Initialize vectors
    r = []
    g = []
    b = []
    
    #print(x,y)
    
    # Loop to collect RGB values to the right of the detected point
    for j in range(2):
        for i in range(30, 40):
            col_up = img[y + j, x + i, :]
            r.append(col_up[0])
            g.append(col_up[1])
            b.append(col_up[2])
            col_down = img[y - j, x + i, :]
            r.append(col_down[0])
            g.append(col_down[1])
            b.append(col_down[2])
    
    # Calculate average RGB values
    avg_ph_col = [np.mean(b), np.mean(g), np.mean(r)]
    
    #print("Average pH RGB Values:", avg_ph_col)
    
    return avg_ph_col

def calc_strip_finder(filename):
    # Load image
    img = cv2.imread(filename)
    
    # Get image dimensions
    h, w, _ = img.shape
    
    # Status variable for loop
    status = 0
    
    # Loop to detect dark line
    for x in range(250,w):
        for y in range(h):
            col = img[y, x, :]
            if col[0] <= 100:  # found pH line
                for y2 in range(y+40,h): # jump down to find calcium line
                    col = img[y2, x+3, :]
                    if col[0] <= 100:
                        status = 1;
                        break
        if status == 1:
            break
    
    # Initialize vectors
    r = []
    g = []
    b = []
    
    #print(x,y2)
    
    # Loop to collect RGB values to the right of the detected point
    for j in range(2):
        for i in range(30, 40):
            col_up = img[y2 + j, x + i, :]
            r.append(col_up[0])
            g.append(col_up[1])
            b.append(col_up[2])
            col_down = img[y2 - j, x + i, :]
            r.append(col_down[0])
            g.append(col_down[1])
            b.append(col_down[2])
            
    
    # Calculate average RGB values
    avg_calc_col = [np.mean(b), np.mean(g), np.mean(r)]
    
    #print("Average Calcium RGB Values:", avg_calc_col)
    
    return avg_calc_col


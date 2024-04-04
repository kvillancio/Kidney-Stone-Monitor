from PIL import Image
import numpy as np
from scipy.ndimage import gaussian_filter, binary_fill_holes
from skimage.feature import canny
from skimage.morphology import remove_small_objects
import matplotlib.pyplot as plt


def preprocess_image(image):
    grayscale_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    blurred_image = gaussian_blur(grayscale_image, (13, 13), 0)
    return blurred_image

def gaussian_blur(image, kernel_size, sigma):
    return gaussian_filter(image, sigma=sigma, mode='constant')

# segment the calibration squares wth canny edge detection, filling, and then removing noise
def segment(image):
    edges = canny_edge_detection(image, 1, 16)
    filled_image = binary_fill_holes(edges)
    cleaned_image = morphology_cleanup(filled_image, min_area=30)
    return cleaned_image

def canny_edge_detection(image, low_threshold, high_threshold):
    return canny(image, sigma=1, low_threshold=low_threshold, high_threshold=high_threshold)

def morphology_cleanup(image, min_area):
    cleaned_image = remove_small_objects(image, min_size=min_area, connectivity=1)
    return cleaned_image.astype(np.uint8)

# find the first corners of either the top ca or ph calibration square
def find_first_square_corner(height, width, segmented_image, square_type):
    if square_type == 'ph':
        start = width - 1
        stop = -1
        index = -1
    else:
        start = 1
        stop = width -1
        index = 1
    row_sums = np.sum(segmented_image, axis=1)  
    for row in range(height - 1):
        # check if the current row has at least 30 white pixels to avoid using a noisy row
        if row_sums[row] >= 30:
            for col in range(start, stop, index):
                if segmented_image[row, col] == 1:
                    squareTop_row = row
                    squareTop_col = col
                    return squareTop_row, squareTop_col
    return None 

# find the first center kernel using the row and column found from find_first_square_corner and 
# append that kernel to the corresponding ph or ca kernel list
def find_first_center_kernel(first_row, first_col, kernel_list, segmented_image, square_type):
    col2 = first_col
    if square_type == 'ph':
        while segmented_image[first_row, col2] != 0:
            col2 -= 1
    else:
        while segmented_image[first_row, col2] != 0:
            col2 += 1
    bottom_row = first_row
    while segmented_image[bottom_row, first_col] != 0:
        bottom_row += 1
    center_row = round((bottom_row + first_row)/2)
    center_col = round((col2 + first_col)/2)
    # create a 5x5 kernel centered around center_row, center_col
    kernel_list.append([center_row - 2, center_row + 3, center_col - 2, center_col + 3])
    return bottom_row, center_col

# after finding the first square kernel this function finds the rest of the kernels by going down
# the center col and adjust the center coordinates while going down; 
# those kernels are appended to the corresponding ph or ca kernel list
def find_rest_of_calibration_kernels(bottom_row, center_col, height, kernel_list, squares, segmented_image):
    bottom_row += 3
    right_col = left_col = center_col
    while bottom_row < (height - 1) and len(kernel_list) < squares:
        while segmented_image[bottom_row, center_col] != 1 and bottom_row < height - 1:
            bottom_row += 1   
        top_row = bottom_row
        while segmented_image[bottom_row, center_col] != 0:
            bottom_row += 1
        center_row = round((top_row + bottom_row) / 2)
        while segmented_image[center_row, right_col] != 0:
            right_col += 1
        while segmented_image[center_row, left_col] != 0:
            left_col -= 1
        center_col = round((left_col + right_col) / 2)
        kernel_list.append([center_row - 2, center_row + 3, center_col - 2, center_col + 3])  
    return 

# can be used to visualize kernels on the segmented image so you can see where the average rgb 
# value is going to be calculated from
def visualize_kernels(segmented_image, kernel_list):
    plt.imshow(segmented_image, cmap='gray')
    for kernel in kernel_list:
        min_row, max_row, min_col, max_col = kernel
        for row_offset in range(min_row, max_row): 
            for col_offset in range(min_col, max_col):  
                plt.scatter(col_offset, row_offset, color='red', marker='s', s=1)  
    plt.xlabel('Column')
    plt.ylabel('Row')
    plt.title('Kernels On the Segmented Image')
    plt.show()

def get_average_rgb_from_kernels(kernel_list, original_image):
    average_rgb_values = []
    for kernel in kernel_list:
        region = original_image[kernel[0]:kernel[1], kernel[2]:kernel[3]]
        average_rgb = np.mean(region, axis=(0, 1))  
        average_rgb_values.append([average_rgb[0], average_rgb[1], average_rgb[2]])
    return average_rgb_values

def get_ph_and_ca_calibration_values(filename):
    image_array = np.array(Image.open(filename))
    processed_image = preprocess_image(image_array)
    segmented_image = segment(processed_image)
    plt.imshow(segmented_image, cmap='gray')
    plt.title('Segmented Image')
    plt.show()
    print()
    height, width = segmented_image.shape[:2]
    ph_kernels = []
    ca_kernels = []
    all_kernels = []

    first_row_ph, first_col_ph = find_first_square_corner(height, width, segmented_image, 'ph')
    first_row_ca, first_col_ca = find_first_square_corner(height, width, segmented_image, 'ca')

    bottom_row_ph, center_col_ph = find_first_center_kernel(first_row_ph, first_col_ph, ph_kernels, segmented_image, 'ph')
    bottom_row_ca, center_col_ca = find_first_center_kernel(first_row_ca, first_col_ca, ca_kernels, segmented_image, 'ca')

    find_rest_of_calibration_kernels(bottom_row_ph, center_col_ph, height, ph_kernels, 7, segmented_image) # should be 7 kernels
    find_rest_of_calibration_kernels(bottom_row_ca, center_col_ca, height, ca_kernels, 5, segmented_image) # should be 5 kernels

    all_kernels = ph_kernels + ca_kernels
    visualize_kernels(segmented_image, all_kernels)

    ph_calibration_rgb_values = get_average_rgb_from_kernels(ph_kernels, image_array)
    ca_calibration_rgb_values = get_average_rgb_from_kernels(ca_kernels, image_array)

    return ph_calibration_rgb_values, ca_calibration_rgb_values
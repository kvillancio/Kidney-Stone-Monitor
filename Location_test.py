from PIL import Image

def calc_color(rgb_vals):
    red = rgb_vals[0]
    green = rgb_vals[1]
    blue = rgb_vals[2]
    # Convert the RGB values to a hex color code
    hex_color = "#{:02X}{:02X}{:02X}".format(red, green, blue)
    return hex_color

# Location function for calibration chart
def locate_pH(filename):
    # Open image
    image = Image.open(filename)
    # Initialize rgb for pH
    rgb1 = []
    # Initialize starting position
    x1 = image.width
    y1 = image.height

    # Iterate over every pixel from right to left until the color is not white
    # Return horizontal position of the first column
    for y in range(y1 - 1):
        for x in range(x1 - 1, 0, -1):
            # Get the pixel color at the current position
            pixel_color = image.getpixel((x, y))
            print(pixel_color[1])
            if  (pixel_color[0]!=pixel_color[1]+6 | pixel_color[0]!=pixel_color[1]-6) & (pixel_color[2]!=pixel_color[1]+6 | pixel_color[2]!=pixel_color[1]-6)  & (pixel_color[0]!=pixel_color[2]+6 | pixel_color[2]!=pixel_color[0]-6): 
                x1 = x-20  # Save the x position for pH and shift more towards center of the block
                y1 = y+15 #shift towards center of the clock
                break
        if (pixel_color[0]!=pixel_color[1]+6 | pixel_color[0]!=pixel_color[1]-6) & (pixel_color[2]!=pixel_color[1]+6 | pixel_color[2]!=pixel_color[1]-6)  & (pixel_color[0]!=pixel_color[2]+6 | pixel_color[2]!=pixel_color[0]-6):
            break

    # Iterate vertically through found column and store RGB values for each block
    for block in range(7):
        rgb_temp = []
        found_white_pixel = False  # Flag to detect white pixels
        for y in range(y1, image.height):
            # Get the pixel color at the current position
            pixel_color = image.getpixel((x1, y))
            if found_white_pixel and  (pixel_color[0]==pixel_color[1]+6 | pixel_color[0]==pixel_color[1]-6) & (pixel_color[2]==pixel_color[1]+6 | pixel_color[2]==pixel_color[1]-6)  & (pixel_color[0]==pixel_color[2]+6 | pixel_color[2]==pixel_color[0]-6):
                y1 = y+15  # Update y1 when a white pixel is encountered shift it more to the center of the block
                break
            if (pixel_color[0]!=pixel_color[1]+6 | pixel_color[0]!=pixel_color[1]-6) & (pixel_color[2]!=pixel_color[1]+6 | pixel_color[2]!=pixel_color[1]-6)  & (pixel_color[0]!=pixel_color[2]+6 | pixel_color[2]!=pixel_color[0]-6):
                pixel_color = image.getpixel((x1, y))
                rgb_temp.append(pixel_color)
                found_white_pixel = True

        if rgb_temp:
            # Compute average color for a column in one block
            red = [temp[0] for temp in rgb_temp]
            green = [temp[1] for temp in rgb_temp]
            blue = [temp[2] for temp in rgb_temp]
            # Calculate averages for RGB separately
            rgb1.append([sum(red) // len(red), sum(green) // len(green), sum(blue) // len(blue), 255])

    return rgb1

# Location function for calibration chart
def locate_Ca(filename):
    # Open image
    image = Image.open(filename)
    # Initialize rgb for pH
    rgb1 = []
    # Initialize starting position
    x1 = image.width
    y1 = image.height

    # Iterate over every pixel from left to right until the color is not white
    # Return horizontal position of the first column
    for y in range(y1 - 1):
        for x in range(0,x1 - 1):
            # Get the pixel color at the current position
            pixel_color = image.getpixel((x, y))
            if (pixel_color[0]==pixel_color[1]+6 | pixel_color[0]==pixel_color[1]-6) & (pixel_color[2]==pixel_color[1]+6 | pixel_color[2]==pixel_color[1]-6)  & (pixel_color[0]==pixel_color[2]+6 | pixel_color[2]==pixel_color[0]-6): 
                x1 = x+20  # Save the x position for pH and shift more towards center of the block
                y1 = y+15 #shift towards center of the clock
                break
        if pixel_color != (255, 255, 255, 255):
            break

    # Iterate vertically through found column and store RGB values for each block
    for block in range(5):
        rgb_temp = []
        found_white_pixel = False  # Flag to detect white pixels
        for y in range(y1, image.height):
            # Get the pixel color at the current position
            pixel_color = image.getpixel((x1, y))
            if found_white_pixel and pixel_color == (255, 255, 255, 255):
                y1 = y+15  # Update y1 when a white pixel is encountered shift it more to the center of the block
                break
            if pixel_color != (255, 255, 255, 255):
                pixel_color = image.getpixel((x1, y))
                rgb_temp.append(pixel_color)
                found_white_pixel = True

        if rgb_temp:
            # Compute average color for a column in one block
            red = [temp[0] for temp in rgb_temp]
            green = [temp[1] for temp in rgb_temp]
            blue = [temp[2] for temp in rgb_temp]
            # Calculate averages for RGB separately
            rgb1.append([sum(red) // len(red), sum(green) // len(green), sum(blue) // len(blue), 255])

    return rgb1

# Location function for calibration chart
def locate_strip_Ca(filename):
    # Open image
    image = Image.open(filename)
    # Initialize rgb for pH
    rgb1 = []
    # Initialize starting position
    x1 = image.width
    y1 = image.height

    # Iterate over every pixel from left to right until the color is not white
    # Return horizontal position of the first column
    for y in range(y1 - 1):
        for x in range(0,(x1)//2):
            # Get the pixel color at the current position
            pixel_color = image.getpixel((x, y))
            if (pixel_color[0]==pixel_color[1]+6 | pixel_color[0]==pixel_color[1]-6) & (pixel_color[2]==pixel_color[1]+6 | pixel_color[2]==pixel_color[1]-6)  & (pixel_color[0]==pixel_color[2]+6 | pixel_color[2]==pixel_color[0]-6): 
                x1 = x+20  # Save the x position for pH and shift more towards center of the block
                y1 = y+15 #shift towards center of the clock
                break
        if pixel_color != (255, 255, 255, 255):
            break

    # Iterate vertically through found column and store RGB values for each block
    for block in range(5):
        rgb_temp = []
        found_white_pixel = False  # Flag to detect white pixels
        for y in range(y1, image.height):
            # Get the pixel color at the current position
            pixel_color = image.getpixel((x1, y))
            if found_white_pixel and pixel_color == (255, 255, 255, 255):
                y1 = y+15  # Update y1 when a white pixel is encountered shift it more to the center of the block
                break
            if pixel_color != (255, 255, 255, 255):
                pixel_color = image.getpixel((x1, y))
                rgb_temp.append(pixel_color)
                found_white_pixel = True

        if rgb_temp:
            # Compute average color for a column in one block
            red = [temp[0] for temp in rgb_temp]
            green = [temp[1] for temp in rgb_temp]
            blue = [temp[2] for temp in rgb_temp]
            # Calculate averages for RGB separately
            rgb1.append([sum(red) // len(red), sum(green) // len(green), sum(blue) // len(blue), 255])

    return rgb1

if __name__ == "__main__":
    filename = input('Filename: ')
    rgb_pH = locate_pH(filename)
    rgb_Ca=locate_Ca(filename)
    sample_Ca=locate_strip_Ca(filename)
    print(rgb_pH)
    print()
    print(rgb_Ca)
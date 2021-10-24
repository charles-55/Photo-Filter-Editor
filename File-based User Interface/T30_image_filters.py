# Imports
from Cimpl import Color,copy,create_color,get_color,get_height,get_width,Image,load_image,set_color

# Functions
# Jake Bissonnette 101148821
def red_channel(img:Image) -> Image:
    """Returns a red filtered image of an original image.
    """
    
    new_image = copy(img)
    for pixel in img:
        x, y, (r, g, b) = pixel
        new_color = create_color(r, 0, 0)
        set_color(new_image, x, y, new_color)
    return new_image

# Alamin Ahmed, 101140975
def green_channel(img:Image)-> Image:
    """Returns a green filtered image of an original image.
    """
    
    new_image = copy(img)
    for pixel in img:
        x, y, (r, g, b) = pixel
        new_colour = create_color(0,g,0) # Mix up the colours ad hoc
        set_color (new_image, x, y, new_colour)
    return new_image

#Dhruv Sannd, 101156588
def blue_channel(img:Image)-> Image:
    """Returns a blue filtered image of an original image.
    """
    
    new_image = copy(img)
    for pixel in img:
        x, y, (r, g, b) = pixel
        new_colour = create_color(0,0,b) # Mix up the colours ad hoc
        set_color (new_image, x, y, new_colour)
    return new_image

# Nwoko Osamudiamen, 101152520
def combine(red_image:Image,green_image:Image,blue_image:Image)-> Image:
    """Returns a combined color image of a red, green and blue filtered image in that order.
    """
    
    combined = copy(red_image)
    
    for pixel in red_image:
        x,y, (r,g,b) = pixel
        c = get_color(red_image,x,y)
        r1 = c[0]
        c = get_color(green_image,x,y)
        g1 = c[1]
        c = get_color(blue_image,x,y)
        b1 = c[2]
        new_colour = create_color(r1,g1,b1)
        set_color (combined, x, y, new_colour)
    
    return combined

# Nwoko Osamudiamen, 101152520
def two_tone(img:Image, color1:str, color2:str) -> Image:
    """Returns a woodcut print imsge with any two colours
    """
    
    if color1 == "black":
        new_color1 = create_color(0, 0, 0)
    if color1 == "white":
        new_color1 = create_color(255, 255, 255)
    if color1 == "red":
        new_color1 = create_color(255, 0, 0)
    if color1 == "lime":
        new_color1 = create_color(0, 255, 0)
    if color1 == "blue":
        new_color1 = create_color(0, 0, 255)
    if color1 == "yellow":
        new_color1 = create_color(255, 255, 0)
    if color1 == "cyan":
        new_color1 = create_color(0, 255, 255)
    if color1 == "magenta":
        new_color1 = create_color(255, 0, 255)
    if color1 == "gray":
        new_color1 = create_color(128, 128, 128)
        
    if color2 == "black":
        new_color2 = create_color(0, 0, 0)
    if color2 == "white":
        new_color2 = create_color(255, 255, 255)
    if color2 == "red":
        new_color2 = create_color(255, 0, 0)
    if color2 == "lime":
        new_color2 = create_color(0, 255, 0)
    if color2 == "blue":
        new_color2 = create_color(0, 0, 255)
    if color2 == "yellow":
        new_color2 = create_color(255, 255, 0)
    if color2 == "cyan":
        new_color2 = create_color(0, 255, 255)
    if color2 == "magenta":
        new_color2 = create_color(255, 0, 255)
    if color2 == "gray":
        new_color2 = create_color(128, 128, 128)
    
    for pixel in img:
        x,y, (r,g,b) = pixel
        brightness = (r + g + b) / 3
        if 0 <= brightness <= 127:
            set_color (img, x, y, new_color1)
        if 128 <= brightness <= 255:
            set_color (img, x, y, new_color2)
    return img

# Nwoko Osamudiamen, 101152520
def three_tone(new_image:Image, color1:str, color2:str, color3:str) -> Image:
    """Returns a woodcut print imsge with any three colours
    """
    
    if color1 == "black":
        new_color1 = create_color(0, 0, 0)
    if color1 == "white":
        new_color1 = create_color(255, 255, 255)
    if color1 == "red":
        new_color1 = create_color(255, 0, 0)
    if color1 == "lime":
        new_color1 = create_color(0, 255, 0)
    if color1 == "blue":
        new_color1 = create_color(0, 0, 255)
    if color1 == "yellow":
        new_color1 = create_color(255, 255, 0)
    if color1 == "cyan":
        new_color1 = create_color(0, 255, 255)
    if color1 == "magenta":
        new_color1 = create_color(255, 0, 255)
    if color1 == "gray":
        new_color1 = create_color(128, 128, 128)
        
    if color2 == "black":
        new_color2 = create_color(0, 0, 0)
    if color2 == "white":
        new_color2 = create_color(255, 255, 255)
    if color2 == "red":
        new_color2 = create_color(255, 0, 0)
    if color2 == "lime":
        new_color2 = create_color(0, 255, 0)
    if color2 == "blue":
        new_color2 = create_color(0, 0, 255)
    if color2 == "yellow":
        new_color2 = create_color(255, 255, 0)
    if color2 == "cyan":
        new_color2 = create_color(0, 255, 255)
    if color2 == "magenta":
        new_color2 = create_color(255, 0, 255)
    if color2 == "gray":
        new_color2 = create_color(128, 128, 128)
        
    if color3 == "black":
        new_color3 = create_color(0, 0, 0)
    if color3 == "white":
        new_color3 = create_color(255, 255, 255)
    if color3 == "red":
        new_color3 = create_color(255, 0, 0)
    if color3 == "lime":
        new_color3 = create_color(0, 255, 0)
    if color3 == "blue":
        new_color3 = create_color(0, 0, 255)
    if color3 == "yellow":
        new_color3 = create_color(255, 255, 0)
    if color3 == "cyan":
        new_color3 = create_color(0, 255, 255)
    if color3 == "magenta":
        new_color3 = create_color(255, 0, 255)
    if color3 == "gray":
        new_color3 = create_color(128, 128, 128)
    
    for pixel in new_image:
        x,y, (r,g,b) = pixel
        brightness = (r + g + b) / 3
        if 0 <= brightness <= 84:
            set_color (new_image, x, y, new_color1)
        if 85 <= brightness <= 170:
            set_color (new_image, x, y, new_color2)
        if 171 <= brightness <= 255:
            set_color (new_image, x, y, new_color3)
    return new_image

# Alamin Ahmed, 101140975
def extreme_contrast(original_image)-> Image:
    """Returns a copy of an image in which the contrast between the pixels has been taken to its extreme values, either maximum or minimum."""
    
    new_image = copy(original_image)    
    for x,y,(r,g,b) in original_image:
        if r>= 0 and r<=127:
            r1=0
        if r>=128:
            r1=255
        if g>=0 and g<=127:
            g1=0
        if g>=128:
            g1=255
        if b>=0 and b<=127:
            b1=0
        if b>=128:
            b1=255
        color=create_color(r1,g1,b1)
        set_color(new_image,x,y,color)
    return new_image

# Jake Bissonnette, 101148821
def sepia(image: Image) -> Image:
    """ Returns a copy of an image in which all the pixels have been sepia-tinted
    show(sepia("p2-original.jpg")) 
    Image Shown
    """
    
    sepia_image = copy(image)
    for x, y, (r, g, b) in image:
        brightness = (r + g + b) // 3
        new_color = create_color(brightness, brightness, brightness)
        set_color(sepia_image, x, y, new_color)   

    for x, y, (r, g, b) in sepia_image:
        if g <63:
            b = 0.9 * b
            r = 1.1 * r
        elif 63 <= g <= 191:
            b = 0.85 * b
            r = 1.15 * r
        elif g > 191:
            b = 0.93 * b
            r = 1.08 * r
        set_color(sepia_image, x, y, Color(r, g, b))
        
    return sepia_image

# Dhruv Sannd, 101156588
def _adjust_component(new_image):
    """Returns a smaller number of colours than the original image. Adjust component determines which quadrant a component lies in and returns the midpoint of that quadrant.
    """
    
    for pixel in new_image:
        x, y, (r, g, b) = pixel 
        
        if r in range (0, 64):
            r = 31
        elif r in range (64, 128):
            r = 95
        elif r in range (128, 192):
            r = 159
        elif r in range (192, 256):
            r = 223
        
        if g in range (0, 64):
            g = 31
        elif g in range (64, 128):
            g = 95
        elif g in range (128, 192):
            g = 159
        elif g in range (192, 256):
            g = 223
        
        if b in range (0, 64):
            b = 31
        elif b in range (64, 128):
            b = 95
        elif b in range (128, 192):
            b = 159
        elif b in range (192, 256):
            b = 223
            
        new_color = create_color(r, g, b)
        set_color (new_image, x, y, new_color)
    
    return new_image


def posterize (img: Image) -> Image:
    """
    Returns a posterized copy of an image.
    """

    posterize_image = _adjust_component(img)

    return posterize_image

# Nwoko Osamudiamen, 101152520

def detect_edges(img: Image, threshold_value: int) -> Image:
    """
    """
    img_height = get_height(img)
    
    for pixel in img:
        x, y, (r, g, b) = pixel
        if y != (img_height-1):
            pixel_above_brightness = (r+g+b)/3
            (r1,g1,b1) = get_color(img,x,y+1)
            pixel_below_brightness = (r1+g1+b1)/3
            contrast = abs(pixel_above_brightness - pixel_below_brightness)
            if contrast <= threshold_value:
                set_color(img,x,y,create_color(255,255,255))
            elif contrast > threshold_value:
                set_color(img,x,y,create_color(0,0,0))
        elif y == (img_height-1):
            set_color(img,x,y,create_color(255,255,255))
    return img

# Alamin Ahmed, 101140975
def brightness_calcution(col: tuple) -> int:
    '''
    Returns the brightness of the pixels using the values of RGB
    '''        
    r, g, b = col
   
    brightness = (r + g + b) // 3
       
    return brightness

def detect_edges_better(image1: Image, threshold: int) -> Image:
    '''
    Returns an image in which the pixel's colour turns black if the relationship between the contrast 
    of the pixel under or to the right is higher than the threshold set by the user. 
    Otherwise the pixel's colour is changed to white.
    ''' 
    image2 = copy(image1)
   
    for x in range(get_width(image2) - 1):
        for y in range(get_height(image2) - 1):
       
            pixel_upper = brightness_calcution(get_color(image2, x, y))
            pixel_under = brightness_calcution(get_color(image2, x, y + 1))
            pixel_right = brightness_calcution(get_color(image2, x + 1, y))
           
            if (abs(pixel_upper - pixel_under) > threshold or abs(pixel_upper - pixel_right) > threshold):
                new_color = create_color(0, 0, 0)
                set_color(image2, x, y, new_color)                
            else:
                new_color = create_color(255, 255, 255)
                set_color(image2, x, y, new_color)
            
    for pixel in image2:
        x,y,(r,g,b) = pixel
        last_x = get_width(image2)-1
        last_y = get_height(image2)-1
        
        if (x == last_x) or (y == last_y):
            new_color = create_color(255, 255, 255)
            set_color(image2, x, y, new_color)            
    return image2

#Jake Bissonnette, 101148821
def flip_vertical(img: str)-> Image:
    """ Returns a vertically flipped copy of the image passed into the filter.
    >>> image = load_image(choose_file())
        v_flip = flip_vertical(image)
        show(v_flip) 
    """
    new_img = copy(img)
    w = get_width(img)
    h = get_height(img)
    mid_point = w // 2
    
    for y in range(h):
        for x in range(mid_point):
            r1, g1, b1 = get_color(img, x, y)
            r2, g2, b2 = get_color(img, (-(x + 1)), y)
            
            set_color(new_img, x, y, Color(r2, g2, b2))
            set_color(new_img, (-(x + 1)), y, Color(r1, g1, b1))
  
    return new_img

#Dhruv Sannd, 101156588
from Cimpl import *

def flip_horizontal(img: Image)-> Image:
    new_img = copy(img)
    w = get_width(img)
    h = get_height(img)
        
    for x in range(w):
        for y in range(h):
            r1, g1, b1 = get_color(img, x, y)
            r2, g2, b2 = get_color(img, x, (-(y + 1)))
                
            set_color(new_img, x, y, Color(r2, g2, b2))
            set_color(new_img, x, (-(y + 1)), Color(r1, g1, b1))
      
    return new_img
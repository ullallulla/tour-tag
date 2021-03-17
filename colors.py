#import unicornhathd
#import time, colorsys
#import numpy
from .ports import unicornGrid

def set_origin_port_color():
    o_color = numpy.array(unicornGrid)
    for x in range(16):
        for y in range(16):
            h = 0.8  # red
            s = 0.16  # saturation at the top of the red scale
            v = 0.15      # brightness depends on range
            r, g, b = colorsys.hsv_to_rgb(h, s, v)  # convert hsv back to RGB
            red = int(r * 255.0)                    # makes 0-1 range > 0-255 range
            green = int(g * 255.0)
            blue = int(b * 255.0)
            unicornhathd.set_pixel(x, y, red, green, blue)  # sets pixels on the hat
        unicornhathd.show()                             # show the pixels
        time.sleep(0.005)                               # tiny gap, sets frames to a smooth 200/sec
    time.sleep(0.8) 
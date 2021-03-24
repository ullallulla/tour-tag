#import unicornhathd
#import time, colorsys
#import numpy
from .colors import *



unicornGrid = [[0]*16 for i in range(16)]

ahvenanmaa = {
    "name": "Ahvenanmaa",
    "y1": 14,
    "y2": 15,
    "x1": 0,
    "x2": 1
}
turku = {
    "name": "Turku",
    "y1": 14,
    "y2": 15,
    "x1": 6,
    "x2": 7
}
helsinki = {
    "name": "Helsinki",
    "y1": 14,
    "y2": 15,
    "x1": 10,
    "x2": 11
}
hamina = {
    "name": "Hamina",
    "y1": 14,
    "y2": 15,
    "x1": 14,
    "x2": 15
}
pori = {
    "name": "Pori",
    "y1": 10,
    "y2": 11,
    "x1": 6,
    "x2": 7
}
vaasa = {
    "name": "Vaasa",
    "y1": 6,
    "y2": 7,
    "x1": 6,
    "x2": 7
}
kokkola = {
    "name": "Kokkola",
    "y1": 3,
    "y2": 4,
    "x1": 10,
    "x2": 11
}
oulu = {
    "name": "Oulu",
    "y1": 0,
    "y2": 1,
    "x1": 14,
    "x2": 15
}

def toggle_origin_port(port):
    if port == ahvenanmaa['name']:
        unicornGrid[ahvenanmaa['y1']][ahvenanmaa['x1']] = 1
        unicornGrid[ahvenanmaa['y1']][ahvenanmaa['x2']] = 1
        unicornGrid[ahvenanmaa['y2']][ahvenanmaa['x1']] = 1
        unicornGrid[ahvenanmaa['y2']][ahvenanmaa['x2']] = 1
    if port == turku['name']:
        unicornGrid[turku['y1']][turku['x1']] = 1
        unicornGrid[turku['y1']][turku['x2']] = 1
        unicornGrid[turku['y2']][turku['x1']] = 1
        unicornGrid[turku['y2']][turku['x2']] = 1
    if port == helsinki['name']:
        unicornGrid[helsinki['y1']][helsinki['x1']] = 1
        unicornGrid[helsinki['y1']][helsinki['x2']] = 1
        unicornGrid[helsinki['y2']][helsinki['x1']] = 1
        unicornGrid[helsinki['y2']][helsinki['x2']] = 1
    if port == hamina['name']:
        unicornGrid[hamina['y1']][hamina['x1']] = 1
        unicornGrid[hamina['y1']][hamina['x2']] = 1
        unicornGrid[hamina['y2']][hamina['x1']] = 1
        unicornGrid[hamina['y2']][hamina['x2']] = 1
    if port == pori['name']:
        unicornGrid[pori['y1']][pori['x1']] = 1
        unicornGrid[pori['y1']][pori['x2']] = 1
        unicornGrid[pori['y2']][pori['x1']] = 1
        unicornGrid[pori['y2']][pori['x2']] = 1
    if port == vaasa['name']:
        unicornGrid[vaasa['y1']][vaasa['x1']] = 1
        unicornGrid[vaasa['y1']][vaasa['x2']] = 1
        unicornGrid[vaasa['y2']][vaasa['x1']] = 1
        unicornGrid[vaasa['y2']][vaasa['x2']] = 1
    if port == kokkola['name']:
        unicornGrid[kokkola['y1']][kokkola['x1']] = 1
        unicornGrid[kokkola['y1']][kokkola['x2']] = 1
        unicornGrid[kokkola['y2']][kokkola['x1']] = 1
        unicornGrid[kokkola['y2']][kokkola['x2']] = 1
    if port == oulu['name']:
        unicornGrid[oulu['y1']][oulu['x1']] = 1
        unicornGrid[oulu['y1']][oulu['x2']] = 1
        unicornGrid[oulu['y2']][oulu['x1']] = 1
        unicornGrid[oulu['y2']][oulu['x2']] = 1


def toggle_destination_port(port):
    if port == ahvenanmaa['name']:
        unicornGrid[ahvenanmaa['y1']][ahvenanmaa['x1']] = 1
        unicornGrid[ahvenanmaa['y1']][ahvenanmaa['x2']] = 1
        unicornGrid[ahvenanmaa['y2']][ahvenanmaa['x1']] = 1
        unicornGrid[ahvenanmaa['y2']][ahvenanmaa['x2']] = 1
    if port == turku['name']:
        unicornGrid[turku['y1']][turku['x1']] = 1
        unicornGrid[turku['y1']][turku['x2']] = 1
        unicornGrid[turku['y2']][turku['x1']] = 1
        unicornGrid[turku['y2']][turku['x2']] = 1
    if port == helsinki['name']:
        unicornGrid[helsinki['y1']][helsinki['x1']] = 1
        unicornGrid[helsinki['y1']][helsinki['x2']] = 1
        unicornGrid[helsinki['y2']][helsinki['x1']] = 1
        unicornGrid[helsinki['y2']][helsinki['x2']] = 1
    if port == hamina['name']:
        unicornGrid[hamina['y1']][hamina['x1']] = 1
        unicornGrid[hamina['y1']][hamina['x2']] = 1
        unicornGrid[hamina['y2']][hamina['x1']] = 1
        unicornGrid[hamina['y2']][hamina['x2']] = 1
    if port == pori['name']:
        unicornGrid[pori['y1']][pori['x1']] = 1
        unicornGrid[pori['y1']][pori['x2']] = 1
        unicornGrid[pori['y2']][pori['x1']] = 1
        unicornGrid[pori['y2']][pori['x2']] = 1
    if port == vaasa['name']:
        unicornGrid[vaasa['y1']][vaasa['x1']] = 1
        unicornGrid[vaasa['y1']][vaasa['x2']] = 1
        unicornGrid[vaasa['y2']][vaasa['x1']] = 1
        unicornGrid[vaasa['y2']][vaasa['x2']] = 1
    if port == kokkola['name']:
        unicornGrid[kokkola['y1']][kokkola['x1']] = 1
        unicornGrid[kokkola['y1']][kokkola['x2']] = 1
        unicornGrid[kokkola['y2']][kokkola['x1']] = 1
        unicornGrid[kokkola['y2']][kokkola['x2']] = 1
    if port == oulu['name']:
        unicornGrid[oulu['y1']][oulu['x1']] = 1
        unicornGrid[oulu['y1']][oulu['x2']] = 1
        unicornGrid[oulu['y2']][oulu['x1']] = 1
        unicornGrid[oulu['y2']][oulu['x2']] = 1
    
    print(unicornGrid)

    """ testi = numpy.array(unicornGrid)
    for x in range(16):
        for y in range(16):
            h = 0.0  # red
            s = 1.0  # saturation at the top of the red scale
            v = testi[x, y]      # brightness depends on range
            r, g, b = colorsys.hsv_to_rgb(h, s, v)  # convert hsv back to RGB
            red = int(r * 255.0)                    # makes 0-1 range > 0-255 range
            green = int(g * 255.0)
            blue = int(b * 255.0)
            unicornhathd.set_pixel(x, y, red, green, blue)  # sets pixels on the hat
        unicornhathd.show()                             # show the pixels
        time.sleep(0.005)                               # tiny gap, sets frames to a smooth 200/sec
    time.sleep(0.8)  """ 

def clear_ports():
    for i in range(16):
        for j in range(16):
            unicornGrid[i][j] = 0
    #unicornhathd.off()
    return 
    

def set_next_port():
    'asd'


def set_arrived(next_port, destination_ports):
    destination_ports.remove(next_port)
    if len(destination_ports) == 0:
        set_final_destination_color(next_port)
    else:
        set_current_port_color(next_port)
    print(destination_ports)



def set_departed(next_port, current_port, origin_port):
    if origin_port != current_port:
        clear_port_color(current_port)
    set_next_port_color(next_port)
    

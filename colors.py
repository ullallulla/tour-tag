#import unicornhathd
#import time, colorsys
#import numpy
from .ports import *
from .main import *


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

def set_origin_port_color(port):
    if port == ahvenanmaa['name']:
        r = 0
        g = 255
        b = 0
        unicornhathd.set_pixel(ahvenanmaa['y1'],ahvenanmaa['x1'], r, g, b)
        unicornhathd.set_pixel(ahvenanmaa['y1'],ahvenanmaa['x2'], r, g, b)
        unicornhathd.set_pixel(ahvenanmaa['y2'],ahvenanmaa['x1'], r, g, b)
        unicornhathd.set_pixel(ahvenanmaa['y2'],ahvenanmaa['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == turku['name']:
        r = 0
        g = 255
        b = 0
        unicornhathd.set_pixel(turku['y1'],turku['x1'], r, g, b)
        unicornhathd.set_pixel(turku['y1'],turku['x2'], r, g, b)
        unicornhathd.set_pixel(turku['y2'],turku['x1'], r, g, b)
        unicornhathd.set_pixel(turku['y2'],turku['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == helsinki['name']:
        r = 255
        g = 0
        b = 0
        unicornhathd.set_pixel(helsinki['y1'],helsinki['x1'], r, g, b)
        unicornhathd.set_pixel(helsinki['y1'],helsinki['x2'], r, g, b)
        unicornhathd.set_pixel(helsinki['y2'],helsinki['x1'], r, g, b)
        unicornhathd.set_pixel(helsinki['y2'],helsinki['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == hamina['name']:
        r = 255
        g = 0
        b = 0
        unicornhathd.set_pixel(hamina['y1'],hamina['x1'], r, g, b)
        unicornhathd.set_pixel(hamina['y1'],hamina['x2'], r, g, b)
        unicornhathd.set_pixel(hamina['y2'],hamina['x1'], r, g, b)
        unicornhathd.set_pixel(hamina['y2'],hamina['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == pori['name']:
        r = 255
        g = 0
        b = 0
        unicornhathd.set_pixel(pori['y1'],pori['x1'], r, g, b)
        unicornhathd.set_pixel(pori['y1'],pori['x2'], r, g, b)
        unicornhathd.set_pixel(pori['y2'],pori['x1'], r, g, b)
        unicornhathd.set_pixel(pori['y2'],pori['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == vaasa['name']:
        r = 255
        g = 0
        b = 0
        unicornhathd.set_pixel(vaasa['y1'],vaasa['x1'], r, g, b)
        unicornhathd.set_pixel(vaasa['y1'],vaasa['x2'], r, g, b)
        unicornhathd.set_pixel(vaasa['y2'],vaasa['x1'], r, g, b)
        unicornhathd.set_pixel(vaasa['y2'],vaasa['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == kokkola['name']:
        r = 255
        g = 0
        b = 0
        unicornhathd.set_pixel(kokkola['y1'],kokkola['x1'], r, g, b)
        unicornhathd.set_pixel(kokkola['y1'],kokkola['x2'], r, g, b)
        unicornhathd.set_pixel(kokkola['y2'],kokkola['x1'], r, g, b)
        unicornhathd.set_pixel(kokkola['y2'],kokkola['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)        
    if port == oulu['name']:
        r = 255
        g = 0
        b = 0
        unicornhathd.set_pixel(oulu['y1'],oulu['x1'], r, g, b)
        unicornhathd.set_pixel(oulu['y1'],oulu['x2'], r, g, b)
        unicornhathd.set_pixel(oulu['y2'],oulu['x1'], r, g, b)
        unicornhathd.set_pixel(oulu['y2'],oulu['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)


#####################

def set_destination_port_color(port):
    if port == ahvenanmaa['name']:
        r = 0
        g = 255
        b = 0
        unicornhathd.set_pixel(ahvenanmaa['y1'],ahvenanmaa['x1'], r, g, b)
        unicornhathd.set_pixel(ahvenanmaa['y1'],ahvenanmaa['x2'], r, g, b)
        unicornhathd.set_pixel(ahvenanmaa['y2'],ahvenanmaa['x1'], r, g, b)
        unicornhathd.set_pixel(ahvenanmaa['y2'],ahvenanmaa['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == turku['name']:
        r = 0
        g = 255
        b = 0
        unicornhathd.set_pixel(turku['y1'],turku['x1'], r, g, b)
        unicornhathd.set_pixel(turku['y1'],turku['x2'], r, g, b)
        unicornhathd.set_pixel(turku['y2'],turku['x1'], r, g, b)
        unicornhathd.set_pixel(turku['y2'],turku['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == helsinki['name']:
        r = 0
        g = 255
        b = 0
        unicornhathd.set_pixel(helsinki['y1'],helsinki['x1'], r, g, b)
        unicornhathd.set_pixel(helsinki['y1'],helsinki['x2'], r, g, b)
        unicornhathd.set_pixel(helsinki['y2'],helsinki['x1'], r, g, b)
        unicornhathd.set_pixel(helsinki['y2'],helsinki['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == hamina['name']:
        r = 0
        g = 255
        b = 0
        unicornhathd.set_pixel(hamina['y1'],hamina['x1'], r, g, b)
        unicornhathd.set_pixel(hamina['y1'],hamina['x2'], r, g, b)
        unicornhathd.set_pixel(hamina['y2'],hamina['x1'], r, g, b)
        unicornhathd.set_pixel(hamina['y2'],hamina['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == pori['name']:
        r = 0
        g = 255
        b = 0
        unicornhathd.set_pixel(pori['y1'],pori['x1'], r, g, b)
        unicornhathd.set_pixel(pori['y1'],pori['x2'], r, g, b)
        unicornhathd.set_pixel(pori['y2'],pori['x1'], r, g, b)
        unicornhathd.set_pixel(pori['y2'],pori['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == vaasa['name']:
        r = 0
        g = 255
        b = 0
        unicornhathd.set_pixel(vaasa['y1'],vaasa['x1'], r, g, b)
        unicornhathd.set_pixel(vaasa['y1'],vaasa['x2'], r, g, b)
        unicornhathd.set_pixel(vaasa['y2'],vaasa['x1'], r, g, b)
        unicornhathd.set_pixel(vaasa['y2'],vaasa['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == kokkola['name']:
        r = 0
        g = 255
        b = 0
        unicornhathd.set_pixel(kokkola['y1'],kokkola['x1'], r, g, b)
        unicornhathd.set_pixel(kokkola['y1'],kokkola['x2'], r, g, b)
        unicornhathd.set_pixel(kokkola['y2'],kokkola['x1'], r, g, b)
        unicornhathd.set_pixel(kokkola['y2'],kokkola['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)        
    if port == oulu['name']:
        r = 0
        g = 255
        b = 0
        unicornhathd.set_pixel(oulu['y1'],oulu['x1'], r, g, b)
        unicornhathd.set_pixel(oulu['y1'],oulu['x2'], r, g, b)
        unicornhathd.set_pixel(oulu['y2'],oulu['x1'], r, g, b)
        unicornhathd.set_pixel(oulu['y2'],oulu['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)


################################################################


def set_next_port_color(port):
    if port == ahvenanmaa['name']:
        r = 0
        g = 0
        b =  255
        unicornhathd.set_pixel(ahvenanmaa['y1'],ahvenanmaa['x1'], r, g, b)
        unicornhathd.set_pixel(ahvenanmaa['y1'],ahvenanmaa['x2'], r, g, b)
        unicornhathd.set_pixel(ahvenanmaa['y2'],ahvenanmaa['x1'], r, g, b)
        unicornhathd.set_pixel(ahvenanmaa['y2'],ahvenanmaa['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == turku['name']:
        r = 0
        g = 0
        b =  255
        unicornhathd.set_pixel(turku['y1'],turku['x1'], r, g, b)
        unicornhathd.set_pixel(turku['y1'],turku['x2'], r, g, b)
        unicornhathd.set_pixel(turku['y2'],turku['x1'], r, g, b)
        unicornhathd.set_pixel(turku['y2'],turku['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == helsinki['name']:
        r = 0
        g = 0
        b =  255
        unicornhathd.set_pixel(helsinki['y1'],helsinki['x1'], r, g, b)
        unicornhathd.set_pixel(helsinki['y1'],helsinki['x2'], r, g, b)
        unicornhathd.set_pixel(helsinki['y2'],helsinki['x1'], r, g, b)
        unicornhathd.set_pixel(helsinki['y2'],helsinki['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == hamina['name']:
        r = 0
        g = 0
        b =  255
        unicornhathd.set_pixel(hamina['y1'],hamina['x1'], r, g, b)
        unicornhathd.set_pixel(hamina['y1'],hamina['x2'], r, g, b)
        unicornhathd.set_pixel(hamina['y2'],hamina['x1'], r, g, b)
        unicornhathd.set_pixel(hamina['y2'],hamina['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == pori['name']:
        r = 0
        g = 0
        b =  255
        unicornhathd.set_pixel(pori['y1'],pori['x1'], r, g, b)
        unicornhathd.set_pixel(pori['y1'],pori['x2'], r, g, b)
        unicornhathd.set_pixel(pori['y2'],pori['x1'], r, g, b)
        unicornhathd.set_pixel(pori['y2'],pori['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == vaasa['name']:
        r = 0
        g = 0
        b =  255
        unicornhathd.set_pixel(vaasa['y1'],vaasa['x1'], r, g, b)
        unicornhathd.set_pixel(vaasa['y1'],vaasa['x2'], r, g, b)
        unicornhathd.set_pixel(vaasa['y2'],vaasa['x1'], r, g, b)
        unicornhathd.set_pixel(vaasa['y2'],vaasa['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
    if port == kokkola['name']:
        r = 0
        g = 0
        b =  255
        unicornhathd.set_pixel(kokkola['y1'],kokkola['x1'], r, g, b)
        unicornhathd.set_pixel(kokkola['y1'],kokkola['x2'], r, g, b)
        unicornhathd.set_pixel(kokkola['y2'],kokkola['x1'], r, g, b)
        unicornhathd.set_pixel(kokkola['y2'],kokkola['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)        
    if port == oulu['name']:
        r = 0
        g = 0
        b =  255
        unicornhathd.set_pixel(oulu['y1'],oulu['x1'], r, g, b)
        unicornhathd.set_pixel(oulu['y1'],oulu['x2'], r, g, b)
        unicornhathd.set_pixel(oulu['y2'],oulu['x1'], r, g, b)
        unicornhathd.set_pixel(oulu['y2'],oulu['x2'], r, g, b)
        unicornhathd.show()
        time.sleep(0.005)
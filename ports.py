#import unicornhathd
#import time, colorsys
#import numpy
from .colors import set_next_port_color



unicornGrid = [[0]*16 for i in range(16)]



""" def toggle_origin_port(port):
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
        unicornGrid[oulu['y2']][oulu['x2']] = 1 """
    




def clear_ports():
    for i in range(16):
        for j in range(16):
            unicornGrid[i][j] = 0
    #unicornhathd.off()


def set_next_port():
    'asd'


def set_arrived(next_port, destination_ports):
    destination_ports.remove(next_port)



def set_departed(next_port, destination_ports):
    set_next_port_color(next_port)
    

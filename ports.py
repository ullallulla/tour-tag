#import unicornhathd
#import time, colorsys
from .colors import *





def clear_ports():
    #unicornhathd.off()
    return 
    



def set_arrived(next_port, destination_ports):
    destination_ports.remove(next_port)
    #if len(destination_ports) == 0:
        #set_final_destination_color(next_port)
    #else:
        #set_current_port_color(next_port)
    #print(destination_ports)



def set_departed(next_port, current_port, origin_port):
    if origin_port != current_port:
        clear_port_color(current_port)
    set_next_port_color(next_port)

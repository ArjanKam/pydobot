from serial.tools import list_ports
from pydobot import Dobot # https://github.com/luismesas/pydobot
from time import sleep


DOBOT_PORT = 3 # /dev/cu.SLAB_USBtoUART


def show_ports():
    for i, c in enumerate(list_ports.comports()):
        print(f"use : list_ports.comports()[ {i} ].device  --> {c.device}")


def check_current_pos():
    print("---- Current posotion ----")
    x, y, z, r, j1, j2, j3, j4 = device.pose()
    print(f"x={x:9.4f}, y={y:9.4f}, z={z:9.4f}, r={r:9.4f}")


def check_suckion():
    print("---- Suckion ON-OFF ----")
    for _ in range(3):
        device.suck(True )
        sleep(1)
        device.suck(False)
        sleep(1)


def check_grip():
    print("---- Grip ON-OFF ----")
    for _ in range(3):
        device.grip(True )
        sleep(1)
        device.grip(False)
        sleep(1)
        
        
def move_dobot():
    x, y, z, r, j1, j2, j3, j4 = device.pose()
    x += 40
    device.move_to(x, y, z, r, wait=True)  # we wait until this movement is done before continuing
    device.wait(1000)
    y += 40
    device.move_to(x, y, z, r, wait=True)  # we wait until this movement is done before continuing
    device.wait(1000)
    z += 20
    device.move_to(x, y, z, r, wait=True)  # we wait until this movement is done before continuing
    device.wait(1000)
    
    
def check_infrared():
    pass


def check_color():
    pass


def check_assembly_line():
    pass


portDoBot = list_ports.comports()[DOBOT_PORT].device
device    = Dobot(port=portDoBot)
device.suck(False)

show_ports()
check_current_pos()
check_suckion()
check_grip()
move_dobot()
check_infrared()
check_color()
check_assembly_line()
    
device.close()
from collections import namedtuple

class Volme():
    x = 0x01
    y = 0x02
    z = 0x03
    V = 0x00

def Call_x00_Named_tuple():
    namTup  = namedtuple('namTup', ['x', 'y', 'z', 'V'])
    axis    = namTup(x= 0x01, y= 0x02, z=0x03, V=0x00)

    Volme.V = Volme.x * Volme.y * Volme.z

    print(Volme.V)
    i   = -1
    print(hex(i))

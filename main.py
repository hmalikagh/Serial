# port
# baudrate
# bytesize
# timeout
# stopbits
import re

import serial
import keyboard

ser = serial.Serial(port="COM7", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
x, y, z = 0, 0, 0


def get_position(decoded,x,y,z):
    wyrazenie_regularne = r'est\[(.*?),(.*?),(.*?),(.*?)\]'
    wyniki = re.search(wyrazenie_regularne, decoded)
    if wyniki is not None:
        x = float(wyniki.group(1))
        y = float(wyniki.group(2))
        z = float(wyniki.group(3))
        return x,y,z
    else:
        return x,y,z


while True:
    receive = ser.readline()
    decoded = receive.decode('Ascii')

    if len(decoded) > 0:
        x, y, z = get_position(decoded,x,y,z)
    print(x, y, z)

    # decoded = '4016[0.00,0.00,0.00]=0.73 9929[0.00,1.00,0.00]=1.00 1C99[1.00,0.00,0.00]=1.15 D1B2[1.00,1.00,0.00]=1.15 le_us=2929 est[0.12,0.21,-0.67,51]'

ser.close()


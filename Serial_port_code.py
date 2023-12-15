#port
#baudrate
#bytesize
#timeout
#stopbits
import re

import serial
import keyboard

ser = serial.Serial(port="COM7",baudrate=115200, bytesize=8,timeout=2, stopbits=serial.STOPBITS_ONE)
x, y, z = 0, 0, 0
def get_position(decoded):
    if len(decoded)>0:
        position_str = decoded[(re.search(r'est', decoded).end()):]
        x = float(position_str[1:re.search(r',', position_str).start()])

        position_str = position_str[re.search(r',', position_str[1:]).end():]
        y = float(position_str[1:re.search(r',', position_str[1:]).end()])

        position_str = position_str[1:]
        position_str = position_str[re.search(r',', position_str).start():]
        position_str = position_str[1:]

        z = float(position_str[:re.search(r',', position_str).start()])
        return x,y,z
	
	#wyrazenie_regularne = r'est\[(.*?),(.*?),(.*?),(.*?)\]'
	#wyniki = re.search(wyrazenie_regularne, ciag_znakow)
	#x = float(wyniki.group(1))
   	#y = float(wyniki.group(2))

while True:
    receive = ser.readline()
    decoded = receive.decode('Ascii')

    if len(decoded)>0:
        x,y,z = get_position(decoded)
    print(x,y,z)


    #decoded = '4016[0.00,0.00,0.00]=0.73 9929[0.00,1.00,0.00]=1.00 1C99[1.00,0.00,0.00]=1.15 D1B2[1.00,1.00,0.00]=1.15 le_us=2929 est[0.12,0.21,-0.67,51]'
    #get_position(decoded)

    # if keyboard.is_pressed('q'):
    #     print("User need to to Quit the application")
    #     break

ser.close()


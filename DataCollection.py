#shoongi
#400312914

from cmath import cos,sin
from serial import Serial
import math

def getXY(dist):
    angleInc = 22.5
    xArray = []
    yArray = []
    for i in range (len(dist)):
        x = dist[i] * math.cos(math.radians(180-i*angleInc))
        y = dist[i] * math.sin(math.radians(180-i*angleInc))
        xArray.append(x)
        yArray.append(y)
    return xArray,yArray

userInput = "a"
while (userInput != "q"):
    s = Serial("COM3", 115200, timeout = 10)
    print("Opening: " + s.name)

    # reset the buffers of the UART port to delete the remaining data in the buffers
    s.reset_output_buffer()
    s.reset_input_buffer()

    measurements = []
    zMeasure = []
    # wait for user's signal to start the program
    input("Press Enter to start communication...")
    # send the character 's' to MCU via UART
    # This will signal MCU to start the transmission
    s.write('s'.encode())
    # recieve 10 measurements from UART of MCU

    for i in range(16):
        x = s.readline()
        reading = x.decode()
        reading = reading.strip()
        reading = reading.split(",")
        distRead = reading[0]
        zRead = int(reading[1]) * 300
        measurements.append(int(distRead))
        zMeasure.append(int(zRead))
       
    # the encode() and decode() function are needed to convert string to bytes
    # because pyserial library functions work with type "bytes"


    #close the port
    print("Closing: " + s.name)
    s.close()

    xMeasure,yMeasure = getXY(measurements)

    file = open("measurements.xyz", "a")
    for h in range (len(measurements)):
        dataString = str(zMeasure[h]) + " " + str(int(yMeasure[h])) + " " + str(int(xMeasure[h])) + "\n"
        file.write(dataString.format(x))
    file.close()

    userInput = input("Enter q to quit")
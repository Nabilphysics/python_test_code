import time
import serial
ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1)
time.sleep(0.1)
i = 0


while True:
    i = i + 1
    
    #send_data = str(i%2) + 'F100F112' 

    send_data = 'KF110S110S110S110G'
    #send_data = send_data + '\n' 
    ser.write(bytes(send_data, 'utf-8'))
    #ser.write(send_data.encode())
    
    packet = ser.readline()
    print(packet)
    
    time.sleep(0.001)
    
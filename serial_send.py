import time
import serial
ser = serial.Serial('/dev/ttyACM0', 115200, timeout= 1)
time.sleep(0.1)



while True:
    send_data = "F100F100" + '\n'
    ser.write(bytes(send_data, 'utf-8'))
    time.sleep(0.1)
    print(send_data)
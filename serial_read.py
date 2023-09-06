import time
import serial
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

right_encoder_rawValue_current = 0
count = 0
count_flag = False
counted_flag = False
#ser.open()

while True:
    if ser.in_waiting:
        packet = ser.readline()
        decoded_packet = packet.decode('utf').rstrip('\n')
        serial_split = decoded_packet.split(',')
        right_encoder_rawValue_current = float(serial_split[0])

        if(right_encoder_rawValue_current > 1000):
            #right_encoder_rawValue_current = 1000
            count_flag = True
        
        if((right_encoder_rawValue_current > 0) and (right_encoder_rawValue_current < 100)):
            count_flag = False
            counted_flag = False


        if(count_flag == True and counted_flag == False):
            count = count + 1
            counted_flag = True

        print(right_encoder_rawValue_current)
        print(count_flag)
        print(count)
        
    

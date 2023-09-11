import time
import serial
from datetime import datetime
ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1)
time.sleep(0.1)
i = 0

right_encoder_rawValue_current = 0.0
counter = 0.0
counter_flag = False
total_counter = 0.0
time_counter = 0.0
previous_encoder_value = 0.0


time.sleep(1)
start_time_seconds = time.time()
for i in range(100):
    send_data = 'KS110F100S110S110G'
    ser.write(bytes(send_data, 'utf-8'))
    time.sleep(0.1)
    print('Initial Loop')

while True:
    start_loop = time.time()

    send_data = 'KS110F100S110S110G'
    ser.write(bytes(send_data, 'utf-8'))
    
    packet = ser.readline()

    try:
        #print(serial_decode) position 0 = right encoder raw value, 1 = left Encoder Raw Value
        serial_decode = packet.decode("utf-8","ignore")
        serial_split = serial_decode.split(",")
    
        right_encoder_rawValue_current = int(serial_split[0])    
    except:
        pass

    
    
    
    if(right_encoder_rawValue_current >= 30000.0 and counter_flag == True):
        counter = counter + 3.21254902  
        counter_flag = False
    
 
    if(right_encoder_rawValue_current < 30000):
        counter_flag = True

    if(right_encoder_rawValue_current > 30000):
        total_counter = total_counter + (right_encoder_rawValue_current/10000) 

    end_time = time.time() - start_time_seconds

   

    encoder_difference = abs(right_encoder_rawValue_current - previous_encoder_value)
    
    time_difference = time.time() - start_loop
    rpm = ((encoder_difference/10200)/time_difference) * 60

    print('Counter: ', counter, ' Encoder: ', right_encoder_rawValue_current, ' Time_counter ', end_time, ' Encoder_Difference:', encoder_difference, ' Time_Difference:',time_difference, ' RPM:', rpm)
    
    previous_encoder_value = right_encoder_rawValue_current
    
    time.sleep(0.001)


    
import time
import serial
ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1)
time.sleep(0.1)
i = 0

right_encoder_rawValue_current = 0

for k in range(1):
    send_data = 'KS110F090S110S110G'
    ser.write(bytes(send_data, 'utf-8'))
    time.sleep(0.1)



while True:
    i = i + 1
    
    #send_data = str(i%2) + 'F100F112' 

    #send_data = 'KS110F255S110S110G'
    #send_data = send_data + '\n' 
    #ser.write(bytes(send_data, 'utf-8'))
    #ser.write(send_data.encode())
    
    packet = ser.readline()

    try:
        #print(serial_decode) position 0 = right encoder raw value, 1 = left Encoder Raw Value
        serial_decode = packet.decode("utf-8","ignore")
        serial_split = serial_decode.split(",")
    
        right_encoder_rawValue_current = int(serial_split[0])
       
            
    except:
        pass

   
    if(right_encoder_rawValue_current > 14000.0):
        send_data = 'KS110S100S110S110G'
        ser.write(bytes(send_data, 'utf-8'))
    
    if(right_encoder_rawValue_current < 20000.0):
        send_data = 'KS110F255S110S110G'
        ser.write(bytes(send_data, 'utf-8'))
    
    if(right_encoder_rawValue_current == 0):
        send_data = 'KS110F255S110S110G'
        ser.write(bytes(send_data, 'utf-8'))

    #right_encoder_rawValue_current = 30000
    print(right_encoder_rawValue_current)
    
    time.sleep(0.001)
    
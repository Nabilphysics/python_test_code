import time
import serial
ser = serial.Serial('/dev/ttyACM0', 115200,timeout= 1)
time.sleep(0.1)

encoder_highest = 1023.0
encoder_lowest = 0.0
previous_encoder = 0.0
encoder_tick_resolution = 1.0
current_encoder = 0.0
tick_count = 0.0
tick_count_resolution = 1.0
highest_tick = 30000.0
lowest_tick = -30000.0
right_encoder_rawValue_current = 0.0
first_cycle_flag = True

while True:
    if ser.in_waiting:
        serial_raw = ser.readline() 
        #print(serial_raw)
        try:
            serial_decode = serial_raw.decode('utf-8').rstrip('\n')
            #print(serial_decode) position 0 = right encoder raw value, 1 = left Encoder Raw Value
            serial_split = serial_decode.split(',')
        
            current_encoder = int(serial_split[2])
            #left_encoder_rawValue_current = float(serial_split[1])
        except:
            pass

        # If Rotation is in Positive Direction (Clockwise)  
        if((previous_encoder > encoder_highest * 0.7 and previous_encoder <= encoder_highest) and (current_encoder >= encoder_lowest and current_encoder < encoder_highest * 0.3)):
            previous_encoder = previous_encoder - encoder_highest
        #Rotation Check if Negative Direction (Anti Clockwise)
        elif((current_encoder > encoder_highest * 0.7 and current_encoder <= encoder_highest) and (previous_encoder >= encoder_lowest and previous_encoder < encoder_highest * 0.3)):
            previous_encoder = previous_encoder + encoder_highest
                
        if(current_encoder <= previous_encoder - encoder_tick_resolution):
            # change + to - after this line if you want
            tick_count = tick_count + (abs(current_encoder - previous_encoder)/encoder_tick_resolution)
            # We want Encoder Tick count 0 at Robot Startup. So it will check startup and will reset tick counter
            if(first_cycle_flag == True):
                tick_count = 0
                first_cycle_flag = False

            #print('Tick- : ', tick_count, ' C_Enc: ', current_encoder,' P_Enc: ',previous_encoder, ' Diff: ', current_encoder - previous_encoder)
            #print(' - - ')
            previous_encoder = current_encoder 
        
        elif((current_encoder >= previous_encoder + encoder_tick_resolution)):
            tick_count = tick_count - (abs(current_encoder - previous_encoder)/encoder_tick_resolution)
            # We want Encoder Tick count 0 at Robot Startup. So it will check startup and will reset tick counter
            if(first_cycle_flag == True):
                tick_count = 0
                first_cycle_flag = False
            #print('Tick+ : ', tick_count, ' C_Enc: ', current_encoder,' P_Enc: ',previous_encoder, ' Diff: ', current_encoder - previous_encoder)
            #print(' - - -')
            previous_encoder = current_encoder 

        if(tick_count > highest_tick):
            tick_count = 0

        if(tick_count < lowest_tick):
            tick_count = 0  
       
        print(' Current_Data:', current_encoder, ' Tick Count:',tick_count) 
     
   
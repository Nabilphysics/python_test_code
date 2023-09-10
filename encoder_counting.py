encoder_highest = 10.0
encoder_lowest = 0.0
previous_encoder = 0.0
encoder_tick_resolution = 1.0
current_encoder = 0.0
tick_count = 0
tick_count_resolution = 1
highest_tick = 100
lowest_tick = -100
first_cycle_flag = True

while(1):
    encoder_analog_data = input("  ")
    current_encoder = float(encoder_analog_data)
    
    #Rotatin Check if Negative Direction (Anti Clockwise)
    if((current_encoder > encoder_highest * 0.7 and current_encoder <= encoder_highest) and (previous_encoder >= encoder_lowest and previous_encoder < encoder_highest * 0.3)):
        previous_encoder = previous_encoder + encoder_highest
        print('Prev +: ',previous_encoder)
    #Rotation Positive Direction (Clockwise)  
    elif((previous_encoder > encoder_highest * 0.7 and previous_encoder <= encoder_highest) and (current_encoder >= encoder_lowest and current_encoder < encoder_highest * 0.3)):
        previous_encoder = previous_encoder - encoder_highest
        print('Prev -: ',previous_encoder)
      
    if((current_encoder >= previous_encoder + encoder_tick_resolution)):
        tick_count = tick_count + (abs(current_encoder - previous_encoder)/encoder_tick_resolution)
        # We want Encoder Tick count 0 at Robot Startup. So it will check startup and will reset tick counter
        if(first_cycle_flag == True):
            tick_count = 0
            first_cycle_flag = False
        previous_encoder = current_encoder 
    elif(current_encoder <= previous_encoder- encoder_tick_resolution):
        tick_count = tick_count - (abs(current_encoder - previous_encoder)/encoder_tick_resolution)
        # We want Encoder Tick count 0 at Robot Startup. So it will check startup and will reset tick counter
        if(first_cycle_flag == True):
            tick_count = 0
            first_cycle_flag = False
        previous_encoder = current_encoder 
        

    if(tick_count > highest_tick):
        tick_count = 0
        
    if(tick_count < lowest_tick):
        tick_count = 0  
        
    
    
    #print('Prev_Enc:',previous_encoder)    
    
    print(' Current_Data:', current_encoder,' Tick Count:',tick_count)   
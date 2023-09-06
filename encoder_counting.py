encoder_highest = 14.0
encoder_lowest = 0.0
previous_encoder = 0.0
encoder_tick_resolution = 1.0
current_encoder = 0.0
tick_count = 0
tick_count_resolution = 1
highest_tick = 100
lowest_tick = -100

while(1):
    encoder_analog_data = input(" --- Plz Input Encoder Analog Data: ")
    current_encoder = float(encoder_analog_data)
    
    #Rotatin Check if Negative Direction (Anti Clockwise)
    if((current_encoder > encoder_highest * 0.7 and current_encoder <= encoder_highest) and (previous_encoder >= encoder_lowest and previous_encoder < encoder_highest * 0.3)):
        previous_encoder = previous_encoder + encoder_highest
    #Rotation Positive Direction (Clockwise)  
    elif((previous_encoder > encoder_highest * 0.7 and previous_encoder <= encoder_highest) and (current_encoder >= encoder_lowest and current_encoder < encoder_highest * 0.3)):
        previous_encoder = previous_encoder - encoder_highest
      
    if((current_encoder >= previous_encoder + encoder_tick_resolution)):
        tick_count = tick_count + tick_count_resolution
        previous_encoder = current_encoder 
    elif(current_encoder <= previous_encoder- encoder_tick_resolution):
        tick_count = tick_count - tick_count_resolution
        previous_encoder = current_encoder 
        

    if(tick_count > highest_tick):
        tick_count = 0
        
    if(tick_count < lowest_tick):
        tick_count = 0  
        
    
    
    #print('Prev_Enc:',previous_encoder)    
    
    print(' Current_Data:', current_encoder, ' Previous_Data:', previous_encoder,' Tick Count:',tick_count)   
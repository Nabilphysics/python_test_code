target_left_wheel_velocity = 0.0
target_right_wheel_velocity = 0.0

robot_base = 1.0


#########
encoder_min = -32768
encoder_max = 32768
prev_encoder = 0
rmult = 0
encoder_low_wrap = (encoder_max - encoder_min) * 0.3 + encoder_min
encoder_high_wrap = (encoder_max - encoder_min) * 0.7 + encoder_min
#########

def targetWheelVelocity(commanded_linear_velocity, commanded_angular_velocity):
        
        target_left_wheel_velocity = commanded_linear_velocity - ((commanded_angular_velocity * robot_base)/2)
        target_right_wheel_velocity = commanded_linear_velocity + ((commanded_angular_velocity * robot_base)/2)
        print('Target Left Wheel Velocity: ',target_left_wheel_velocity) 
        print('Target Right Wheel Velocity: ',target_right_wheel_velocity) 

def rwheelCallback(data):
    global encoder_high_wrap, encoder_low_wrap, rmult, prev_encoder
    enc = data
    if(enc < encoder_low_wrap and prev_encoder > encoder_high_wrap):
        rmult = rmult + 1
        print('rmult+ : ', rmult)
    
    if(enc > encoder_high_wrap and prev_encoder < encoder_low_wrap):
        rmult = rmult - 1
        print('rmult : ', rmult)
        
    right = 1.0 * (enc + rmult * (encoder_max - encoder_min))
    print("self.right= ", right) 
    prev_encoder = enc

#targetWheelVelocity(0.04,0.0)
for i in range(-5, 5, 1):
     rwheelCallback(i)
     print(i)




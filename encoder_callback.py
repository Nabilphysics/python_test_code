encoder_low_wrap = -13107.2
encoder_high_wrap = 13107.2
encoder_max = 32768
encoder_min = -32768
left = 0
lmult = 0
enc = 0
prev_lencoder = 0



def lwheelCallback(msg):
    global lmult, left, enc, prev_lencoder
    enc = msg
    
    if (enc < encoder_low_wrap and prev_lencoder > encoder_high_wrap):
        lmult = lmult + 1
        print("lmult+: " + str(lmult))
        
    if (enc > encoder_high_wrap and prev_lencoder < encoder_low_wrap):
        lmult = lmult - 1
        print("lmult-: " + str(lmult))
        
    left = 1.0 * (enc + lmult * (encoder_max - encoder_min)) 
    print("left: " + str(left))
    prev_lencoder = enc
    print("prev_lencoder: " + str(prev_lencoder))

 

def main():
    lwheelCallback(32000)
    

if __name__ == "__main__":
    main()
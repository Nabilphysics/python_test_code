
encoder_min = -5
encoder_max = 5

mult = 0 
prev_encoder = 0
curr_enc = 0 
encoder_low_wrap = ((encoder_max - encoder_min) * 0.3 + encoder_min) 
encoder_high_wrap = ((encoder_max - encoder_min) * 0.7 + encoder_min )


def leftForwardEncoderCount(en):
        global mult,prev_encoder,curr_enc,encoder_high_wrap, encoder_low_wrap
        enc = en
        if (enc < encoder_low_wrap and prev_encoder > encoder_high_wrap):
            mult = mult + 1
       
        if (enc > encoder_high_wrap and prev_encoder < encoder_low_wrap):
            mult = mult - 1
            
        curr_enc= 1.0 * (enc + mult * (encoder_max - encoder_min)) 
        prev_encoder = enc
        print(curr_enc)




def main():
    while True:
        inp = int(input('Input Encoder: '))
        leftForwardEncoderCount(inp)



# __name__
if __name__=="__main__":
    main()
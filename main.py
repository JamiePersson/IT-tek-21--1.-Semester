from dcmotor import DCMotor1      
from machine import Pin, PWM   
from time import sleep

frequency = 15000

#Driver 1, A + B - Højre Side
D1_STBY = Pin(17, Pin.OUT) #H-BRO 1, er sat til VALUE 1 hele tiden.
D1_PHA_A = Pin(4, Pin.OUT)
D1_EN_A = PWM(Pin(16), frequency) #Aktiverer højre baghjul
#D1_PHA_B = Pin(0, Pin.OUT)
#D1_EN_B = PWM(Pin(15), frequency) #Aktiverer højre forhjul

# #Driver 2, A + B - Venstre Side
# D2_STBY = Pin(14, Pin.OUT) #H-BRO 2, er sat til VALUE 1 hele tiden.
# D2_PHA_A = Pin(13, Pin.OUT)
# D2_EN_A = PWM(Pin(12), frequency) #Aktiverer venstre forhjul
# D2_PHA_B = Pin(27, Pin.OUT)
# D2_EN_B = PWM(Pin(26), frequency) #Aktiverer venstre baghjul    


D1_STBY.value(1)#H bro højre side
# D2_STBY.value(1)#H bro venstre side

#DC1A 
dc_motor1A = DCMotor1(D1_STBY, D1_PHA_A, D1_EN_A)      
dc_motor1A = DCMotor1(D1_STBY, D1_PHA_A, D1_EN_A, 350, 1023)

#DC1B 
#dc_motor1B = DCMotor(D1_STBY, D1_PHA_B, D1_EN_B)      
#dc_motor1B = DCMotor(D1_STBY, D1_PHA_B, D1_EN_B, 350, 1023)

#DC2A 
# dc_motor2A = DCMotor2(D2_STBY, D2_PHA_A, D2_EN_A)      
# dc_motor2A = DCMotor2(D2_STBY, D2_PHA_A, D2_EN_A, 350, 1023)

#DC2B 
#dc_motor2B = DCMotor(D2_STBY, D2_PHA_B, D2_EN_B)      
#dc_motor2B = DCMotor(D2_STBY, D2_PHA_B, D2_EN_B, 350, 1023)


#D1A
while True:
    dc_motor1A.forward(10)
    sleep(2)
    dc_motor1A.stop()
    sleep(2)
    dc_motor1A.backwards(10)
    sleep(2)
    dc_motor1A.forward(5)
    sleep(2)
    dc_motor1A.stop()
    sleep(2)
#     dc_motor2A.forward(50)
#     sleep(2)
#     dc_motor2A.stop()
#     sleep(2)
#     dc_motor2A.backwards(100)
#     sleep(2)
#     dc_motor2A.forward(5)
#     sleep(2)
#     dc_motor2A.stop()
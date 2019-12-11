import RPi.GPIO as GPIO  #using RPi.GPIO as GPIO
import time              #use time from the time package

PULSE=7                  #initialize PULSE to  GPIO 7
R=5                      #initialize R as 5
GPIO.setwarnings(False)  #setwarning as False
GPIO.setmode(GPIO.BCM)   #set GPIO pins as BCM(Broadcom
GPIO.setup(PULSE,GPIO.OUT)#set Pulse as OUTPUT
p=GPIO.PWM(7,50)          #set p as GPIO PWM with 50Hz
p.start(7.5)              #Start at servo 7.5ms

for x in range(5):        
 p.ChangeDutyCycle(7.5)   #Servo will rotate to its Neutral Position
 print("NEUTRAL")
 time.sleep(3)
 p.ChangeDutyCycle(12.5)  #Servo will rotate to its 180 Position
 print("SERVO 180")
 time.sleep(2)
 p.ChangeDutyCycle(2.5)   #Servo will rotate to its 0 Position
 print("SERVO 0")
 time.sleep(2)
p.stop()
GPIO.cleanup()



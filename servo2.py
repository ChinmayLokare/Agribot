import RPi.GPIO as GPIO
import time

PULSE=7
R=3
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PULSE,GPIO.OUT)
p=GPIO.PWM(7,50)
p.start(7.5)
for x in range(3):
 p.ChangeDutyCycle(12.5)  #//180
 print("SERVO 180")
 time.sleep(2)
 p.ChangeDutyCycle(2.5)   #//0
 print("SERVO 0")
 time.sleep(2)
 p.ChangeDutyCycle(7.5)	  #//NEUTRAL
 print("NEUTRAL")
 time.sleep(4)
p.stop()
GPIO.cleanup()



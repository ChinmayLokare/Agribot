import RPi.GPIO as GPIO
import time
import cv2
import datetime


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
 cap=cv2.VideoCapture(0)

 print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
 print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


 check , frame =cap.read()
        # date and time on it

 font= cv2.FONT_HERSHEY_SIMPLEX
 text = 'width:'+ str(cap.get(3)) + 'height:' + str(cap.get(4))
 datet=str(datetime.datetime.now())
 frame =cv2.putText(frame , datet ,(10,50), font ,1,(0,255,255), 2 ,cv2.LINE_AA)
 print(check)
 print(frame)

        #representing image
 cv2.imshow("capturing",frame)

        # for press any key to out (millis )

 cv2.waitKey(0)

        # saving image
 cv2.imwrite(str(x)+'.jpg',frame)

         # shutdown the camera
 cap.release()
 time.sleep(2)
 p.ChangeDutyCycle(2.5)   #//0
 print("SERVO 0")
 cap=cv2.VideoCapture(0)

 print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
 print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


 check , frame =cap.read()
        # date and time on it

 font= cv2.FONT_HERSHEY_SIMPLEX
 text = 'width:'+ str(cap.get(3)) + 'height:' + str(cap.get(4))
 datet=str(datetime.datetime.now())
 frame =cv2.putText(frame , datet ,(10,50), font ,1,(0,255,255), 2 ,cv2.LINE_AA)
 print(check)
 print(frame)

        #representing image
 cv2.imshow("capturing",frame)

        # for press any key to out (millis )

 cv2.waitKey(0)
 
        # saving image
 cv2.imwrite(str(x)+'.jpg',frame)

         # shutdown the camera
 cap.release()
 time.sleep(2)
 p.ChangeDutyCycle(7.5)	  #//NEUTRAL
 print("NEUTRAL")
 cap=cv2.VideoCapture(0)

 print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
 print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


 check , frame =cap.read()
        # date and time on it

 font= cv2.FONT_HERSHEY_SIMPLEX
 text = 'width:'+ str(cap.get(3)) + 'height:' + str(cap.get(4))
 datet=str(datetime.datetime.now())
 frame =cv2.putText(frame , datet ,(10,50), font ,1,(0,255,255), 2 ,cv2.LINE_AA)
 print(check)
 print(frame)

        #representing image
 cv2.imshow("capturing",frame)

        # for press any key to out (millis )

 cv2.waitKey(0)

        # saving image
 cv2.imwrite(str(x)+'.jpg',frame)

         # shutdown the camera
 cap.release()
 time.sleep(4)
p.stop()
GPIO.cleanup()



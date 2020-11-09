import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

def turnonModulation():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(16,GPIO.OUT)
	GPIO.setup(20,GPIO.OUT)
	GPIO.setup(21,GPIO.OUT)
	while True:
		color =input("Choose color(R:red , G:green , B:Blue)  : ")
		if color=='R':
			pwm_led=GPIO.PWM(16,500)
			break
		elif color=='G':
			pwm_led=GPIO.PWM(20,500)
			break
		elif color=='B':
			pwm_led=GPIO.PWM(21,500)
			break
		else:
			print("Wrong input color type!")
	pwm_led.start(0)
	try:
		while True:
			for i in range(101): # output from 0 to 100
				if(i==100):
					i=0
				pwm_led.ChangeDutyCycle(i) #change output
				time.sleep(0.02)
	except KeyboardInterrupt:
		GPIO.cleanup()

if __name__=="__main__":
	turnonModulation()
	GPIO.cleanup()

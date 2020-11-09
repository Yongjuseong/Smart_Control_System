import RPi.GPIO as GPIO
import time
def turnonButton():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25,GPIO.IN)
	GPIO.setup(25,GPIO.OUT)
	GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP) #Button input setting
	control = False #LED control static variable
	def buzz():
		pitch=1000
		duration = 0.1
		period = 1.0/pitch
		delay = period /2
		cycles = int(duration * pitch)
		for i in range(cycles):
			GPIO.output(25,True)
			time.sleep(delay)
			GPIO.output(25,False)
			time.sleep(delay)
	try:
		while True:
			button_state=GPIO.input(12)
			if button_state == False: # push Button ==>False
				if control==True: # Toggle
					control=False
					print("All Off")
					GPIO.cleanup()
					break
				else:
					control=True
					print('button pressed')
			if control ==True: #Button True -> buzzer On
				buzz()
				time.sleep(0.3)
			time.sleep(0.3) #0.2 seconds interval
	except KeyboardInterrupt:
		GPIO.cleanup()
if __name__=="__main__":
		try:
			turnonButton()

		except KeyboardInterrupt:
			GPIO.cleanup()

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) #BCM 16 Red
def turnonRed():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(16,GPIO.OUT) # BCM 16 RED)
	try:
		while True:
			GPIO.output(16,True) # 16 On
	except KeyboardInterrupt:
		GPIO.output(16,False) # 16 Off
		GPIO.cleanup()

if __name__=="__main__":
	turnonRed()
	GPIO.cleanup()

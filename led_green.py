import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)
def turnonGreen():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(20,GPIO.OUT) #BCM 20 Green
	try:
		while True:
			GPIO.output(20,True) # 20 ON
	except KeyboardInterrupt:
		GPIO.output(20,False)
		GPIO.cleanup()

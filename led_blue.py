import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
def turnonBlue():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(21,GPIO.OUT) #BCM 21 blue
	try:
		while True:
			GPIO.output(21,True) # 21 ON
	except KeyboardInterrupt:
		GPIO.output(21,False)
		GPIO.cleanup()

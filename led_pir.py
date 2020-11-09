import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(24,GPIO.IN)

def turnonPir():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(16,GPIO.OUT)
	GPIO.setup(24,GPIO.IN)
	check =False
	try:
		while True:
			if GPIO.input(24) == True: # sensor -> True
				if check == True:
					while True: # blink
							print("Again Sensor detection")
							GPIO.output(16,True) # Turn on LED
							time.sleep(0.7)
							GPIO.output(16,False) # Turn off LED
							time.sleep(0.7)
							GPIO.output(16,True)
							time.sleep(0.7)
							GPIO.output(16,False)
							if GPIO.input(24) == False:
								print("Detection off!!")
								break
				if check==False:
					print("Detection On!!")
					check=True
					GPIO.output(16,True) # Turn on LED

			if GPIO.input(24) == False: # Sensor -> False
				print("Detction Off!!")
				check=False
				GPIO.output(16,False) # Turn off LED
			time.sleep(3)

	except KeyboardInterrupt:
		GPIO.output(16,False)
		GPIO.cleanup()


if __name__ =="__main__":
		turnonPir()
		GPIO.cleanup()

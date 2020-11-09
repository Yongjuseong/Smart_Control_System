import RPi.GPIO as GPIO
import time
import led_red as LedRed
import led_green as LedGreen
import led_blue as LedBlue
import led_pir as LedPir
import led_modulation as LedModulation
import led_blink as LedBlink
import button_buzzer as ButtonBuzzer
import buzzer_melody as BuzzerMelody
GPIO.setmode(GPIO.BCM)
'''
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP) #Button input setting
GPIO.setup(25,GPIO.IN)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP) #Button input setting
control = False #LED control static variable
def buzz():
	pitch=1000
	duration = 0.1
	period = 1.0/pitch
	delay = period /2
	cycles = int(duration *  pitch)
	for i in range(cycles):
		GPIO.output(25,True)
		time.sleep(delay)
		GPIO.output(25,False)
		time.sleep(delay)
'''
if __name__=="__main__":
	while True:
		'''
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
		time.sleep(0.3) #0.2 seconds interval '''
		print("==========================================================================")
		print(" R : Red on | G : Green On | B: Blue On | PIR: Red on then Blink |")
		print(" M : Modulation | X :BLink On | Button On : Buzzer on then All off|")
		print(" S : Sound On | O : All Off ")
		print("==========================================================================")
		command = input("command input : ") # command input
		if command=='R':
			print("Turn on Red")
			LedRed.turnonRed() # Red On
			GPIO.cleanup()
		elif command =='G':
			print("turn on Green") #Green On
			LedGreen.turnonGreen()
		elif command =='B':
			print("Turn on Blue") #Blue On
			LedBlue.turnonBlue()
		elif command =='P': #PIR Sensor
			print("PIR Sensor On")
			LedPir.turnonPir()
		elif command=='M': #Modulation
			print("Modulation On")
			LedModulation.turnonModulation()
		elif command=='X': #Blink
			print("Blink On")
			LedBlink.turnonBlink()
		elif command=='S': # sound on
			BuzzerMelody.turnonMelody()
		elif command=='O':
			print("All Off")
			GPIO.cleanup()
			break
		elif command=='Z':
			ButtonBuzzer.turnonButton()
		else:
			print("wrong command")

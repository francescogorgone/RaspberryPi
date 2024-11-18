import time
import RPi.GPIO as GPIO

BTN_PIN = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #pull_up_down dice che se non è collegato a niente voglio che la tensione sia 0

#while True:
#    if GPIO.input(BTN_PIN) == GPIO.HIGH:
#        print('Button pushed')

def button_callback(channel):
    print('Callback handled: Button pushed!')

GPIO.add_event_detect(BTN_PIN, GPIO.RISING, callback=button_callback, bouncetime=200)

message = input('Press anything to quit\n')

GPIO.cleanup()


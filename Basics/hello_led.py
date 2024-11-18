#Import all the required packages
import time #per mettere in pausa l'esecuzione del programma
import RPi.GPIO as GPIO #per gestire le GPIO

# LED pin (GPIO channel number)
LED_PIN = 11

#LED On/Off functions
def turn_led_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    return 'led on'
def turn_led_off():
    GPIO.output(LED_PIN, GPIO.LOW)
    return 'led off'

#Use raspberry Pi board and pin numbers
GPIO.setmode(GPIO.BOARD) #impostare la modalità di numerazione fisica

#Set up LED pin and GPIO output channel
GPIO.setup(LED_PIN, GPIO.OUT)

#Turn the led on
turn_led_on()

#Let's keep the LED on for two seconds
time.sleep(2)

#Turn the LED off
turn_led_off()

#Clean up all GPIO ports
GPIO.cleanup()

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
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

#BOT
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def on(update: Update, context: ContextTypes.DEFAULT_TYPE):
    turn_led_on()
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Led is turned on")

async def off(update: Update, context: ContextTypes.DEFAULT_TYPE):
    turn_led_off()
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Led is turned off")

if __name__ == '__main__':
    application = ApplicationBuilder().token('your_API_token').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    on_handler = CommandHandler('on', on)
    application.add_handler(on_handler)

    off_handler = CommandHandler('off', off)
    application.add_handler(off_handler)

    application.run_polling()



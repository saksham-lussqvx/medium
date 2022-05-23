from gtts import gTTS # pip install gtts
from telegram import * # pip install python-telegram-bot
from telegram.ext import (CallbackContext, CommandHandler, Filters,
MessageHandler, Updater)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="Welcome to TxtToSpeechBot!\n\n \
    I will convert your text to speech with ease!\n\nPlease send your \
    message and I'll convert it to audio.")

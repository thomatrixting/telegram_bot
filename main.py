import os

##dependences for telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext import Defaults
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


from os import path
from datetime import datetime
import pytz #mange times zones
from functions import process_df,add_row_to_file,read_users_id

#inicilizate the bot 
defaults = Defaults(parse_mode ='MarkdownV2')

updater = Updater("5684878052:AAFgOiVYom9psZYwq1YUJMYUafOsXIu_c4E",
                  use_context=True,
                  defaults=defaults)

bogota_time_zone = pytz.timezone('America/Bogota')
bogota_date = datetime.now(bogota_time_zone).strftime("%d-%m-%Y") 

root = path.dirname(path.abspath(__file__))
df_path = path.join(root, 'df.txt')
users_path = path.join(root, 'users.txt')

log_in_open = False

def start(update: Update, context: CallbackContext):
    update.message.reply_text("start mesage")

def notification(update: Update, context: CallbackContext):
   #you need to fix the encoding problem
    message = process_df(df_path,bogota_date)
    update.message.reply_text(message)

def log_in(update: Update, context: CallbackContext):
    message = "send pasword: "
    global log_in_open
    log_in_open = True
    update.message.reply_text(message)

def log_in_data_reciver(update: Update, context: CallbackContext):
    input_recived = update.message.text
    input_recived = str.lower(input_recived)
    global log_in_open


    if input_recived == "tqm" and log_in_open:

        chat_id = update.effective_user.id
        users_id = read_users_id(users_path)
        
        if not users_id in users_id:
            add_row_to_file(users_path,str(chat_id))

        update.message.reply_text('updated')
        notification(update,context)

        log_in_open = False
        
    else:
        update.message.reply_text('i don\'t understand')




##set responses
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('notification', notification))
dp.add_handler(CommandHandler('login', log_in))
dp.add_handler(MessageHandler(Filters.text, log_in_data_reciver))

#run the bot
updater.start_polling()


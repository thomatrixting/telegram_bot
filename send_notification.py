##dependences for telegram
from telegram import Bot

from os import path
from functions import process_df,read_users_id
from datetime import datetime
import pytz #mange times zones

def send_message(message,user_id,token):
    tb = Bot(token)
    ret_msg = tb.send_message(user_id,message)
    assert ret_msg.message_id 

def send_messages(bogota_date):

    #inicilizate the bot 
    TOKEN = "5684878052:AAFgOiVYom9psZYwq1YUJMYUafOsXIu_c4E"

    root = path.dirname(path.abspath(__file__))
    df_path = path.join(root, 'df.txt')
    users_path = path.join(root, 'users.txt')

    message = process_df(df_path,bogota_date)
    users_id = read_users_id(users_path)

    for user_id in users_id:
        send_message(message,user_id,TOKEN)

def start_sending():
    bogota_time_zone = pytz.timezone('America/Bogota')
    bogota_date = datetime.now(bogota_time_zone).strftime("%d-%m-%Y") 

    send_messages(bogota_date)
if __name__ == "__main__" :
    start_sending()
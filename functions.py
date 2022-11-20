from random import choice
from telegram import Bot

def process_out(text):
    new_text = []
    replace_dict = {
            '(':'\(',
            ')':'\)',
            '.':'\.',
            '{':'\{'
        }

    if type(text) != list:
        text = [text]

    for instance in text:
        for key, value in replace_dict.items():
            instance = instance.replace(key, value)
        new_text.append(instance)
    
    return(new_text)

def process_df(df_path,bogota_date):

    with open(df_path) as f:
        df_words = f.readlines()

    for row in df_words:
        row_split = row.split(',')

        if row_split[0] == bogota_date:
            send_row = row_split[1:]
            return send_row[0] #resolve the especial characters 
    
    send_row = choice(df_words).split(',')[1:]
    return send_row[0]

def add_row_to_file(file_path,text):
    with open(file_path,'a') as f:
        f.write(text + '\n')

def read_users_id(file_path):
    with open(file_path,'r') as f:
        users = f.readlines()
    users = [user.replace('\n','') for user in users]
    return users
    
if __name__ == "__main__" :
    result = process_df('df.txt','05-11-2022')
    print(result)

    add_row_to_file('users.txt','id_1')
    add_row_to_file('users.txt','id_2')

    print(read_users_id('users.txt'))


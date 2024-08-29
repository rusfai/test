from flask import Flask, jsonify, request, redirect
import asyncio
from aiogram import Bot
import mysql
import mysql.connector
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardMarkup



token = '7224598074:AAHahsZ7bwKowTPkApaWU6JI6jmNSOg2mag'


db_host = "93.93.207.52"
db_user = "gen_user" 
db_password = "PUQC7sa$"
db_name = "default_db"

bot = Bot(token)

def connect():
    mydb = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
    )
    return mydb

async def gg(user_id, account):

    await bot.send_message(user_id, f'Аккаунт {account} успешно пополнен!')

    return 'sucsess'


app = Flask(__name__)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    asyncio.get_event_loop().run_until_complete(gg(int(5779182088), 'fdsgdgb'))
    try:
        all_args = str(request.args.get())
        asyncio.get_event_loop().run_until_complete(gg(int(5779182088), f'{all_args}'))
            
        id_user = int(id_user)
        print(id_user)


        
        mydb = connect()
        mycursor = mydb.cursor(buffered=True)

        
        mycursor.execute("SELECT register FROM kwork14_user WHERE id_tg = '{}'".format(id_user))
        register = mycursor.fetchone()
        register = register[0]

        if int(register) == 0:

            mycursor.execute("SELECT lang FROM kwork14_user WHERE id_tg = '{}'".format(id_user))
            lang = mycursor.fetchone()
            lang = lang[0]


            if lang == 'ru':
                text = 'Вы успешно зарегистрировались! Выберите режим'
            elif lang == 'en':
                text = 'You have successfully registered! Select a mode'
            elif lang == 'tr':
                text = 'Başarıyla kaydoldunuz! Modu seçin'
            else:
                text = 'Ошибка'

            mycursor.execute("UPDATE kwork14_user SET register = '{}' WHERE id_tg = '{}' ".format(1, id_user))
            mydb.commit()

            mycursor.close()
            mydb.close()

            

        return 'sucsess'
    except:
        return 'warning' 




if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
import asyncio
from aiogram import Bot
import mysql
import mysql.connector
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardMarkup

admin_tg = 5779182088

db_host = "93.93.207.52"
db_user = "gen_user" 
db_password = "PUQC7sa$"
db_name = "default_db"

token = '6188238037:AAFZcsoJGYGngbE2awHEHmtOxa2STVqkg0M'
bot = Bot(token)

def connect():
    mydb = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
    )
    return mydb

async def gg(user_id, msg):
    kb_list = [
        [types.InlineKeyboardButton(text='🛫AVIATOR🛫', callback_data='aviator')],
        [types.InlineKeyboardButton(text='🚀LUCKY JET🚀', callback_data='luckyjet')],
        [types.InlineKeyboardButton(text='⭐MINES⭐', callback_data='mines')],
        [types.InlineKeyboardButton(text='🆕ROYAL MINES🆕', callback_data='royalmines')],
        [types.InlineKeyboardButton(text='🆕BOMBUCKS🆕', callback_data='bombucks')],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():

    try:
        asyncio.get_event_loop().run_until_complete(gg(admin_tg, f'Новая регестрация' ))


        id_user = request.args.get('ID')
        id_user = int(id_user)

        
        mydb = connect()
        mycursor = mydb.cursor(buffered=True)

        mycursor.execute("SELECT lang FROM kwork14_user WHERE id_tg = '{}'".format(id_user))
        lang = mycursor.fetchone()
        lang = lang[0]

        if lang == 'ru':
            text = 'Вы успешно зарегистрировались! Нажмите на "Главное меню", а потом "Получить сигнал"'
        elif lang == 'en':
            text = 'You have successfully registered! Click on the "Main Menu" and then "Receive signal"'
        elif lang == 'tr':
            text = 'Başarıyla kaydoldunuz! "Ana Menü" ye ve ardından "Sinyal al" a tıklayın'
        else:
            text = 'Ошибка'

        mycursor.execute("UPDATE kwork14_user SET register = '{}' WHERE id_tg = '{}' ".format(1, id_user))
        mydb.commit()

        mycursor.close()
        mydb.close()

        asyncio.get_event_loop().run_until_complete(gg(int(id_user), f'{text}'))
        return id_user
    
    except:
        return


if __name__ == '__main__':
    app.run(debug=True)
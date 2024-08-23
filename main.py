from flask import Flask, jsonify, request, redirect, url_for
import asyncio
from aiogram import Bot
import mysql
import mysql.connector
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardMarkup



token = '7541114114:AAE4FLFt7guDGBMztpx62lGrz0mDyTxMcfE'

db_host = "147.45.236.147"
db_user = "gen_user" 
db_password = ",E3+QJ/\C0-q*{"
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

    return 'sucsess'


async def edit(user_id, mess, lang, mod):

    if lang == 'ru':
        accept = '✅Я зарегестрировался'
        instruction = '📚ИНСТРУКЦИЯ'
        main_menu = '🏠Главное меню'
        text = 'Подтвердите регистрацию'
    elif lang == 'en':
        accept = '✅I have registered' 
        instruction = '📚INSTRUCTION'
        main_menu = '🏠Main Menu'
        text = 'Confirm registration'
    elif lang == 'tr':
        accept = '✅Kayıt oldum'
        instruction = '📚TALİMAT'
        main_menu = '🏠Ana menü'
        text = 'Kaydı onaylayın'


    kb_list = [
        [types.InlineKeyboardButton(text=accept, callback_data=f'{mod}_reg')],
        [types.InlineKeyboardButton(text=instruction, callback_data=f'instruction_{mod}')],
        [types.InlineKeyboardButton(text=main_menu, callback_data=mod)]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)

    await bot.edit_message_caption(chat_id=user_id, message_id=mess,  caption=text, reply_markup=keyboard)

    return 'sucsess'

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():

    try:
        id_user = request.args.get('ID')

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

            asyncio.get_event_loop().run_until_complete(gg(int(id_user), f'{text}'))

        return 'sucsess'
    except:
        return 'warning' 

@app.route('/click', methods=['POST'])
def click():

    try:

        id_user = request.args.get('ID')
        id_user.split('_')
        id_user = int(id_user[0])
        message = int(id_user[1])
        mod = id_user[2]
       
        mydb = connect()
        mycursor = mydb.cursor(buffered=True)

        mycursor.execute("SELECT lang FROM kwork14_user WHERE id_tg = '{}'".format(id_user))
        lang = mycursor.fetchone()
        lang = lang[0]

        mycursor.close()
        mydb.close()

        asyncio.get_event_loop().run_until_complete(edit(id_user, message, lang, mod))

    
    except:
        pass
    id = id_user
    return redirect(url_for(f'https://to3a.com/1win?ID={id}'))


if __name__ == '__main__':
    app.run(debug=True)
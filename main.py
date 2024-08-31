from flask import Flask, jsonify, request, redirect
import asyncio
from aiogram import Bot
import mysql
import mysql.connector
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



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

async def gg(user_id, account, amount, message_id):

    text = "После оплаты деньги как правило поступают моментально! Если нет, обратитесь в поддержку."
    
    kb_list = [
            [InlineKeyboardButton(text="Задать вопрос", url="https://t.me/anypayservice")],
            [InlineKeyboardButton(text="Пополнить еще", callback_data="start")]
            ]
    
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list)

    kb = [
      [types.InlineKeyboardButton(text="Подписаться", url=f'''https://t.me/anypaymentTG''')]
      ]

    keyboard_channel = InlineKeyboardMarkup(inline_keyboard=kb)


    await bot.edit_message_text(text=text, chat_id=user_id, message_id=message_id, reply_markup=keyboard)
    await bot.send_message(user_id, f'Аккаунт {account} успешно пополнен на {amount} рублей!\n\n<a href=https://t.me/anypaymentTG>Не забудь подписаться на наш ТГ канал</a>', reply_markup=keyboard_channel, parse_mode="HTML")

    return 'sucsess'


app = Flask(__name__)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    mydb = connect()
    mycursor = mydb.cursor(buffered=True)
    try:
        data = request.get_json(force=False, silent=False, cache=True)
  
        mycursor.execute("SELECT * FROM kwork16_payments WHERE transaction_id = '{}'".format(data['order_uuid']))
        payment_info = mycursor.fetchone()

        asyncio.get_event_loop().run_until_complete(gg(payment_info[1], payment_info[2], payment_info[3], payment_info[5]))

        return 'sucsess'
    except:
        return 'warning' 

    mycursor.close()
    mydb.close()


if __name__ == '__main__':
    app.run(debug=True)

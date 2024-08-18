from flask import Flask, jsonify, request
import asyncio
from aiogram import Bot

token = '6188238037:AAFZcsoJGYGngbE2awHEHmtOxa2STVqkg0M'
bot = Bot(token)


async def gg(user_id, msg):
    await bot.send_message(user_id, msg)




app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    try:
        id_user = request.args.get('ID')
    except:
        id_user = 0
    try:
        anower_id = request.form['ID']
    except:
        anower_id = request.form['ID']
    try:
        a = request.get_json(force=True)
    except:
        a = 0

    asyncio.get_event_loop().run_until_complete(gg(5779182088, f'ОТВЕТ {id_user} {a} {anower_id}' ))
    return a

if __name__ == '__main__':
    app.run(debug=True)
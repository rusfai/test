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
    id_user = request.args.get('ID')
    anower_id = request.form['ID']
    a = jsonify(request.get_json(force=True))
    print(request.get_json(force=True))
    asyncio.get_event_loop().run_until_complete(gg(5779182088, f'{id_user} {request.get_json(force=True)} {anower_id}' ))
    return a

if __name__ == '__main__':
    app.run(debug=True)
from cgitb import handler
import os
import telebot
from flask_sqlalchemy import SQLAlchemy, render_templates
from telebot import types
from flask import Flask


token = '7673939553:AAEVET8kWs7QFanPR8YiZVHHQFuZNjdEjYo'
bot = telebot.TeleBot(token)

sticker_list = ['CAACAgQAAxkBAANeZ1QqAAHiylroWe3mNKiD5i_bNo4TAAJyDgACPLQZUMeeP4x6Lf6LNgQ',
                'CAACAgQAAxkBAANgZ1QqGMpuZEV67umUIOvluKUqR_wAAq4OAAKLwhBTXih_F0rHiUk2BA']

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

db = SQLAlchemy(app)


class Base(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)

@app.route('/')
def index():
    mes = Base.query.all()
    return render_templates('index.html', mes=mes)


@bot.message_handler(content_types=['sticker'])
def handler_sticker(message):
    id = message.sticker.file_id
    em = message.sticker.emoji
    text = f"ID Sticker = ({id}). Emoji: ({em})"
    bot.reply_to(message, text)


@bot.message_handler(commands=['f'])
def handler_f(message):
    current_path_app = os.path.abspath(__file__)
    current_path = os.path.dirname(current_path_app)
    my_file = os.path.join(current_path, 'sticker', 'dota.webp')

    with open(my_file, 'rb') as sticker:
        bot.send_sticker(message.chat.id, sticker)


@bot.message_handler(content_types=['text'])
def is_text(message):

    if message.text == 'a':
        bot.send_sticker(message.chat.id, sticker_list[0])
        return True
    elif message.text == 'CAACAgQAAxkBAANeZ1QqAAHiylroWe3mNKiD5i_bNo4TAAJyDgACPLQZUMeeP4x6Lf6LNgQ':
        bot.send_sticker(message.chat.id, sticker_list[1])
        return True
    elif message.text == 'CAACAgQAAxkBAANgZ1QqGMpuZEV67umUIOvluKUqR_wAAq4OAAKLwhBTXih_F0rHiUk2BA':
        bot.send_sticker(message.chat.id, sticker_list[2])
        return True

    bot.send_message(message.chat.id, 'text')




if __name__ == '__main__':
    bot.infinity_polling()
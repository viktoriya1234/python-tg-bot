import telebot
from telebot import types

token = '7673939553:AAEVET8kWs7QFanPR8YiZVHHQFuZNjdEjYo'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['open'])
def handler_open(message):
    bot.send_message(message.chat.id, 'open the door')


@bot.message_handler(commands=['close'])
def handler_close(message):
    bot.send_message(message.chat.id, 'close the door')


@bot.message_handler(commands=['start', 'stop', 'speed'])
def handler_run_car(message):
    car = 'stand'
    if message.text == '/start':
        car = 'we start moving'
    elif message.text == '/stop':
        car = 'stop'
    elif message.text == '/speed':
        car = 'change speed'

    bot.send_message(message.chat.id, car)


@bot.message_handler(commands=['pizza'])
def handler_pizza(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton(text='Pepperoni')
    btn2 = types.KeyboardButton(text='Cheesy')
    keyboard.add(btn1, btn2)

    mes = bot.send_message(message.chat.id, 'Choose a pizza', reply_markup=keyboard)
    bot.register_next_step_handler(mes, pizza_order)


@bot.message_handler(commands=['drink'])
def handler_drinks(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton(text='Pepsi')
    btn2 = types.KeyboardButton(text='Coca Cola')
    btn3 = types.KeyboardButton(text='Fanta')
    keyboard.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, 'Choose a drinks', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Pepsi')
def drinks_pepsi(message):
    bot.send_message(message.chat.id, 'Reserved: ' + message.text)


@bot.message_handler(func=lambda message: message.text == 'Coca Cola')
def drinks_cola(message):
    bot.send_message(message.chat.id, 'Reserved: ' + message.text)


@bot.message_handler(func=lambda message: message.text == 'Fanta')
def drinks_fanta(message):
    bot.send_message(message.chat.id, 'Reserved: ' + message.text)


@bot.message_handler(commands=['ik'])
def inline_keyboard(message):
    keyboard = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton('button 1', callback_data='b1')
    b2 = types.InlineKeyboardButton('button 2', callback_data='b2')
    keyboard.add(b1, b2)

    bot.send_message(message.chat.id, 'Choose: ', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'b1')
def f_b1(cl):
    if cl.data == 'b1':
        bot.send_message(cl.message.chat.id, 'Right choice 1')
    elif cl.data == 'b2':
        bot.send_message(cl.message.chat.id, 'Right choice 2')


@bot.message_handler(content_types=['text'])
def test_text(message):
    print(message)

    msg = message.text + ' - this is a text message'
    bot.send_message(message.chat.id, msg)


def pizza_order(message):
    if message.text == 'Pepperoni':
        pn = 123435
    elif message.text == 'Cheesy':
        pn = 1223434

    bot.send_message(message.chat.id, f'Your pizza order: "{message.text}" has been placed! №')


if __name__ == '__main__':
    bot.infinity_polling()
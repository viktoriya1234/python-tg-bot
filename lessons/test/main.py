import telebot
from telebot import types

token = '7391689885:AAGK7dR_-29yZpr3NHfqT8C3RG5srr8cbUM'
bot = telebot.TeleBot(token)

stickers = ['CAACAgIAAxkBAAO3Z0iqLLOSpaCz8_EVHM7uWxrxLD4AAgUAA8A2TxP5al-agmtNdTYE']

# --- BOT MESSAGE ---------------------------------------------------


# команда /start
@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, 'Команда СТАРТ!')


# команда /stop
@bot.message_handler(commands=['stop'])
def command_stop(message):
    bot.send_message(message.chat.id, 'Команда СТОП!')


# кманди: /open, /close
@bot.message_handler(commands=['open', 'close'])
def commands_open_close(message):
    mes = ''

    if message.text == '/open':
        mes = 'Відкрито'
    elif message.text == 'close':
        mes = 'Закрито'

    bot.send_message(message.chat.id, mes)


@bot.message_handler(commands=['key'])
def key_go(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button_1 = types.KeyboardButton(text='Кнопка 1')
    button_2 = types.KeyboardButton(text='Кнопка 2')
    keyboard.add(button_1, button_2)

    bot.send_message(message.chat.id, 'Клавіатура', reply_markup=keyboard)


# Реакція на натискання кнопки
@bot.message_handler(func=lambda message: message.text == 'Кнопка 1')
def handle_button_1(message):
    bot.send_message(message.chat.id, 'Ви натиснули кнопку 1.')


@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    sticker_id = message.sticker.file_id
    emoji = message.sticker.emoji

    bot.reply_to(message, f"Ви надіслали стікер з емоджі {emoji} (ID: {sticker_id})")


# --- Текстові повідомлення ---

@bot.message_handler(content_types=['text'])
def bot_message(message):

    if message.text == '1':
        bot.send_sticker(message.chat.id, stickers[0])
        return True

    mes = message.text + ' - Це просто текст'
    bot.send_message(message.chat.id, mes)


# --- Функції -------------------------------------------------------

# Додаємо кнопки
def bot_buttons(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button_1 = types.KeyboardButton(text='Кнопка 1')
    button_2 = types.KeyboardButton(text='Кнопка 2')
    button_3 = types.KeyboardButton(text='Кнопка 3')
    button_4 = types.KeyboardButton(text='Кнопка 4')
    keyboard.add(button_1, button_2, button_3, button_4)

    msg = bot.send_message(message.chat.id, message.text, reply_markup=keyboard)
    bot.register_next_step_handler(msg, button_if)


def button_if(message):
    if message.text == 'Кнопка 1':

        # ... запустити програму ...
        bot.send_message(message.chat.id, '1. Закопати путіна')
    elif message.text == 'Кнопка 2':
        bot.send_message(message.chat.id, '2. Закопати шойгу')
    else:
        bot.send_message(message.chat.id, '3,4. запустити русоріз')


if __name__ == '__main__':
    bot.polling()

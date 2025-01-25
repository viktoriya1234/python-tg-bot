import time
import threading
import config as c
from SQliteManager import SQLNote
import telebot

bot = telebot.TeleBot(c.BOT_TOKEN)

# === SQLITE =========================================
# db = sqlite3.connect('notebook.db')
# cur = db.cursor()

# cur.execute('''CREATE TABLE users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     chat_id INTEGER NOT NULL,
#     name TEXT DEFAULT 'Unknown',
#     deleted INTEGER DEFAULT 0
#     )''')
# db.commit()
#
# cur.execute('''CREATE TABLE IF NOT EXISTS notes (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     chat_id INTEGER NOT NULL,
#     title TEXT NOT NULL,
#     content TEXT DEFAULT '',
#     notification DATETIME DEFAULT CURRENT_TIMESTAMP,
#     is_send INTEGER DEFAULT 0,
#     deleted INTEGER DEFAULT 0
#     )''')
# db.commit()


# === FUNCTIONS ======================================
def get_bd_cursor():
    return SQLNote(c.DB_NAME)


def send_text_message():
    while True:
        bot.send_message(1793322776, 'something worked')
        time.sleep(10)


def bot_start(message):
    print(message)
    with get_bd_cursor() as cur:
        cur.execute("SELECT chat_id FROM users WHERE chat_id='%d'" % message.chat.id)
        row = cur.fetchone()

        if not row:
            cur.execute(f"INSERT INTO users (chat_id, name) VALUES ('{message.chat.id}', '{message.from_user.username}')")
            bot.send_message(message.chat.id, f'Користувача [{message.from_user.username}] додано!')
        else:
            bot.send_message(message.chat.id, 'Ви вже підписалися на цього бота')

def bot_add_title(message):
    bot.send_message(message.chat.id, 'Нотатку додано!')

# === MESSAGE-HANDLERS ===============================

# start - підписатися
# add - додати
# edit - редагувати
# del - видалити
# all - показати усі нотатки
# help - вивести підказки
# end - відписатися

@bot.message_handler(commands=['start', 'add', 'edit', 'del', 'help', 'end'])
def bot_commands(message):
    if '/start' == message.text:
        bot_start()
    elif '/add' == message.text:
        bot.send_message(message.chat.id, 'Введіть нотатку')
        bot.register_next_step_handler(message, bot_add_title)
    elif '/edit' == message.text:
        pass

@bot.message_handler(content_types=['text'])
def text_massage(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, 'Working!')

if __name__ == '__main__':
    # thread = threading.Thread(target=send_text_message)
    # thread.start()
    bot.infinity_polling()
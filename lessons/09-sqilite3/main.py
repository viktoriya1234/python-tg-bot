import time
import threading
import config
import telebot
import sqlite3

bot = telebot.TeleBot(config.BOT_TOKEN)

# === SQLITE =========================================
db = sqlite3.connect('notebook.db')
cur = db.cursor()

# cur.execute('''CREATE TABLE user (
#     id INTEGER PRIMARY KEY,
#     chat_id INTEGER NOT NULL,
#     name TEXT DEFAULT 'Unknown',
#     email TEXT DEFAULT '',
#     deleted INTEGER DEFAULT 0
#     )''')
# db.commit()
# === FUNCTIONS ======================================

def send_text_message():
    while True:
        bot.send_message(1793322776, 'something worked')
        time.sleep(10)

# === MESSAGE-HANDLERS ===============================
@bot.message_handler(commands=['start'])
def bot_start(message):
    cur.execute("SELECT chat_id FROM user")
    row = cur.fetchone()
    if not row:
        cur.execute(F"INSERT INTO user (chat_id, name) VALUES ({message.chat.id}, {message.from_user.username})")
        db.commit()

    bot.send_message(message.chat.id, f'Користувача [{message.from_user.username}]')


@bot.message_handler(content_types=['text'])
def text_massage(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, 'Working!')

if __name__ == '__main__':
    # thread = threading.Thread(target=send_text_message)
    # thread.start()
    bot.infinity_polling()
import telebot

token = '7673939553:AAEVET8kWs7QFanPR8YiZVHHQFuZNjdEjYo'
bot = telebot.TeleBot(token)

def is_int(v):
    try:
        int(v)
        return True
    except ValueError:
        return False


@bot.message_handler(content_types=['text'])
def is_text(message):
    if not is_int(message.text):
        filename = "bot_text.txt"
    else:
        filename = "bot_number.txt"

    with open(filename, 'a') as file:
        file.write(message.text + '\n')

    bot.send_message(message.chat.id, 'saved to file!')


if __name__ == '__main__':
    bot.polling()
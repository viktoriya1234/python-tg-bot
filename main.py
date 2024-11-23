import telebot

token = '7673939553:AAEVET8kWs7QFanPR8YiZVHHQFuZNjdEjYo'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def test_text(message):
    print(message)

    msg = message.text + ' - this is a text message'
    bot.send_message(message.chat.id, msg)

if __name__ == '__main__':
    bot.polling()
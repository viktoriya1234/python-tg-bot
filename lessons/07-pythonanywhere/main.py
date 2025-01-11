import telebot

token = '7673939553:AAEVET8kWs7QFanPR8YiZVHHQFuZNjdEjYo'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def is_text(message):
    bot.send_message(message.chat.id, message.text + '\n[Bot is working!]')


if __name__ == '__main__':
    bot.polling()
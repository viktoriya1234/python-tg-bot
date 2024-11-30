# Заняття 2

### Обробка повідомлень, клавіатура

### [&#8678; Зміст](../index.md)

---

### Обробка повідомлень

> Функція __message_handler__ використовується для обробки різних 
повідомлень від користувачів Telegram.

Основні параметри:

__commands__: Список команд, які повинні оброблятися (наприклад, /start, /stop).

```python
@bot.message_handler(commands=['start', 'stop'])
def handle_command(message):
    bot.reply_to(message, "Це відповідь на команду ...")
```

__content_types__: Типи контенту, які повинні оброблятися (наприклад, text, photo, document).

```python
@bot.message_handler(content_types=['text'])
def handle_content_type(message):
    bot.reply_to(message, "Це текст.")
```

__regexp__: Регулярний вираз, за яким буде оброблятися повідомлення.

```python
@bot.message_handler(regexp='^/repeat (.*)')
def handle_regexp(message):
    bot.reply_to(message, message.text)
```

__func__: Функція, яка повинна повернути True, якщо повідомлення має бути оброблено.

```python
@bot.message_handler(func=lambda message: message.text is not None and 'hello' in message.text.lower())
def handle_custom_function(message):
    bot.reply_to(message, "Привіт!")
```

__chat_types__: Типи чатів, у яких має оброблятися повідомлення (наприклад, private, group, supergroup, channel).

```python
@bot.message_handler(chat_types=['private'])
def handle_private_chat(message):
    bot.reply_to(message, "Це повідомлення з приватного чату.")
```

Послідовність виклику функцій message_handler з різними параметрами має значення. 
Обробники повинні бути розташовані в такій послідовності, 
щоб уникнути конфліктів та забезпечити, що повідомлення обробляються належним чином.

### Клавіатура

Telegram Bot API: [Available types](https://core.telegram.org/bots/api#available-types)

Клавіатури в Telegram ботах – це зручний інструмент для взаємодії з користувачем. 
Вони дозволяють користувачеві вибрати одну з запропонованих опцій, 
замість того, щоб вводити текст вручну. 
Це спрощує використання бота і робить його більш інтуїтивним.

#### Типи клавіатур в PyTelegramBotAPI:

- ReplyKeyboardMarkup: Класична клавіатура, яка замінює стандартну клавіатуру чату.
- InlineKeyboardMarkup: Інтерактивна клавіатура, кнопки якої можуть виконувати різні дії, наприклад, викликати інші команди або відкривати URL.

Проста клавіатура (__ReplyKeyboardMarkup__)

1. Імпортуємо необхідні модулі:

```python
...
from telebot import types
```

2. Створюємо клавіатуру:

```python
#  створюємо об'єкт клавіатури.
my_buttons = types.ReplyKeyboardMarkup()
# створюємо окрему кнопку.
btn1 = types.KeyboardButton('Кнопка 1')
btn2 = types.KeyboardButton('Кнопка 2')
# додаємо кнопки до клавіатури.
my_buttons.add(btn1, btn2)
```

3. Відправити повідомлення з клавіатурою:

```python
bot.send_message(chat_id=YOUR_CHAT_ID, text="Виберіть опцію:", reply_markup=my_buttons)
```

Приклад повного коду:

```python
import telebot
from telebot import types

bot = telebot.TeleBot('YOUR_TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    my_buttons = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Кнопка 1')
    btn2 = types.KeyboardButton('Кнопка 2')
    my_buttons.add(btn1, btn2)
    bot.send_message(message.chat.id, "Виберіть опцію:", reply_markup=my_buttons)

bot.polling()
```

#### Опрацювання натиснутої кнопки

```python
@bot.message_handler(commands=['start'])
def botbutton(message):
    my_buttons = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Кнопка 1')
    btn2 = types.KeyboardButton('Кнопка 2')
    my_buttons.add(btn1, btn2)

    msg = bot.send_message(message.chat.id, message.text + ' .. Працює!', reply_markup=my_buttons)
    # Реєструємо функцію my_bot_message яка спрацює після (натискання кнопки) отримання сповіщення 
    bot.register_next_step_handler(msg, my_bot_message)

def my_bot_message(message):
    if message.text == 'Кнопка 1':
        bot.send_message(message.chat.id, 'натиснута кнопка 1')
    elif message.text == 'Кнопка 2':
        bot.send_message(message.chat.id, 'натиснута кнопка 2')
```


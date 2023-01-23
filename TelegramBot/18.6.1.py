import telebot
from config import keys, TOKEN
from extensions import APIException, CurrencyConverter
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты цену которой хотите узнать>\
    <имя валюты в которой надо узнать цену первой валюты> \
    <количество первой валюты>\nУвидеть список всех доступных валют: /values"
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def help(message: telebot.types.Message):
    text = "Доступные валюты: "
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")

        if len(values) > 3:
            raise APIException("Слишком много параметров.")
        elif len(values) < 3:
            raise APIException("Мало параметров.")

        from_currency, to_currency, amount = values
        total_amount = CurrencyConverter.get_price(from_currency, to_currency, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка пользователя\n{e}")
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {from_currency} в {to_currency} - {total_amount}'
        bot.send_message(message.chat.id, text)

bot.polling()
import telebot

#1529055221:AAEBlhH6VZBhtJeYZHsjlwyRfWPOXBDhwtA

bot = telebot.TeleBot("", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Что вас интересует? Если вас интересует платный курс iOS, напишите \"iOS\". Если вас интересует бесплатный курс по Web Development напишите \"Web Development\".")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == "iOS":
        bot.reply_to(message, 'Стоимость $500 в месяц. Средняя стоимость онлайн курсов с ментором в США стартует от $1000 в месяц и выше. Возможны дополнительные траты, такие как, выплаты определенных % от заработной платы в течение 6-12 месяцев после трудоустройства. У нас фиксированная цена, опытный и терпеливый ментор. Наша миссия - через образование дать реальную возможность иммигрантам всего за 1 год - сменить социальный статус, заработок и условия труда, освободить их потенциал для решения всех потребностей и реализации всех желаний.')
    elif message.text == 'Web Development':
        bot.reply_to(message, 'Это соц проект. Стартуем скоро. От вас требуется желание и ноутбук')
    

bot.polling()


import telebot
token = ('1630599526:AAHlxgufHKr1Kq8o986kvfPYoC71YBQsNNM')
bot = telebot.TeleBot(token)

# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	pass

# Handles all sent documents and audio files
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
	pass

# Handles all text messages that match the regular expression
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
	pass


import telebot

BOT_TOKEN = '1630599526:AAHlxgufHKr1Kq8o986kvfPYoC71YBQsNNM'
bot = telebot.TeleBot(BOT_TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('iOS course', 'Web Development', 'Ask Questions', 'Bazar zhok')


@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Выбери', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text.lower() == 'iOS course':
		bot.send_message(message.chat.id,
						 'Узнайте больше о iOS курсах по ссылке  : http://refpasutmf.space/L?tag=s_140657m_25519c_&site=140657&ad=25519',
						 reply_markup=keyboard1)

	elif message.text.lower() == 'Web Development':
		bot.send_message(message.chat.id,
						 'Web Development : http://refpapvvru.space/L?tag=s_142465m_21499c_&site=142465&ad=21499',
						 reply_markup=keyboard1)

	elif message.text.lower() == 'Ask Questions':
		bot.send_message(message.chat.id, 'Промокод: Luckyman')
		bot.send_message(message.chat.id, 'Регистрация: https://bit.ly/39ppj6c', reply_markup=keyboard1)

	elif message.text.lower() == 'Bazar zhok':
		bot.send_message(message.chat.id, 'Регистрация: https://bit.ly/39r1j2G', reply_markup=keyboard1)

bot.polling(none_stop=True, interval=0)
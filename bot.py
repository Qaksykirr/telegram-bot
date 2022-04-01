#библиотеки, которые загружаем из вне
import telebot
TOKEN = '5139422518:AAFUV3DmfSnbLxbJTzdiyQ8mRM349crJuS8'

ITEM_REPOSITORY = '🧡 Мой репозиторий'
ITEM_WRITE_TO_ME = '😋 Написать мне в личку'
ITEM_SITE = '🤓 Ссылка на мой сайт'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton(ITEM_REPOSITORY)
	item2 = types.KeyboardButton(ITEM_WRITE_TO_ME)
	item3 = types.KeyboardButton(ITEM_SITE)

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Привет тебе от краба, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['cat'])
def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	bot.send_message(message.chat.id, "Вы нашли секретный раздел бота! Котеек в студию!\nhttps://genrandom.com/ru/cats/", 
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	MESSAGE = '';

	if message.chat.type == 'private':
		if message.text == ITEM_REPOSITORY:
			MESSAGE = 'https://github.com/Qaksykirr'
		elif message.text == ITEM_WRITE_TO_ME:
			MESSAGE = 'http://t.me/xenia_krw'
		elif message.text == ITEM_SITE:
			MESSAGE = 'http://about-xenia-kireeva.ru'
		else:
			MESSAGE = "Не знаю что ответить 😢"

	bot.send_message(message.chat.id, MESSAGE);

bot.polling(none_stop=True)

#https://core.telegram.org/bots/api#available-methods
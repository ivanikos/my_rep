import requests, telebot, os



bot = telebot.TeleBot('1265062548:AAFqYKSGzXqCmAANEPfEN02SGj69rs9PLPA')

@bot.message_handler(commands=['start'])

def start_command(message):
	#sent = bot.send_message(message.chat.id, 'Привет, ' + str(message.from_user.username) + '!')
	if message.from_user.id == 799592984:
		bot.send_message(message.chat.id, 'Приветствую, Повелитель!')
	elif message.from_user.id == 866390238:
		photo = open('Belye-lilii-2.jpg', 'rb')
		bot.send_message(message.chat.id, 'Привет, Алёнка! Иван, мой создатель и повелитель, приказал \n'+
						 ' мне приветствовать тебя как особую гостью!)) Я, правда, пока что почти ничего не умею\n'+
						 'Чтобы узнать каким командам я обучен, набери /help')
		bot.send_photo(message.chat.id, photo)
	else:
		bot.send_message(message.chat.id, 'Привет! Я пока что пытаюсь научиться говорить тебе погоду в твоем городе)) \n'
					 + 'чтобы протестировать эту функцию набери /погода')

@bot.message_handler(commands=['help'])
def help_command(message):
	keyboard = telebot.types.InlineKeyboardMarkup()
	keyboard.add(telebot.types.InlineKeyboardButton(
		'Написать разработчику', url='telegram.me/ivanikos'
	))
	bot.send_message(message.chat.id, '1. Чтобы узнать погоду в интересующем тебя городе напиши /weather\n\n'+
									  'Пока что все, но я быстро учусь)',
					 reply_markup=keyboard)

@bot.message_handler(commands=['weather'])
def weather(message):
	msg = bot.reply_to(message, 'Погоду в каком городе хочется тебе знать?')
	bot.register_next_step_handler(msg, weather_ans)

def weather_ans(message):
	try:
		chat_id = message.chat.id
		city = message.text
		res = requests.get(
			f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=896831eabcb093fc849059be7ffbff60')
		data = res.json()
		city_info = {
			'temp': data["main"]["temp"],
			'icon': data["weather"][0]["icon"]
		}
		bot.send_message(message.from_user.id, f'В городе {city.capitalize()} температура {data["main"]["temp"]} градусов, '+
											   f'ощущается как {data["main"]["feels_like"]}\n'+
											   f'Ветер {data["wind"]["speed"]} м/с')
		#bot.send_photo(message.from_user.id, f'{photo} иконка должна быть')
	except Exception as err:
		bot.reply_to(message, 'Извини, что-то пошло не так :(')

@bot.message_handler(content_types=	['text'])
def handle_text_messages(message):

	if message.text.lower() == 'привет':
		bot.send_message(message.from_user.id, 'Привет')
	elif message.text.lower() == 'кто ты?':
		bot.send_message(message.from_user.id, 'Я бот для теста, просто попробовать')
	elif message.text.lower() == 'что ты умеешь?':
		bot.send_message(message.from_user.id, 'Скоро я буду много чего уметь! Вот увидишь!')
	else:
		bot.send_message(message.from_user.id, 'Непонятно ничего, набери /help')

bot.polling(none_stop=True, interval=0)






"""res = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?id=1496511&units=metric&appid=896831eabcb093fc849059be7ffbff60')
data = res.json()
city_info = {
        'city': 'Новый Уренгой',
        'temp': data["main"]["temp"],
        'icon': data["weather"][0]["icon"]
        }
print(city_info)"""








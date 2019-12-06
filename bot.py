import telebot
import random
import pyowm

greetings = ["Привет", "Здравствуй"]
how_are_you = ["Отлично", "Ужасно", "Хорошо"]

token ="THERE_SHOULD_BE_TOKEN"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["weather"])
def weather(message):
    city = bot.send_message(message.chat.id, "В каком городе Вам показать погоду?")
    bot.register_next_step_handler(city, weath)

def weath(message):
    owm = pyowm.OWM("THERE_SHOULD_BE_TOKEN")
    city = message.text
    weather = owm.weather_at_place(city)
    w = weather.get_weather()
    temperature = w.get_temperature("celsius")["temp"]
    wind = w.get_wind()["speed"]
    hum = w.get_humidity()
    desc = w.get_detailed_status()
    bot.send_message(message.chat.id, "Сейчас в городе " + str(city) + " " + str(desc) + ", температура - " + str(temperature) + "°C, влажность - " + str(hum) + "%, скорость ветра - " +str(wind) + "м/с.")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, " + message.chat.first_name + ", я бот, который может рассказать тебе о погоде в твоём городе.")

@bot.message_handler(content_types=["text"])
def main(message):
    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.chat.id, random.choice(greetings) + ", " + message.chat.first_name)
    elif message.text == "Как дела?":
        bot.send_message(message.chat.id, random.choice(how_are_you))

@bot.message_handler(commands=["weather"])
def weather(message):
    city = bot.send_message(message.chat.id, "В каком городе Вам показать погоду?")
    bot.register_next_step_handler(city, weath)

def weath(message):
    owm = pyowm.OWM("THERE_SHOULD_BE_TOKEN", language="ru")
    city = message.text
    weather = owm.weather_at_place(city)
    w = weather.get_weather()
    temperature = w.get_temperature("celsius")["temp"]
    wind = w.get_wind()["speed"]
    hum = w.get_humidity()
    desc = w.get_detailed_status()
    bot.send_message(message.chat.id, "Сейчас в городе " + str(city) + " " + str(desc) + ", температура - " + str(temperature) + "°C, влажность - " + str(hum) + "%, скорость ветра - " +str(wind) + "м/с.")

if __name__ == "__main__":
    bot.polling(none_stop=True)

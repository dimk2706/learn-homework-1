"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging, ephem
import settings
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'settings.PROXY_USERNAME',
        'password': 'settings.PROXY_PASSWORD'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def greet_user_planet(update, context):
    dt_now = datetime.today().date()        #Получение сегодняшней даты
    dt_now=str(dt_now)
    dt_now=dt_now.replace("-", "/")
    user_text = update.message.text.split() #Разбиение сообщения от пользователя
    if user_text[1]=="Mercury":             #В зависимости от введенной пользователем планеты выведется соответствующее сообщение
      planet = ephem.Mercury(dt_now)
      constellation = f"Планета Меркурий сегодня находится в созвездии: {ephem.constellation(planet)[1]}"
    elif user_text[1]=="Venus":
      planet = ephem.Venus(dt_now)
      constellation = f"Планета Венера сегодня находится в созвездии: {ephem.constellation(planet)[1]}"
    elif user_text[1]=="Mars":
      planet = ephem.Mars(dt_now)
      constellation = f"Планета Марс сегодня находится в созвездии: {ephem.constellation(planet)[1]}"
    elif user_text[1]=="Jupiter":
      planet = ephem.Jupiter(dt_now)
      constellation = f"Планета Юпитер сегодня находится в созвездии: {ephem.constellation(planet)[1]}"
    elif user_text[1]=="Saturn":
      planet = ephem.Saturn(dt_now)
      constellation = f"Планета Сатурн сегодня находится в созвездии: {ephem.constellation(planet)[1]}"
    elif user_text[1]=="Uranus":
      planet = ephem.Uranus(dt_now)
      constellation = f"Планета Уран сегодня находится в созвездии: {ephem.constellation(planet)[1]}"
    elif user_text[1]=="Neptune":
      planet = ephem.Neptune(dt_now)
      constellation = f"Планета Нептун сегодня находится в созвездии: {ephem.constellation(planet)[1]}"
    elif user_text[1]=="Pluto":
      planet = ephem.Pluto(dt_now)
      constellation = f"Плутон сегодня находится в созвездии: {ephem.constellation(planet)[1]}"
    else:
       constellation = "Некорректно введено название планеты."
    print(constellation)
    update.message.reply_text(constellation)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)



def main():
    #mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)  Закомментировал так как у меня выдает ошибку при попытке использовать прокси
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", greet_user_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

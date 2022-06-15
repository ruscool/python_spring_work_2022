# import psycopg2 as ps
import telebot
import requests
from my_token import TOKEN
from telebot import types
from motor_bot import DB, Dbquerry, Key_bot, Weather
from connect_db import name, user, password

bot = telebot.TeleBot(TOKEN)
all_for_result = []


# Bot menu
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    buttons = cl_menu_keyboard.start_menu()
    # bot.send_message(message.chat.id, message) # for test
    bot.send_message(message.chat.id, f"{message.from_user.first_name}, добро пожаловать в ТестСистем")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(*buttons)
    bot.send_message(message.chat.id, 'Начнем тестирование - выберите Тест',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mes(message):
    quest = 1
    if message.text == 'Тест':
        menu_key_1 = cl_menu_keyboard.how_much()
        keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard3.add(*menu_key_1)
        bot.send_message(message.chat.id, f'Из скольки вопросов будет тест?', reply_markup=keyboard3)
    elif message.text == '3':
        button1 = cl_menu_keyboard.back()
        keyboard_back = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button1)
        cycle(message, quest, keyboard_back)
        # сюда метод показа вопроса с ответами из класса
    elif message.text == '5':
        button1 = cl_menu_keyboard.back()
        keyboard_back = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button1)
        cycle(message, quest, keyboard_back)
    elif message.text == '10':
        button1 = cl_menu_keyboard.back()
        keyboard_back = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button1)
        cycle(message, quest, keyboard_back)
    elif message.text == 'Статистика':
        bot.send_message(message.chat.id, 'Извините - в разработке :)')
        with open('test_system.pdf', 'rb') as f:
            image = f.read()
        bot.send_photo(message.chat.id, image)
    elif message.text == 'Погода в Спб':
        loc_me = Weather()
        gradus = loc_me.weather()
        gradus = float('{:.1f}'.format(gradus))
        printing = f'Температура в Санкт Петербурге {gradus}°'
        bot.send_message(message.chat.id, printing)
    elif message.text == 'Назад':  # доработать - останов и сохранение данных в БД для продолжения
        buttons = cl_menu_keyboard.back_menu()
        key_back_menu = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*buttons)
        bot.send_message(message.chat.id, "Вы хотите выйти из теста?\n...", reply_markup=key_back_menu)  # not finished

    elif message.text == 'Продолжить':
        bot.send_message(message.chat.id, "Доделать переход")
    elif message.text == 'Новый тест':
        bot.send_message(message.chat.id, "Данные теста потеряны...\n\nДобро пожаловать в ТестСистем")
        buttons = cl_menu_keyboard.start_menu()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(*buttons)
        bot.send_message(message.chat.id, 'Из скольки вопросов будет тест?', reply_markup=markup)

        # bot.send_message(message.chat.id, message) # print all in text - verify


def cycle(message, quest, keyboard_back):
    bot.send_message(message.chat.id, f'Вопрос {quest}', reply_markup=keyboard_back)
    q_list = cl_querry.question_list(5)
    print(q_list)
    for_view = cl_querry.answers_and_question()
    print(for_view)
    bot.send_message(message.chat.id, q_list[0][1])
    l_num = []
    res_login = for_view[2:]
    # print(res_login)
    keyboard_li = types.InlineKeyboardMarkup()
    for i in res_login[0]:
        in_menu = f'{i[1]}'
        l_num.append(in_menu)
        menu_answer = types.InlineKeyboardButton(text=f'{in_menu}', callback_data='1')
        keyboard_li.add(menu_answer)
    bot.send_message(message.chat.id, f'Выберите ответ', reply_markup=keyboard_li)
    bot.reply_backend


def choice_answer():
    pass


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == '1':
        bot.send_message(call.message.chat.id, f'Ответ принят -/доделать')
        # bot.reply_backend
        # bot.callback_query_handler()


# bot.polling(non_stop=True)
if __name__ == '__main__':
    test_db = DB(name, user, password)
    cl_querry = Dbquerry()
    cl_menu_keyboard = Key_bot()
    db = test_db.get_connection()
    bot.polling(non_stop=True)

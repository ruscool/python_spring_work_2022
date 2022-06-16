# import psycopg2 as ps
import requests
import telebot
from my_token import TOKEN
from telebot import types
from motor_bot import DB, Dbquerry, Key_bot, Weather, Logger, Cycles
from connect_db import name, user, password

bot = telebot.TeleBot(TOKEN)


# Bot menu
@bot.message_handler(commands=['start'])
def send_welcome(message):
    buttons = cl_menu_keyboard.start_menu()
    # bot.send_message(message.chat.id, message)  # for test
    bot.send_message(message.chat.id, f"{message.from_user.first_name}, добро пожаловать в ТестСистем")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(*buttons)
    bot.send_message(message.chat.id, 'Начнем тестирование - выберите Тест',
                     reply_markup=markup)


@bot.message_handler(commands=['help'])
def helper():
    pass


@bot.message_handler(content_types=['text'])
def mes(message):
    quest = 1
    if message.text == 'Тест':
        tempo = logger.verification_id(message.from_user.id)
        if tempo == 1:
            buttons = cl_menu_keyboard.back_menu()
            key_back_menu = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*buttons)
            bot.send_message(message.chat.id, "Есть тест который проходили раньше", reply_markup=key_back_menu)
        else:
            menu_key_1 = cl_menu_keyboard.how_much()
            keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard3.add(*menu_key_1)
            bot.send_message(message.chat.id, f'Из скольки вопросов будет тест?', reply_markup=keyboard3)
    elif message.text == '3':
        q = 3
        temp_q = logger.insert_question(q)
        button1 = cl_menu_keyboard.back()
        keyboard_back = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*button1)
        cycle(message, keyboard_back, q)
        # сюда метод показа вопроса с ответами из класса
    elif message.text == '5':
        q = 5
        temp_q = logger.insert_question(q)
        button1 = cl_menu_keyboard.back()
        keyboard_back = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*button1)
        cycle(message, keyboard_back, q)
    elif message.text == '10':
        q = 10
        temp_q = logger.insert_question(q)
        button1 = cl_menu_keyboard.back()
        keyboard_back = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*button1)
        cycle(message, keyboard_back, q)
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
    elif message.text == 'Следующий вопрос':
        q = logger.questions_left(message.from_user.id)
        q = list(q)
        q = q[0]
        button1 = cl_menu_keyboard.back()
        keyboard_back = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*button1)
        cycle(message, keyboard_back, q)
        # bot.send_message(message.chat.id, "Следующий вопрос")
    elif message.text == 'Меню':
        bot.send_message(message.chat.id, "menu")

    elif message.text == 'Продолжить':
        bot.send_message(message.chat.id, "Доделать переход")
    elif message.text == 'Новый тест':
        bot.send_message(message.chat.id, "Данные теста потеряны...\n\nДобро пожаловать в ТестСистем")
        res = logger.new_test(message.from_user.id)
        buttons = cl_menu_keyboard.start_menu()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(*buttons)
        bot.send_message(message.chat.id, 'Начнем тестирование - выберите Тест', reply_markup=markup)

        # bot.send_message(message.chat.id, message) # print all in text - verify


# @bot.message_handler()
def cycle(message, keyboard_back, id_question):
    check = logger.verify_check()
    check = check[0]
    quest = 1
    print('verify', check)
    bot.send_message(message.chat.id, f'Вопрос {quest}', reply_markup=keyboard_back)
    l_num = []
    print(f'message = {message}')
    q_list = cl_querry.question_list(id_question)  # in DB
    quest_in_db = logger.insert_number_question(quest)
    print(q_list)
    for_view = cl_querry.answers_and_question()
    print(f'вопросы = {for_view}')
    bot.send_message(message.chat.id, q_list[0][1])
    res_login = for_view[2:]
    keyboard_li = types.InlineKeyboardMarkup()
    for i in res_login[0]:
        in_menu = f'{i[1]}'
        l_num.append(in_menu)
        l_num.append(i[3])
        if i[3] == 1:
            logger.save_number_quiestion(i[2], i[0])

        menu_answer = types.InlineKeyboardButton(text=f'{in_menu}', callback_data=f'{i[2]}_{i[0]}')
        keyboard_li.add(menu_answer)
    # for_next = bot.send_message(message.chat.id, f'Выберите ответ', reply_markup=keyboard_li)
    bot.send_message(message.chat.id, f'Выберите ответ', reply_markup=keyboard_li)
    print(l_num)
    quest += 1
    check = 1
    id_question -= 1


@bot.callback_query_handler(func=lambda call: True, )
def callback_worker(call):
    print(f'call= {call.data}')
    if call.data != 'callback_worker':
        # wq = cycle(None, None, None, None, 'callback_worker')  # на память
        q_answer = str(call.data)
        q_answer = list(q_answer.split('_'))
        answer = q_answer[1]
        q_answer = q_answer[0]
        print()
        q_in_db = logger.for_answers()
        if q_in_db is None:
            bot.send_message(call.message.chat.id, f'Введите ответ')
        if q_answer == q_in_db:
            bot.send_message(call.message.chat.id, f'Ответ на данный вопрос уже был')
        else:
            ans_in_db = logger.save_answer(answer)
            down = logger.down()
            print(f'down {down}')
            bot.send_message(call.message.chat.id, f'Ответ принят')
            # bot.register_next_step_handler(dd,mes)


# bot.polling(non_stop=True)
if __name__ == '__main__':
    test_db = DB(name, user, password)
    conn = test_db.get_connection()
    cl_querry = Dbquerry()
    logger = Logger(conn)
    cl_menu_keyboard = Key_bot()
    # db = test_db.get_connection()
    bot.polling(non_stop=True)

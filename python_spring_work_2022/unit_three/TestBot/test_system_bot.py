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
def helper(message):
    buttons = cl_menu_keyboard.start_menu()
    # bot.send_message(message.chat.id, message)  # for test
    bot.send_message(message.chat.id, f"{message.from_user.first_name}, добро пожаловать в ТестСистем")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(*buttons)
    bot.send_message(message.chat.id, "В разработке...", reply_markup=markup)


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
        temp_q = logger.insert_question(q, message.chat.id)
        button1 = cl_menu_keyboard.back()
        keyboard_back = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*button1)
        cycle(message, keyboard_back, q)
        # сюда метод показа вопроса с ответами из класса
    elif message.text == '5':
        q = 5
        temp_q = logger.insert_question(q, message.chat.id)
        button1 = cl_menu_keyboard.back()
        keyboard_back = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*button1)
        cycle(message, keyboard_back, q)
    elif message.text == '10':
        q = 10
        temp_q = logger.insert_question(q, message.chat.id)
        button1 = cl_menu_keyboard.back()
        keyboard_back = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*button1)
        cycle(message, keyboard_back, q)
    elif message.text == 'Статистика':
        stat = logger.for_statistic(message.chat.id)
        if len(stat) == 0:
            bot.send_message(message.chat.id, f'У <b>Вас</b> еще нет данных по статистике', parse_mode='html')
        else:
            bot.send_message(message.chat.id,
                             f'<b>Статистика</b>\n\n{message.from_user.first_name}, Вы сдавали Тест <b>{stat[0][0]}</b> раз,'
                             f' из них успешно <b>{stat[0][1]}</b>\n\nКрайний раз результаты теста - '
                             f'правильных ответов <b>{stat[0][2]}</b> из <b>{stat[0][3]}</b>', parse_mode="html")

        # with open('test_system.pdf', 'rb') as f:
        #     image = f.read()
        # bot.send_photo(message.chat.id, image)
    elif message.text == 'Погода в Спб':
        loc_me = Weather()
        gradus = loc_me.weather()
        gradus = float('{:.1f}'.format(gradus))
        printing = f'Температура в Санкт Петербурге {gradus}°'
        bot.send_message(message.chat.id, printing)
    elif message.text == 'Назад':  # доработать - останов и сохранение данных в БД для продолжения
        # qww = 1
        buttons = cl_menu_keyboard.back_menu()
        key_back_menu = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*buttons)
        bot.send_message(message.chat.id, "Вы хотите выйти из теста?\n...", reply_markup=key_back_menu)  # not finished
    elif message.text == 'Следующий вопрос':
        q = logger.questions_left(message.from_user.id)
        end_quest = logger.for_end_test_per(message.from_user.id)
        # print(f'q ={q} , what quest = {end_quest}')
        num_quest = logger.end_test(message.from_user.id)
        # print(num_quest, 'num_quest')
        if q > 0:
            button1 = cl_menu_keyboard.back()
            keyboard_back = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*button1)
            cycle(message, keyboard_back, q)
        elif q == 0:
            button = cl_menu_keyboard.end_test()
            keyboard_back = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button)
            end_test(message, keyboard_back)
    elif message.text == 'Завершить тест':  # переход с конца теста в начало бота
        bot.send_message(message.chat.id, "Результаты теста")
        res = logger.new_test(message.from_user.id)
        buttons = cl_menu_keyboard.start_menu()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(*buttons)
        bot.send_message(message.chat.id, 'Начнем тестирование - выберите Тест', reply_markup=markup)
    elif message.text == 'Продолжить':
        q = logger.questions_left(message.from_user.id)
        last_quest = logger.last_question(message.from_user.id)
        button1 = cl_menu_keyboard.back()
        keyboard_back = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*button1)
        cycle(message, keyboard_back, q, last_quest)

        # bot.send_message(message.chat.id, "Доделать переход")
    elif message.text == 'Новый тест':
        bot.send_message(message.chat.id, "Данные теста потеряны...\n\nДобро пожаловать в ТестСистем")
        res = logger.new_test(message.from_user.id)
        buttons = cl_menu_keyboard.start_menu()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(*buttons)
        bot.send_message(message.chat.id, 'Начнем тестирование - выберите Тест', reply_markup=markup)
    elif message.text == 'Выйти':
        bot.send_message(message.chat.id, "Можете продолжить позже")
        res = logger.new_test(message.from_user.id)
        buttons = cl_menu_keyboard.start_menu()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(*buttons)
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)


def end_test(message, keyboard_back):
    plus = 0
    list_answers = logger.result_plus(message.chat.id)
    len_answers = len(list_answers)
    sum_list = sum(list_answers)
    test = 'Не сдан'
    try:
        if sum_list * 100 / len_answers >= 60:
            test = 'Сдан'
    except:
        test = 'Не сдан'

    # print(f'{list_answers} {len_answers}')
    bot.send_message(message.chat.id,
                     f'Результаты теста\n\nПравильных ответов {sum_list} из {len_answers}\n\nТест {test}',
                     reply_markup=keyboard_back)
    save_statistic = logger.save_statistic(sum_list, len_answers, message.chat.id, test)
    return 0


# @bot.message_handler()
def cycle(message, keyboard_back, id_question, last_quest=0):
    # check = logger.verify_check()
    # check = check[0]
    all_res = []
    quest = logger.quest_count(message.chat.id)
    for_one = []
    if int(last_quest) > 0:
        # print(f'last_q= {last_quest}')
        all_res = logger.one_and_last_quest(last_quest)
        quest = logger.for_end_test_per(message.chat.id)
        for_one.append(quest)
        last_quest = 0
        # print(f'last_q= {last_quest}')

    bot.send_message(message.chat.id, f'Вопрос {quest}', reply_markup=keyboard_back)
    l_num = []

    q_list = cl_querry.question_list(id_question)  # in DB
    quest_in_db = logger.insert_number_question(quest, message.chat.id)

    for_view = cl_querry.answers_and_question()
    # print(for_view)
    bot.send_message(message.chat.id, q_list[0][1])
    # insert func - find last question + last quest {}
    res_login = []
    res_login = all_res
    res_login = for_view[2:]
    keyboard_li = types.InlineKeyboardMarkup()
    for i in res_login[0]:
        # str_i = 'qu'
        # if len(i[1]) > 50:
        #     str_i = str(i[1])
        #     str_i = str_i[:50] + '\n' + str_i[50:]
        # else:
        #     str_i = i[1]
        in_menu = f'{i[1]}'
        # print(f'{i[0]}, {len(i[1])}')
        l_num.append(in_menu)
        l_num.append(i[3])
        if i[3] == 1:
            logger.save_number_quiestion(i[2], i[0], message.chat.id)
        menu_answer = types.InlineKeyboardButton(text=f'{in_menu}', callback_data=f'{i[2]}_{i[0]}', )
        keyboard_li.add(menu_answer)
    # for_next = bot.send_message(message.chat.id, f'Выберите ответ', reply_markup=keyboard_li)
    bot.send_message(message.chat.id, f'Выберите ответ', reply_markup=keyboard_li)

    quest += 1
    logger.save_count_quest(quest)
    check = 1
    id_question -= 1
    return 'Тест'


@bot.callback_query_handler(func=lambda call: True, )
def callback_worker(call):
    # print(f'call= {call.data}')
    if call.data != 'callback_worker':
        # wq = cycle(None, None, None, None, 'callback_worker')  # на память
        # print('call data ', call.data)
        q_answer = str(call.data)
        q_answer = list(q_answer.split('_'))
        answer = int(q_answer[1])
        q_answer = int(q_answer[0])
        q_in_db = logger.for_answers(call.from_user.id)
        ans_in_db = logger.save_answer(answer, call.from_user.id)
        bot.send_message(call.message.chat.id, f'Ответ принят')


# bot.polling(non_stop=True)
if __name__ == '__main__':
    test_db = DB(name, user, password)
    conn = test_db.get_connection()
    cl_querry = Dbquerry()
    logger = Logger(conn)
    cl_menu_keyboard = Key_bot()
    # db = test_db.get_connection()
    bot.polling(non_stop=True)

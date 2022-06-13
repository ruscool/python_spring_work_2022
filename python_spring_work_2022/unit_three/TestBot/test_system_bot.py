import psycopg2 as ps
import telebot
from telebot import types
import requests

TOKEN = "5333165895:AAFo9AFI53d92ZzcRZGO6X5ClqKS9BgTggg"
bot = telebot.TeleBot(TOKEN)


class DB:
    """
    Это документация класса
    """
    __instance__ = None

    # __slots__ = ['name', 'user', 'password', 'conn']

    def __new__(cls, *args, **kwargs):
        if not cls.__instance__:
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    def __init__(self):
        self.name = 'testsystem'
        self.user = 'testsystem'
        self.password = "1234test"

    def get_connection(self) -> list:
        """
        Это документация метода get_connection
        :return: соединение с БД
        """
        with ps.connect(f"dbname={self.name} user={self.user} password={self.password}") as self.conn:
            with self.conn.cursor() as cur:
                cur.execute(f"""SELECT * FROM test LIMIT 3;
                    """)
                res = cur.fetchall()
                # print(f'.38 {res}')
        return self.conn


def question_list():
    conn = db
    with conn.cursor() as cur:
        cur.execute("""select * from question q order by random() limit 10;""")
        result = cur.fetchall()
        return result


# class Main:
#     def __init__(self):
#         start = DB()
#         self.db = start.get_connection()


# Bot menu
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать в ТестСистем")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Тест')
    button_2 = types.KeyboardButton('Статистика')
    button_3 = types.KeyboardButton('Погода в Спб')
    markup.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id, 'Начнем тестирование - выберите Тест\n(Будет задано 10 вопросов)',
                     reply_markup=markup)


def build_menu(buttons, n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu


def weather():
    lat = '59.9386300'
    log = '30.3141300'
    APPID = "097595ef0c992b51dab227235e2c9bef"  # <-- Put your OpenWeatherMap appid here!
    URL_BASE = "http://api.openweathermap.org/data/2.5/"
    conn = requests.get(
        f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={log}&exclude=hourly,daily&appid={APPID}').json()
    kelvin = 273.15
    gradus = float(conn['current']['temp'] - kelvin)
    return gradus
    # print('Температура в Санкт Петербурге', "%.1f" % gradus, 'градусов')


def query_list(): pass


@bot.message_handler(content_types=['text'])
def mes(message):
    if message.text == 'Тест':
        conn = db
        button1 = types.KeyboardButton('Назад')
        keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button1)

        q_list = question_list()
        len_questions = len(q_list)
        in_bd = []
        quest = 1

        bot.send_message(message.chat.id, f'Вопрос {quest}', reply_markup=keyboard3)
        with conn.cursor() as cur:
            # print()
            cur.execute(f"""select a.num_answer ,a.answer_text,q.id_question,a.r_answer 
                    from question q inner join answer 
                    a on q.id_question = a.id_question where q.id_question = {q_list[0][0]} order by a.id_answer asc ;""")
            res_login = cur.fetchall()

        len_answers = len(res_login)
        l_num = []
        bot.send_message(message.chat.id, q_list[0][1])
        for i in res_login:
            in_menu = f'{i[0]} {i[1]}'
            l_num.append(in_menu)
            bot.send_message(message.chat.id, f'{i[0]} {i[1]}')  # quiestion
        quest += 1
        if quest == 11:
            print('11')
            quest = 1
    elif message.text == 'Статистика':
        bot.send_message(message.chat.id, 'Извините - в разработке :)')
    elif message.text == 'Погода в Спб':
        gradus = weather()
        gradus = float('{:.1f}'.format(gradus))
        printing = f'Температура в Санкт Петербурге {gradus}°'
        # printing = f'Температура в Санкт Петербурге', "%.1f" % gradus, 'градусов'
        bot.send_message(message.chat.id, printing)
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, "Добро пожаловать в ТестСистем")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        button_1 = types.KeyboardButton('Тест')
        button_2 = types.KeyboardButton('Статистика')
        button_3 = types.KeyboardButton('Погода в Спб')
        markup.add(button_1, button_2, button_3)
        bot.send_message(message.chat.id, 'Начнем заново', reply_markup=markup)

        # bot.send_message(message.chat.id, message) # print all in text - verify


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)
#     # bot.send_message()


# bot.polling(non_stop=True)
if __name__ == '__main__':
    # start = Main()
    # bot.infinity_polling()
    test_db = DB()
    db = test_db.get_connection()
    bot.polling(non_stop=True)

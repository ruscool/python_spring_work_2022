import psycopg2 as ps
from telebot import types
import requests
from connect_db import name, user, password

# name = 'testsystem'
# user = 'testsystem'
# password = "1234test"


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

    def __init__(self, name, user, password):
        self.name = name
        self.user = user
        self.password = password

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


class Dbquerry:
    def __init__(self):
        db_new = DB(name, user, password)
        self.conn = db_new.get_connection()

    def question_list(self, count):
        with self.conn.cursor() as cur:
            cur.execute(f"""select * from question q order by random() limit {count};""")
            self.result = cur.fetchall()
            return self.result

    def answers_and_question(self):
        with self.conn.cursor() as cur:
            # print()
            cur.execute(f"""select a.num_answer ,a.answer_text,q.id_question,a.r_answer 
                    from question q inner join answer 
                    a on q.id_question = a.id_question where q.id_question = {self.result[0][0]} order by a.id_answer asc ;""")
            self.res_login = cur.fetchall()
        self.len_answers = len(self.res_login)
        for_view_bot = 1
        print()
        return self.len_answers, self.result[0][0], self.res_login


class Weather:
    def weather(self):
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


class Key_bot:
    def how_much(self) -> list:
        button_1 = types.KeyboardButton('3')
        button_2 = types.KeyboardButton('5')
        button_3 = types.KeyboardButton('10')
        return button_1, button_2, button_3

    def back_menu(self):
        button_1 = types.KeyboardButton('Продолжить')
        button_2 = types.KeyboardButton('Новый тест')
        return button_1, button_2

    def start_menu(self):
        button_1 = types.KeyboardButton('Тест')
        button_2 = types.KeyboardButton('Статистика')
        button_3 = types.KeyboardButton('Погода в Спб')
        return button_1, button_2, button_3

    def back(self):
        button1 = types.KeyboardButton('Назад')
        return button1


if __name__ == '__main__':
    a = DB(name, user, password)
    # print(a.get_connection())
    qa = Dbquerry()
    # print(qa.question_list(3))
    qa.question_list(3)
    ss = qa.answers_and_question()
    print(ss)

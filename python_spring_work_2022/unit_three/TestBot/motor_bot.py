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


class Cycles:
    pass


class Logger:  # будет собирать и проверять инфу через БД
    def __init__(self, conn):
        self.answer = None
        self.user = None
        self.answer_for = None
        self.r_answer = None
        # self.anwer = None
        self.quest = None
        self.id_user = None
        self.q = None
        self.conn = conn

    def quest_count(self):
        with self.conn.cursor() as cur:
            cur.execute(f"""select t.all_quests  from "temp" t where id_user = {self.user};""")
            self.result_id = cur.fetchone()
            res = list(self.result_id)
            return int(res[0]) if int(res[0]) > 0 else 1

    def save_count_quest(self, quest):
        with self.conn.cursor() as cur:
            cur.execute(f"""UPDATE public."temp" SET all_quests={quest} WHERE id_user={self.user};""")

    def verification_id(self, id_user):
        self.id_user = id_user
        with self.conn.cursor() as cur:
            cur.execute(f"""select t.id_user from "temp" t where t.id_user = {self.id_user}""")
            self.result_id = cur.fetchone()
            print(self.result_id)
            if self.result_id is None:
                cur.execute(f"""INSERT INTO public."temp" (id_user) VALUES ({self.id_user});""")
                self.conn.commit()
                return 0
            else:
                return 1

    def insert_question(self, q, user_id):
        with self.conn.cursor() as cur:
            self.user = user_id
            self.q = q
            cur.execute(f"""UPDATE public."temp" SET questions={self.q} WHERE id_user ={self.user};""")
            cur.execute(f"""UPDATE public."temp" SET "check"=0 WHERE id_user ={self.user};""")
            cur.execute(f"""UPDATE public."temp" SET "all_quests"=0 WHERE id_user ={self.user};""")
            self.conn.commit()

    def insert_number_question(self, quest):
        with self.conn.cursor() as cur:
            self.quest = quest
            cur.execute(f"""UPDATE public."temp" SET number_question={self.quest} WHERE id_user ={self.user};""")
            self.conn.commit()

    def insert_answer(self, answer):
        with self.conn.cursor() as cur:
            self.answer = answer
            cur.execute(f"""UPDATE public."temp" SET number_question={self.quest} WHERE id_user ={self.id_user};""")
            self.conn.commit()

    def new_test(self, user):
        with self.conn.cursor() as cur:
            self.user = user
            cur.execute(f"""select ta.id_user_temp from temp_answers ta where id_user_temp ={self.user};""")
            self.result = cur.fetchone()
            print('cur', self.id_user, self.user)
            if self.result is not None:
                print('not norrre', self.id_user, self.user)
                cur.execute(f"""DELETE FROM public.temp_answers WHERE id_user_temp ={self.user};""")
                cur.execute(f"""DELETE FROM public.temp WHERE id_user ={self.user};""")
                self.conn.commit()
            cur.execute(f"""select ta.id_user from temp ta where id_user ={self.user};""")
            res_2 = cur.fetchone()
            print(res_2, 'res2')
            if res_2 is not None:
                cur.execute(f"""DELETE FROM public.temp WHERE id_user ={self.user};""")

            # else:
            #     return 0

    def continues(self):
        pass

    def save_number_quiestion(self, number, r_answer):
        with self.conn.cursor() as cur:
            self.number = number
            self.r_answer = r_answer
            cur.execute(f"""UPDATE public."temp" SET "check"=1 WHERE id_user={self.id_user};""")
            cur.execute(
                f"""INSERT INTO public.temp_answers (id_question,id_user_temp,r_answer) 
                VALUES ({self.number},{self.id_user},{self.r_answer});""")
            self.conn.commit()

    def for_answers(self):
        with self.conn.cursor() as cur:
            cur.execute(f"""select ta.id_question from temp_answers ta where id_user_temp ={self.id_user}""")
            res = cur.fetchone()
            res = list(res)
            return res[0]

    def save_answer(self, answer):
        with self.conn.cursor() as cur:
            self.answer_for = answer
            cur.execute(
                f"""UPDATE public.temp_answers SET answer={self.answer_for} WHERE id_user_temp ={self.id_user};""")
            cur.execute(f"""UPDATE public."temp" SET "check"=0 WHERE id_user={self.id_user};""")
            self.conn.commit()

    def verify_check(self):
        with self.conn.cursor() as cur:
            cur.execute(f"""select t."check" from "temp" t where id_user ={self.user}""")
            res = cur.fetchone()
            return res

    def down(self):
        with self.conn.cursor() as cur:
            cur.execute(f"""select t."check" from "temp" t where id_user ={self.id_user}""")
            res = cur.fetchone()
            return res

    def questions_left(self, user):
        self.user = user
        print(f'user= {self.user}')
        with self.conn.cursor() as cur:
            cur.execute(f"""select t.questions -t.number_question  from "temp" t where id_user = {self.user};""")
            res = cur.fetchone()
            res = list(res)
            return int(res[0])

    def for_end_test_per(self,user):
        self.user = user
        with self.conn.cursor() as cur:
            cur.execute(f"""select t.number_question from "temp" t where id_user = {self.user};""")
            res = cur.fetchone()
            res = list(res)
            return int(res[0])

    def saving_for_continues(self):
        pass

    def end_test(self):
        with self.conn.cursor() as cur:
            cur.execute(f"""select t.questions from "temp" t where id_user ={self.user};""")
            res = cur.fetchone()
            res = list(res)
            return int(res[0])


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
        button0 = types.KeyboardButton('Следующий вопрос')
        button1 = types.KeyboardButton('Назад')
        return button0, button1

    def down_menu(self):
        button_2 = types.KeyboardButton('Следующий вопрос')
        button_3 = types.KeyboardButton('Меню')
        return button_2, button_3

    def end_test(self):
        button_1 = types.KeyboardButton('Завершить тест')
        return button_1


if __name__ == '__main__':
    a = DB(name, user, password)
    # print(a.get_connection())
    qa = Dbquerry()
    # print(qa.question_list(3))
    qa.question_list(3)
    ss = qa.answers_and_question()
    print(ss)

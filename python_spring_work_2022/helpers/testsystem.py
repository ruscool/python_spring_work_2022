# todo: Реализовать классы DB и Profile
import random
import time
from time import sleep
import bcrypt
import psycopg2 as ps
import os


class Db:
    def __init__(self, name, user, password):
        self.name = name
        self.user = user
        self.password = password

    def get_connection(self):
        with ps.connect(f"dbname={self.name} user={self.user} password={self.password}") as self.conn:
            with self.conn.cursor() as cur:
                cur.execute(f"""SELECT *  FROM profile
                    """)
                res = cur.fetchall()

        return self.conn


class Profile(Db):
    ''' Данный класс содержит конструктор и метод set_profile и get_profile для добавления и получения
     пользователя соответсвенно'''

    # В констукторе инициализируем атрибуты сущности Profile
    def __init__(self, login, u_password, f_name, ouch, l_name, age, tel, email, name, user, password):
        super().__init__(name, user, password)
        self.login = login
        self.user_password = u_password
        self.f_name = f_name
        self.ouch = ouch
        self.l_name = l_name
        self.age = age
        self.tel = tel
        self.email = email
        self.get_connection()

    # в аргументе conn передается дискриптор подключения к БД
    def set_profile(self):
        with self.conn.cursor() as cur:
            print('Регистрация нового пользователя')
            try:
                cur.execute(f"""SELECT p.login  FROM profile p
                    where p.login ='{self.login}'""")
                res_login = cur.fetchone()
                if self.login == res_login[0]:
                    return 'Такой логин есть, введите новый логин'
            except:
                self.conn.rollback()

            hashAndSalt = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt())
            hashAndSalt = hashAndSalt.decode('utf-8')
            try:
                cur.execute("""SELECT x.id_user FROM public."user_man" x
                    ORDER BY x.id_user desc limit 1""")
                res_user_count = cur.fetchone()
                new_res_user = int(res_user_count[0]) + 1
            except:
                new_res_user = 1
                self.conn.rollback()

            cur.execute(
                f"""insert into public."user_man" (id_user,first_name, ouch, last_name, email, phone) values \
                ({new_res_user},'{self.f_name}','{self.ouch}','{self.l_name}','{self.email}',{self.tel});""")
            self.conn.commit()
            cur.execute(f"""insert into profile (id_profile,login,password,id_user_man) values \
                ({new_res_user},'{self.login}','{hashAndSalt}',{new_res_user});
                """)
            print('Пользователь добавлен')
            self.conn.commit()

    def get_profile(self):
        # print(self.__class__.__mro__)
        with self.conn.cursor() as cur:
            cur.execute(f"""SELECT p.login,p.password  FROM profile p
                           where p.login ='{self.login}'""")
            res_login = cur.fetchone()
            if res_login is None:
                print('Нет такого пользователя, хотите зарегистрироваться?')
                return 0
            else:
                valid = bcrypt.checkpw(self.password.encode(), res_login[1].encode())
                if valid:
                    print(f'Вы вошли под пользователем {self.login}')
                    return 1
                else:
                    print('Неверный пароль, попробуйте заново')
                    return 0


class Auth:
    def __init__(self):
        self.if_true = None
        self.is_auth = False

    def login(self, user: int) -> bool:
        """
        Возврат true - если пользователь вошел в систему
        :param user:
        :return: True
        """
        self.if_true = user
        if self.if_true == 1:
            self.is_auth = True
        return self.is_auth

    def registration(self):
        new_user = Profile('usr99', '1234test', 'Иван', 'Петрович', 'Сидоров', 29, 89234238937, 'ru@ru.com',
                           'testsystem', 'testsystem', '1234test')
        new_user.set_profile()
        self.is_auth = True
        return self.is_auth

    def log_out(self):
        self.is_auth = False


class Testsystem:
    def __init__(self):
        self.questions_in_test = None
        self.num_list = self.show_list()
        self.show_questions()

    def show_list(self):
        data = Test()
        self.data = data.get_list()
        print('Выберите номер теста')  # in View
        l=[]
        for key in self.data:
            print(key[0], '-', key[1])
            l.append(key[0])
        # print(l)
        print("\034", end="")
        try:
            self.test_number = int(input())
            if self.test_number not in l:
                raise Exception('')
        except:
            print('Неправильно выбран номер теста, повторно выберите номер теста')
            self.show_list()
        # todo: сделать выборку только из списка и запись начала теста в БД
        # self.template = data
        return self.test_number

    def show_questions(self):
        print('\n' * 30)
        # print(self.num_list)
        print(f'Выбран тест под номером {self.test_number} и вопросы к нему')
        get = Test()
        self.questions_in_test = get.get_questions(self.test_number)
        # print(self.questions_in_test)
        return self.questions_in_test

    def my_metods(self):
        pass


class Test:
    def __init__(self):
        self.conn = Db('testsystem', 'testsystem', '1234test').get_connection()

    def run(self):
        new_user = Profile('usr89', '1234test', 'Иван', 'Петрович', 'Сидоров', 29, 89234238937, 'ru@ru.com',
                           'testsystem', 'testsystem', '1234test')

        self.if_user = new_user.get_profile()
        self.t = Testsystem()
        self.v = QuestionView()
        data = self.t.questions_in_test
        self.v.render(data)

    def get_list(self) -> list:
        """
        Возврат 5 случайных тестов
        :return:
        """
        # conn = Db('testsystem', 'testsystem', '1234test')
        # conn = conn.get_connection()
        with self.conn.cursor() as cur:
            cur.execute(f"""SELECT id_test, theme FROM public."test";
                """)
            list = cur.fetchall()
            random_list = random.sample(list, 5)
            random_list.sort()

        return random_list

    def get_questions(self, number):
        with self.conn.cursor() as cur:
            cur.execute(f"""SELECT tq.id_question, q.question_text  FROM test t inner join
             test_question tq on t.id_test =tq.id_test left join question q on tq.id_question =q.id_question 
             where t.id_test ={number};""")
            res_login = cur.fetchall()

        return res_login


# View
class View:  # abstract
    def __init__(self):
        self.conn = Db('testsystem', 'testsystem', '1234test').get_connection()

    def render(self):
        pass


class ListView(View):
    def render(self):
        print()
        v_list = Testsystem
        # print('Выберите номер теста')  # in View
        # for key in v_list.show_list():
        #     print(key[0], '-', key[1])
        # print("\034", end="")
        # self.test_number = input()
        # print(v_list.show_list())
        # return self.test_number


class QuestionView(View):
    def render(self, data):
        for i in data:
            print(i[0],i[1])


class RegistrationView(View):
    """В классе перегружаем виртуальный метод  render от родителя"""

    def render(self, data):
        """Метод реализует отрисовку регистрации пользователя"""


class LoginView(View):
    """В классе перегружаем виртуальный метод  render от родителя"""

    def render(self, data):
        """Метод реализует отрисовку входа по логину и паролю для зарегистрированного пользователя"""


if __name__ == "__main__":
    main = Test()
    main.run()

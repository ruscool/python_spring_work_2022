# todo: Реализовать классы DB и Profile
import random
import time
from time import sleep
import bcrypt
import psycopg2 as ps
from datetime import datetime as dtime
import datetime
from abc import ABC, abstractmethod


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
        self.dt = datetime.datetime.now()
        self.questions_in_test = None
        self.num_list = self.show_list()
        self.conn = Db('testsystem', 'testsystem', '1234test').get_connection()

    def show_list(self):
        data = Test()
        self.data = data.get_list()
        print('Выберите номер теста')  # in View
        l = []
        for key in self.data:
            print(key[0], '-', key[1])
            l.append(key[0])
        print("\034", end="")
        try:
            self.test_number = int(input())
            if self.test_number not in l:
                raise Exception('')
        except:
            print('Неправильно выбран номер теста, повторно выберите номер теста')
            self.show_list()
        return self.test_number

    def show_questions(self):
        print('\n' * 30)
        print(f'Выбран тест под номером {self.test_number} и вопросы к нему')
        get = Test()
        self.questions_in_test = get.get_questions()

        for i in self.questions_in_test:
            print(i[0], i[1])
        print('\nНачнем тест - дается время 10 мин')
        for i in range(5, 0, -1):
            print(i, end=' ')
            sleep(0.1)
        self.dt = dtime.now().timestamp()

        return self.questions_in_test

    def my_metods(self, answers):
        """
        Сбор информации о дате сдаче, номера теста, и отвеченных вопросах,
        записи ее в БД и подсчета результата

        :param dt:
        :param answers:
        :return: (dt,self.test_number, answers)
        """
        # self.dt = dt
        self.for_result = answers
        self.answers = str(answers)

        # здесь сделать слияние для БД и расчета результата теста
        # ввод (дата, номер теста, ответы) - в БД - для хранения
        # разбор ответов - пока только в Да или нет и в %
        print(self.dt, self.test_number, self.answers)
        print('я здесь')
        return self.dt, self.test_number, self.answers

    def save_in_base(self):
        with self.conn.cursor() as cur:
            cur.execute(f"""INSERT INTO public."result" (id,id_user,id_test,answer,date_test)
	            VALUES (1,8,{self.test_number},'{self.answers}','{self.dt}');""")
            self.conn.commit()

    def result_test(self):
        end_dt = int(self.for_result[-1])
        how_long = int(end_dt - self.dt)
        nn = time.strftime("%M:%S", time.localtime(how_long))
        print(' ' * 30)
        print(f'Тест пройдет за {nn}')
        print(self.for_result)
        if sum(self.for_result[2:-1:3]) / 10 * 100 > 75:
            test = 'Сдан'
        else:
            test = 'Не сдан'
        print(f'Результаты теста')
        print(f'Правильно на {sum(self.for_result[2:-1:3]) / 10 * 100} процентов, тест - {test}')


class Test:
    def __init__(self):
        self.conn = Db('testsystem', 'testsystem', '1234test').get_connection()

    def run(self):
        new_user = Profile('usr89', '1234test', 'Иван', 'Петрович', 'Сидоров', 29, 89234238937, 'ru@ru.com',
                           'testsystem', 'testsystem', '1234test')

        self.if_user = new_user.get_profile()
        self.t = Testsystem()
        self.v = QuestionView()
        data = self.t.show_questions()
        self.get_questions()
        self.answers = self.v.render(data)
        self.t.my_metods(self.answers)
        # self.t.save_in_base()
        self.t.result_test()

    def get_list(self) -> list:
        """
        Возврат 5 случайных тестов
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute(f"""SELECT id_test, theme FROM public."test";
                """)
            list = cur.fetchall()
            random_list = random.sample(list, 5)
            random_list.sort()
            # print(random_list)
        return random_list

    def get_questions(self):
        with self.conn.cursor() as cur:
            cur.execute(f"""select * from question q """)
            res_login = cur.fetchall()
            random_questions = random.sample(res_login, 10)
            random_questions.sort()
            # print(random_questions)
        return random_questions


# View
class View(ABC):  # abstract
    @abstractmethod
    def render(self):
        pass


class ListView(View):
    def render(self):
        print()


class QuestionView(View):
    def __init__(self):
        self.end_dt = None
        self.conn = Db('testsystem', 'testsystem', '1234test').get_connection()
        self.answer = None

    def render(self, data):
        print(' ' * 30)
        in_bd = []
        print(data)
        for n in data:
            print('Вопрос', n[1])
            print('Выберите ответ:')
            with self.conn.cursor() as cur:
                print()
                cur.execute(f"""select a.num_answer ,a.answer_text,q.id_question,a.id_answer,a.r_answer 
                from question q inner join answer 
                a on q.id_question = a.id_question where q.id_question ={n[0]} order by a.id_answer asc ;""")
                self.res_login = cur.fetchall()
                per = 0
                for i in self.res_login:
                    print(i[0], i[1])
                    per = i[-1]
            st = 0
            # если нет номера такого ответа
            while st != 1:
                st = 0
                self.answer = int(input())
                l_num = [1, 2, 3]
                try:
                    if self.answer not in l_num:
                        print('Выберите из списка по номеру')
                    else:
                        st = 1
                        in_bd.append(n[0])
                        in_bd.append(int(self.answer))
                        in_bd.append(int(per))
                        # print('after del:', in_bd)
                        print('Ответ принят\n')
                except:
                    print('Выберите из списка по номеру')
        self.end_dt = dtime.now().timestamp()
        in_bd.append(self.end_dt)
        print('Тест окончен\n')
        return in_bd


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

# todo: Реализовать классы DB и Profile
import bcrypt
import psycopg2 as ps


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
        with self.conn.cursor() as cur:
            cur.execute(f"""SELECT p.login,p.password  FROM profile p
                           where p.login ='{self.login}'""")
            res_login = cur.fetchone()
            if res_login is None:
                return 'Нет такого пользователя, хотите зарегистрироваться?'
            else:
                valid = bcrypt.checkpw(self.password.encode(), res_login[1].encode())
                if valid:
                    return f'Вы вошли под пользователем {self.login}'
                else:
                    return 'Неверный пароль, попробуйте заново'


class Auth:
    def __init__(self):
        self.is_auth = False

    def login(self):
        pass

    # вызов БД
    # obj = Profile(self, login, password)
    # проверка
    # return self.is_auth = True

    def registration(self):
        pass

    # регистрация
    # obj = Profile (параметры)
    # return obj.set_profile() - регистрация нового пользователя
    # возврат  self.is_auth = True

    def log_out(self):
        self.is_auth = False


class Testsystem:
    def get_list_test(self):
        # todo:
        obj = Test()
        obj.get_list()


class Test:
    def get_list(self):
        # возврат из БД рандом 10 тестов
        return '10 tests'

    def get_questions(self, id_list):
        # возврат номера теста
        # дома сделать объединение таблиц test, questions, answer
        return 'возврат номера теста'


if __name__ == "__main__":
    # conn = Db('testsystem', 'testsystem', '1234test')
    # conn = conn.get_connection()
    # print(conn)
    print()
    new_user = Profile('usr89', '1234test', 'Иван', 'Петрович', 'Сидоров', 29, 89234238937, 'ru@ru.com',\
                       'testsystem', 'testsystem', '1234test')

    test = new_user.get_profile()
    print(test)  # проверка

    add_user = new_user.set_profile()
    print(add_user)

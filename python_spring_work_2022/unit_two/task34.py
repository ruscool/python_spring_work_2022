# todo: Реализовать классы DB и Profile
import bcrypt
import psycopg2 as ps


# class Db:
#     """Данный класс содержит конструктор и метод get_connect. В конструкторе инициализируются переменные
#      (атрибуты доступа к БД). Метод возвращает соединение."""
#     def __init__(self, dbname, user, password):
#         self.name = dbname
#         self.user = user
#         self.password = password
#
#     def get_connect(self):
#         # Метод возвращает соединение к БД
#         pass

class Db:
    def __init__(self, name, user, password):
        self.name = name
        self.user = user
        self.password = password

    def get_connection(self):
        with ps.connect(f"dbname={self.name} user={self.user} password={self.password}") as conn:
            with conn.cursor() as cur:
                cur.execute(f"""SELECT *  FROM profile
                    """)
                res = cur.fetchall()
                # print(res)
        return conn


class Profile:
    ''' Данный класс содержит конструктор и метод set_profile и get_profile для добавления и получения
     пользователя соответсвенно'''

    # В констукторе инициализируем атрибуты сущности Profile
    def __init__(self, login, password, f_name, ouch, l_name, age, tel, email):
        self.login = login
        self.password = password
        self.f_name = f_name
        self.ouch = ouch
        self.l_name = l_name
        self.age = age
        self.tel = tel
        self.email = email

    # в аргументе conn передается дискриптор подключения к БД
    def set_profile(self, conn):
        # print('Введите логин и пароль')
        # s_login = str(input('Логин '))
        with conn.cursor() as cur:
            cur.execute(f"""SELECT p.login,p.password  FROM profile p
                           where p.login ='{self.login}'""")
            res_login = cur.fetchone()
            if res_login is None:
                print('Нет такого пользователя, хотите зарегистрироваться?')
                print('\n1. да', '\n2. нет')
                choice = input()
                if int(choice) == 1:
                    return 2
                elif choice == 2:
                    return 'Хорошо, bye'
            else:
                s_password = input('password ')
                valid = bcrypt.checkpw(s_password.encode(), res_login[1].encode())
                if valid:
                    return f'Вы вошли под пользователем {self.login}'
                else:
                    return 'Неверный пароль, попробуйте заново'

    def get_profile(self, conn):
        # Извлекает профиль из БД
        pass


if __name__ == "__main__":
    conn = Db('testsystem', 'testsystem', '1234test')
    conn = conn.get_connection()
    print(conn)
    print()
    new_user = Profile('usr88', '1234test', 'Иван', 'Петрович', 'Сидоров', 29, 89234238937, 'ru@ru.com')
    test = new_user.set_profile(conn)
    print(test)

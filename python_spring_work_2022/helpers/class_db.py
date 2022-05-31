import bcrypt
import psycopg2 as ps


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


class Profile(Db):
    def __init__(self, age):
        # super().__init__(name, user, password)
        super().get_connection()
        print(self.get_connection())
        # self.login = login
        # self.password = password
        # self.fio = fio
        # self.cur = Db.
        self.age = age

    def get_profile(self):
        print('Введите логин и пароль')
        s_login = str(input('Логин '))

        self.cur.execute(f"""SELECT p.login,p.password  FROM profile p
               where p.login ='{s_login}'""")
        res_login = self.cur.fetchone()
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
                return f'Вы вошли под пользователем {s_login}'
            else:
                return 'Неверный пароль, попробуйте заново'

    def set_profile(self):
        try:
            self.cur.execute("""SELECT x.id_user FROM public."user_man" x
                ORDER BY x.id_user desc limit 1""")
            res_user_count = self.cur.fetchone()
            new_res_user = int(res_user_count[0]) + 1
        except:
            new_res_user = 1
            self.conn.rollback()
        self.cur.execute(
            f"""insert into public."user_man" (id_user,first_name) values \
                        ({new_res_user},'{self.name}');""")
        self.conn.commit()
        self.cur.execute(f"""insert into profile (id_profile,login,password,id_user_man) values \
                        ({new_res_user},'{self.login}','{self.password}',{new_res_user});
                        """)
        print('Пользователь добавлен')
        self.conn.commit()


class User_man():
    pass


if __name__ == "__main__":
    conn = Db('testsystem', 'testsystem', '1234test')
    conn = conn.get_connection()
    print(conn)
    print()
    # проверка логина и пароля
    conn_profile = Profile('33')
    get1 = conn_profile.get_profile()
    print(get1)

    # set1 = conn_profile.set_profile()
    # print(set1)

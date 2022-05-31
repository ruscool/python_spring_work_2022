import bcrypt
import psycopg2 as ps


class Db:
    def __init__(self, name, user, password):
        self.name = name
        self.user = user
        self.password = password

    def get_connection(self):
        with ps.connect(f"dbname={self.name} user={self.user}") as conn:
            with conn.cursor() as cur:
                cur.execute(f"""SELECT *  FROM profile
                    """)
                res = cur.fetchone()
        return res


class Profile:
    def __init__(self, db, login, password, name, age):
        self.db = db
        self.login = login
        self.password = password
        self.name = name
        self.age = age

    def get_profile(self):
        with ps.connect(f"dbname={self.db} user={self.name}") as conn:
            with conn.cursor() as cur:
                # print('Введите логин и пароль')
                # s_login = str(input('Логин '))
                cur.execute(f"""SELECT p.login,p.password  FROM profile p
                       where p.login ='{self.login}'""")
                res_login = cur.fetchone()
                if res_login is None:
                    return 'Нет такого пользователя, хотите зарегистрироваться?'

                else:
                    valid = bcrypt.checkpw(self.password.encode(), res_login[1].encode())
                    if valid:
                        return f'Вы вошшли под пользователем {self.login}'
                    else:
                        return 'Неверный пароль, попробуйте заново'

    def set_profile(self):
        with ps.connect(f"dbname={self.db} user={self.name}") as conn_set:
            with conn_set.cursor() as cur:
                try:
                    cur.execute("""SELECT x.id_user FROM public."user_man" x
                        ORDER BY x.id_user desc limit 1""")
                    res_user_count = cur.fetchone()
                    new_res_user = int(res_user_count[0]) + 1
                except:
                    new_res_user = 1
                    conn_set.rollback()
                cur.execute(
                    f"""insert into public."user_man" (id_user,first_name) values \
                                ({new_res_user},'{self.name}');""")
                conn_set.commit()
                cur.execute(f"""insert into profile (id_profile,login,password,id_user_man) values \
                                ({new_res_user},'{self.login}','{self.password}',{new_res_user});
                                """)
                print('Пользователь добавлен')
                conn_set.commit()


conn = Db('testsystem', 'testsystem', '1234')
conn = conn.get_connection()
print(conn)
print()
# проверка логина и пароля
conn_profile = Profile('testsystem', 'admin', '1234test', 'testsystem', '33')
get1 = conn_profile.get_profile()
print(get1)

# set1 = conn_profile.set_profile()
# print(set1)

# todo: Написать авторизацию пользователя в систему.

# Приложение в начале должно предлагать меню
# 1. Вход
# 2. Регистрация


# 1. При выборе пункта "Вход" пользователю необходимо ввести
# логин и пароль, поэтапно.
# login: _________
# password: ________
# При вводе данных авторизации, система проверяет есть ли данный
# пользователь в БД (логин) если нет то предлагает зарегистрироваться.
# Если есть и пароли совпадают, то происходит вход в систему. Пользователю показывается
# приглашение вида "Добро пожаловать Вася Пупкин!" и выпадает меню
# выбора билетов для тестирования(пока заглушка).
#
# 2. При выборе "Регистрация" пользователю необходимо ввести новый
# логин, пароль, фио, почту, телефон, группу. После система заводит
# запись в БД если пользователя под данным логином нет. Если такой пользователь
# уже существует то программа выдает об этом сообщение. Пароль необходимо хранить в БД
# в виде хеша + соль.
#
# По хешированию прочитать статью
# https://pythonist.ru/heshirovanie-parolej-v-python-tutorial-po-bcrypt-s-primerami/
# для хеширования пароля воспользоваться библиотекой bcrypt

import bcrypt
import psycopg2 as ps


def solt_hash_create(password):
    # password = '1234test'
    hashAndSalt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    # save "hashAndSalt" in data base
    # print(hashAndSalt)
    return hashAndSalt


def solt_hash_out(password):
    hashAndSalt = solt_hash_create(password)
    valid = bcrypt.checkpw(password.encode(), hashAndSalt)
    # print(valid)
    return valid


def main():
    print('Вход пользователя:\n1. Вход\n2. Регистрация\n3. Выход')
    try:
        start = int(input('Выберите действие '))
        return start
    except:
        print('только 1 или 2\nПробуем заново')
        return main()


def test_login():
    with ps.connect("dbname=testsystem user=testsystem") as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            print('Введите логин и пароль')
            s_login = input('login ')
            s_password = input('password ')
            cur.execute(f"select login from profile where login={s_login}")
            res = cur.fetchall()
            print(s_login, res)

    return 'new user'


def fio_split(fio):
    # print(fio.split())
    return fio.split()


def new_user():
    with ps.connect("dbname=testsystem user=testsystem") as conn:
        with conn.cursor() as cur:
            print('Регистрация нового пользователя')
            # логин, пароль, фио, почту, телефон, группу.
            try:
                new_user_login = input('Логин ')
                cur.execute(f"""SELECT p.login  FROM profile p
                    where p.login ='{new_user_login}'""")
                res_login = cur.fetchone()
                if new_user_login == res_login[0]:
                    print('Такой логин есть, введите новый логин')
                    return new_user()
            except:
                conn.rollback()

            new_password = input('Пароль ')
            new_fio = input('ФИО полностью ')
            new_email = input('email ')
            new_phone = input('телефон ')
            new_group = int(input('группа '))
            new_user_login = 'admin'
            # new_password = '1234test'
            # new_fio = 'Смирнов Олег Максимович'
            # new_email = 'er@df'
            # new_phone = 345346
            # new_group = 123

            print('\nПроверьте данные ')
            print('Логин', new_user_login, '\nПароль', new_password, '\nФИО', new_fio)
            print('email', new_email, '\nТелефон', new_phone, '\nГруппа', new_group)
            print('\nВерно?', '\n1. да', '\n2. нет')
            save_data = input()
            if save_data == 1:
                print('ok')
            elif save_data == 2:
                print('ок, заново')
                return new_user()
            fio = fio_split(new_fio)
            # new_f = fio[0]

            new_password = solt_hash_create(new_password)
            new_p = str(new_password)[2:-1]

            try:
                cur.execute("""SELECT x.id_user FROM public."user_man" x
                    ORDER BY x.id_user desc limit 1""")
                res_user_count = cur.fetchone()
                new_res_user = int(res_user_count[0]) + 1
            except:
                new_res_user = 1
                conn.rollback()

            cur.execute(
                f"""insert into public."user_man" (id_user,first_name, ouch, last_name, email, group_user) values \
                ({new_res_user},'{fio[1]}','{fio[2]}','{fio[0]}','{new_email}',{new_group});""")
            conn.commit()
            cur.execute(f"""insert into profile (id_profile,login,password,id_user_man) values \
                ({new_res_user},'{new_user_login}','{new_p}',{new_res_user});
                """)
            print('Пользователь добавлен')
            conn.commit()


def save_new_login():
    pass


number = main()
if number == 1:
    test_login()
elif number == 2:
    new_user()
elif number == 3:
    print('До свиданья')
else:
    print('Введено неправильно - попробуйте заново')
    main()

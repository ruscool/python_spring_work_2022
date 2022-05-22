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
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def solt_hash_out(part, password):
    return bcrypt.checkpw(password.encode(), solt_hash_create(part))


def main():
    print('Вход пользователя:\n1. Вход\n2. Регистрация\n3. Выход')
    try:
        start = int(input('Выберите действие '))
        return start
    except:
        print('только 1 или 2\nПробуем заново')
        return main()


def quest_answer():
    pass


def test_login():
    with ps.connect("dbname=testsystem user=testsystem") as conn:
        with conn.cursor() as cur:
            print('Введите логин и пароль')
            s_login = str(input('Логин '))
            cur.execute(f"""SELECT p.login,p.password  FROM profile p
                where p.login ='{s_login}'""")
            res_login = cur.fetchone()
            if res_login is None:
                print('Нет такого пользователя, хотите зарегистрироваться?')
                print('\n1. да', '\n2. нет')
                choice = input()
                if int(choice) == 1:
                    return 2
                elif choice == 2:
                    return 'Хорошо, ', bye()
            else:
                s_password = input('password ')
                valid = bcrypt.checkpw(s_password.encode(), res_login[1].encode())
                if valid:
                    return 3
                else:
                    print('Неверный пароль, попробуйте заново')
                    return test_login()


def test_student():
    pass


def bye():
    return 'До свиданья'


def fio_split(fio):
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
            print('\nПроверьте данные ')
            print('Логин', new_user_login, '\nПароль', new_password, '\nФИО', new_fio)
            print('email', new_email, '\nТелефон', new_phone, '\nГруппа', new_group)
            print('\nВерно?')
            print('\n1. да', '\n2. нет')
            save_data = input()
            if save_data == 1:
                print('ok')
            elif save_data == 2:
                print('ок, заново')
                return new_user()
            fio = fio_split(new_fio)
            hashAndSalt = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
            hashAndSalt = hashAndSalt.decode('utf-8')
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
                ({new_res_user},'{new_user_login}','{hashAndSalt}',{new_res_user});
                """)
            print('Пользователь добавлен')
            conn.commit()


def save_new_login():
    pass


def test_student():
    pass


number = main()
if number == 1:
    res = test_login()
    if res == 2:
        new_user()
    elif res == 3:
        print('Добро пожаловать Вася Пупкин!')
        test_student()
elif number == 2:
    new_user()
elif number == 3:
    bye()
else:
    print('Введено неправильно - попробуйте заново')
    main()

import requests
import psycopg2 as ps
from bs4 import BeautifulSoup
import pandas as pd
import lxml

url = "https://testua.ru/informatika/414-testy-po-informatike-s-otvetami.html"


class ParsText():
    def __init__(self, url):
        self.url = url
        self.count = 0
        self.main()

    def main(self):
        self.conn = Db('testsystem', 'testsystem', '1234test').get_connection()
        self.open_html()
        self.open_file()
        self.list_create()
        self.file_in_base()
        self.only_quest()
        self.save_in_base()

    def open_html(self):
        """
        Отрываем и сохраеняем страницу
        :return:
        """
        req = requests.get(self.url)
        self.src = req.text
        # print(self.src)
        with open('tests.html', 'w') as self.f:
            self.f.write(self.src)

    def open_file(self):
        """
        Открытие файла на чтение
        :return:
        """
        with open('test_text.txt', 'r') as file:
            self.f = file.readlines()

    def list_create(self):
        """
        Создаем список
        :return:
        """
        f_list = []
        for i in self.f:
            f_list.append(i.rstrip())
        # print(len(self.f))
        # print(len(f_list))
        self.l = []
        count = 0
        bl = []
        for i in range(len(f_list)):
            if count == 0:
                if f_list[i][0].isdigit():
                    count += 1
                bl.append(f_list[i])
            elif count == 1:
                if f_list[i][0].isdigit():
                    self.l.append(bl)
                    bl = []
                    count = 0
                bl.append(f_list[i])
                if len(bl) > 0:
                    count = 1

    def file_in_base(self):
        """
        Преобразование в словарь
        :return:
        """
        self.new_base = []
        # print(self.l[-1])
        for_num = 1
        for i in self.l:
            index = i[0].find('.')
            for row in range(1, len(i)):
                # print(i[row][0])
                # print(i[row][2:])
                if i[row][0] == '+':
                    r_answer = 1
                else:
                    r_answer = 0
                self.new_base.append({
                    'number': i[0][:index],
                    'question': i[0][index + 2:],
                    'r_answer': r_answer,
                    'answer': i[row][2:],
                    'num_answer': row
                })
                for_num += 1
        for o in self.new_base:
            print(o)

    def only_quest(self):
        """
        Преобразование в словарь
        :return:
        """
        self.only_q = []
        for_num = 0
        for i in self.l:
            index = i[0].find('.')
            self.only_q.append({
                'number': i[0][:index],
                'question': i[0][index + 2:]
            })
            for_num += 1
        num_quest = 1
        # print(str(self.only_q[28]['question']))
        with self.conn.cursor() as cur:  # работает
            for k in self.only_q:
                cur.execute(f"""INSERT INTO public.question (id_question,question_text)
                                VALUES ({k['number']},'{str(k['question'])}');""")
        self.conn.commit()
        num_quest += 1
        # for o in self.only_q:
        #     print(o)

    def save_in_base(self):
        # count = 0
        with self.conn.cursor() as cur:
            # for k in self.only_q:
            #     cur.execute(f"""INSERT INTO public.question (id_question,question_text)
            #                     VALUES ({k['number']},'{k['question']}');""")
            #     self.conn.commit()
            #     # count = 1
            num_answer = 1
            # count_answers=len(self.l)
            # print(count_answers)
            # with self.conn.cursor() as cur:
            for i in self.new_base:
                # if res_login is None:
                print(num_answer, i['answer'], i['number'], i['r_answer'])
                cur.execute(f"""INSERT INTO public.answer (id_answer,answer_text,id_question,r_answer,num_answer)
                                     VALUES ({num_answer},'{i['answer']}',{i['number']},
                                        {i['r_answer']},{i['num_answer']});""")
                self.conn.commit()
                # cur.execute(f"""select count(*) from answer a where a.id_question = {};""")

                # self.conn.commit()
                # res_login = cur.fetchone()
                num_answer += 1

    def save_to_json(self):
        pass


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


if __name__ == '__main__':
    one = ParsText(url)

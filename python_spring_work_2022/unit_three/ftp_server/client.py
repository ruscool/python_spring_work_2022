# # Echo client program
import socket


class Ftp_client:
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 50881
        self.path = './ftp_files/'
        self.run()

    def run(self):
        self.load_list_file()
        # self.load_file()

    def load_list_file(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
            # count = 0
            self.s.connect((self.HOST, self.PORT))
            file_l = 'list'
            zapros = f'GET {file_l}'.encode('utf-8')
            # print('to_server ', zapros)
            self.s.send(zapros)
            data = self.s.recv(1024)
            list_new = data.decode('utf-8')
            # print('[serser] = ', list_new)
            self.list_new = list_new[1:-1].split(", ")
            print('Список файлов на сервере:')
            for i in self.list_new:
                print(i[1:-1])
            # count = 1
            print('.' * 30)
            print('end...load list')

            # 2
            try:
                file_f = str(input("Выберите файл:"))
                zapros = f'GET {file_f}'.encode('utf-8')
                print('to_server ', zapros)
                self.s.send(zapros)
            except:
                print('Неправильный выбор')

            # 3 прием и запись файла
            with open(self.path + file_f, 'wb') as f:
                dd = self.s.recv(1024)
                print(f'dd-1 = {len(dd)}')
                f.write(dd)
                print(f'dd0 = {len(dd)}')
                while len(dd) == 1024:
                    dd = self.s.recv(1024)
                    f.write(dd)
                    print(f'dd1 = {len(dd)}')

            # f.close()
            print(f'File loaded {file_f}')
            print('end...load file')

            # 4 answer
            # self.s.send('')

            # self.s.close()
        # return self.list_new

    @classmethod
    def verification(cls, inp):
        pass


if __name__ == '__main__':
    start = Ftp_client()

# #  TODO: реализовать протокол
# # https://docs.python.org/3/library/socket.html#module-socket
# # https://pythonist.ru/rabota-s-setevymi-soketami-na-python/
import socket
import datetime
import list_dir
from sys import platform


class Ftp_mini_server:
    """
    ftp_mini_server
    """

    def __init__(self):
        self.dt = None
        self.HOST = ''
        self.PORT = 50880
        self.addr = None
        self.conn = None
        self.format = 'utf-8'
        self.run()

    def run(self):
        self.comp = self.listen_server()
        self.logger(self.comp)

    def listen_server(self):
        """
        Основной метод - запуск и работа с клиентом
        :return:
        """
        print('-' * 50)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen(5)
            self.conn, self.addr = s.accept()
            with self.conn:
                print('self.connected by', self.addr)
                while True:
                    try:
                        self.list_files = list_dir.list_files()
                        self.req_file = str(self.list_files).encode('utf-8')
                        data = self.conn.recv(1024).decode('utf-8')  # .decode('utf-8')
                        if len(data.split(' ')) > 1:
                            self.request = data.split(' ')[1]  # запрос или имя файла
                        else:
                            self.request = data
                        self.path = f'.{self.sys_tem()}server_files{self.sys_tem()}'
                        if not self.request:
                            break
                        else:
                            if self.request == 'list':
                                self.conn.sendall(self.req_file)
                            else:
                                self.dt = datetime.datetime.now()
                                file = f'{self.path}{self.request}'
                                with open(file, "rb") as f:
                                    self.conn.sendfile(f)
                    except KeyboardInterrupt:
                        print('NO data, stop')
                        break
                return self.dt, self.addr, file

    @classmethod
    def sys_tem(cls):
        """
        В зависимости от системы меняет '\' или '/'
        :return: '\' или '/'
        """
        if platform == "linux" or platform == "linux2":
            return '/'
        elif platform == "darwin":
            return '/'
        elif platform == "win32":
            return '\\'

    def logger(self, comp: list):  # what need - data, ip, what
        """
        Запись в логгер - когда, с какого адреса заходил и что скачивал
        :param comp: list
        :return:
        """
        dt, ip, what = comp
        print(comp, '\n', dt, ip, what)
        with open('logger.txt', 'a') as f:
            dt = dt.strftime('%d-%m-%Y_%H:%M:%S')
            f.write(f'\n{dt}: {ip}{what}')


if __name__ == '__main__':
    start = Ftp_mini_server()

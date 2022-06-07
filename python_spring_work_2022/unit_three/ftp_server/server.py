# #  TODO: реализовать протокол
# # https://docs.python.org/3/library/socket.html#module-socket
# # https://pythonist.ru/rabota-s-setevymi-soketami-na-python/
import socket
import os
import list_dir


class Ftp_mini_server:
    # Дописать протокол передачи файла. Сперва разбираем
    # HOST = ''  # Хост
    # PORT = 50010  # Порт сервра

    # Создаем сокет
    def __init__(self):
        self.HOST = ''
        self.PORT = 50881
        self.addr = None
        self.conn = None
        self.format = 'utf-8'
        self.run()

    def run(self):
        self.listen_server()

    def listen_server(self):
        print('-' * 50)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            print(s)
            s.listen(5)
            self.conn, self.addr = s.accept()
            with self.conn:
                print('self.connected by', self.addr)
                count = 0
                while True:
                    try:
                        count += 1
                        print(f'count = {count}')
                        self.list_files = list_dir.list_files()
                        print(self.list_files)
                        aa = str(self.list_files).encode('utf-8')
                        data = self.conn.recv(1024).decode('utf-8')  # .decode('utf-8')
                        if not data:
                            break
                        print('что пришло:', data)
                        if len(data.split(' ')) > 1:
                            request = data.split(' ')[1]  # запрос или имя файла
                        else:
                            request = data
                        print(f'request from client: {request},', type(request))
                        self.path = './server_files/'
                        if not request:
                            break
                        else:
                            if request == 'list':
                                print(f'to client {aa}')
                                self.conn.sendall(aa)
                                print('конец запроса')
                            else:
                                file = f'{self.path}{request}'
                                with open(file, "rb") as f:
                                    self.conn.sendfile(f)
                                    # data = f.read()
                                # print(repr(f))
                                print(f'передача файла {request}')
                                # self.conn.send('test'.encode(self.format))

                                print('end send file')
                                # f.close()
                                # s.close()

                            # file = 'server_files/opt-2.png'
                            # with open('server_files/opt-2.png', 'rb') as f:
                            #     file = f.readlines()
                            #     # print(file[:10])
                            #     self.conn.sendall(file)
                            # self.conn.sendall(self.list_files)
                    except KeyboardInterrupt:
                        print('NO data, stop')
                        break


if __name__ == '__main__':
    start = Ftp_mini_server()


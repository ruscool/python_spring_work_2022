import os

def list_files():
    path='./server_files/'
    list_f=os.listdir(path)
    # print(list_f)
    return list_f

if __name__ == '__main__':
    list_files()
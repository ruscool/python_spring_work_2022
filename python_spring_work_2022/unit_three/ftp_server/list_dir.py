import os

def list_files():
    path='./server_files/'
    list_f=os.listdir(path)
    # print(list_f)
    return list_f


list_files()
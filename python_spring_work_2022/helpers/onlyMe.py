# # сбор помощников
#
# import datetime
# import time
# # print(dir(list))
# """
# import os
# # печать списка аттрибутов
# def dir(x): return [a for a in dir(x) if not a.startswith("__")]
#
# print(dirx(list))
# #print(help(list))
#
# #print(tuple.__doc__)
# #print(os.path.__doc__)
# print(help(list.extend))
#
# #print([a[i]+1 for i in range(n)]) # однострочник"""
#
# tt = datetime.date.fromtimestamp(time.time())
# print(tt)
# d=tt.day
# print(d)
import pandas as pd
import matplotlib.pyplot as plt
from python_spring_work_2022.helpers.all_func import insert_time_in_header_file


def create_from_csv() -> any:
    """
    Загрузка из файла csv

    """
    text = pd.read_csv("/CSV/15 logs200122.csv")

    print(text.keys())
    print(text[['id', 'timestamp', 'contract_type', 'entry_tick',
                'sell_price']].tail())
    text[['timestamp', 'entry_tick']].plot()
    plt.show()


def write_f():
    text = pd.read_json("../../for_read_file/from_30042022_172746.json")
    # text.index.name = "number"
    # text.columns.name = "main"
    # print(text["ask"].head())
    print(text.columns)
    # text['ask'].head(100).plot()
    btc = text[text['currency'] == 'BTCUSD']
    # btc[['high','low','open']].plot()
    # print(text.dtypes)
    # print(text.shape)
    # print(text.describe())
    # print(text[text["open"] > 29000])
    # print(btc.ask)
    # print(text.groupby('currency', as_index=False).agg({'bid': 'count'}).sort_values('bid', ascending=False))
    # print(text.groupby('currency', as_index=False).agg({'bid': 'count'}).
    # sort_values('bid', ascending=False).to_csv("sort_data.csv", index=False)) # вещь - 2 строки
    # print(text.groupby(['currency','ask']).mean())

    col1 = text['currency'] == 'BTCUSD'
    col_name=(text.loc[col1])

    # orders.query('sales > 1000 & ship_mode == First') - example
    new_col = text['close'] - text['open']
    pr=text[['currency', 'open', 'close']]
    text=text.assign(raz=text['high']-text['close'])
    # print(pr.loc[col1].head())
    # print(text.mean(axis=0)) # -среднее по столбцам
    # text=(text[['currency', 'high', 'close','raz']].loc[col1])
    rec_mean=text['raz']
    print(rec_mean)
    # print(text)
    # insert(2, 'raznica', new_col))
    # print(text)

    plt.show()


def from_new_file():
    with open("../../for_read_file/data_set3.txt") as f_read:
        cre_list = list(f_read)
        l = ""
        for line in cre_list[1:]:
            if line == cre_list[-1]:
                l = l + line
            else:
                l = l + line + ","
        l = "[" + l + "]"
        for i in range(len(l)):
            dd = l[i]
            if dd == "\'":
                l = l[:i] + '"' + l[i + 1:]
        time_insert = insert_time_in_header_file()
        print(time_insert)
        f_path = "../for_read_file/from_" + time_insert + ".json"
        with open(f_path, "w+") as f_new_file:
            f_new_file.write(l)


# from_new_file()
write_f()

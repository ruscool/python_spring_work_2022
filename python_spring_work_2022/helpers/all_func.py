# todo:  all_func - мои рабочие функции

import pandas as pd
import matplotlib.pyplot as plt
import datetime


def create_from_csv() -> any:
    """
    Загрузка из файла csv данных для Pandas
    графики

    """
    text = pd.read_csv("/Users/ruslan/PycharmProjects/pythonBrouser2/CSV/15 logs200122.csv")

    print(text.keys())
    print(text[['id', 'timestamp', 'contract_type', 'entry_tick',
                'sell_price']].tail())
    text[['timestamp', 'entry_tick']].plot()
    plt.show()


def insert_time_in_header_file():
    """
    Возвращает значение -дата_время для файла
    :return: str
    """
    dt = datetime.datetime.now()
    return dt.strftime('%d%m%Y_%H%M%S')



a=insert_time_in_header_file()
print(a)
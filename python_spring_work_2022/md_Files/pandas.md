## Pandas

*** 
pd.shape - количество строк и колонок

#### https://smysl.io/blog/pandas/

#### https://nuancesprog.ru/p/12234/

https://nuancesprog.ru/p/12819/ - нужное
https://nuancesprog.ru/p/12898/ - добавление столбцов в dataFrame
https://pythobyte.com/sorting-a-dataframe-649de5fa/ - - Сортировка фрейма данных с помощью функции sort_values()
https://pythonist.ru/piramidalnaya-sortirovkaheapsort-na-python/

https://coderlessons.com/tutorials/python-technologies/izuchite-strukturu-dannykh-python/python-algoritmy-sortirovki

#### index -

df.set_index('колонка', inplace-True) - установка индекса и проходом на будущее df.reset.index - сброс индекса при
загрузке файла прописать после имени файла -

#### loc  iloc - уточнить

2. Функция iloc

1.функция loc loc - это функция "Выбор по метке". Проще говоря, она предназначена для получения данных по метке. Что это
за метка, это '2013-01-01' ~ '2013-01-06', 'A' ~ 'D'

2.Функция iloc - это выбор по позиции, то есть выбор данных по позиции, то есть данных n-й строки и n-го столбца,
поэтому целочисленный параметр позиции передается.

#### set_option

df.set_option('display.max_columns', макс значение) - установка макс значения колонок при выводе df.set_option('
display.max_rows', макс значение) - макс - но строк

#### at

pd.at[индекс, колонка,если несколько колонок, то еще одни []] = 'название' - также как loc

#### if else

https://datatofish.com/if-condition-in-pandas-dataframe/

####  

https://medium.com/nuances-of-programming/4-способа-добавления-колонок-в-датафреймы-pandas-ac032ebbe6bf

# количество строк подсчитать

.shape метод для получения количества строк DataFrame .len(DataFrame.index) быстрейший метод получения количества строк
в Pandas dataframe.apply() для подсчета строк, удовлетворяющих условию в Pandas

# поменять имя в колонке

df.rename(columns={'имя которое меняем':'новое имя'}, inplace=True)

df[''колонка'].map({"старое значение","новое значение"})

### обьединение баз

df.append(df2,ignore_index=True,sort=False)

## sort sorted
d.sort_values(by='колонка')
d.sort_values(by='колонка', ascending=Fale, inplace=True) - по убывающей
d.sort_values(by=['колонка','еще колонка'], ascending=[False, True]) - можно устанавливать
                                на каждую колонку порядок
вернуть - df.sort_index()

### grouppping and agg
df['columns'].value_counts() - подсчет всего по группам в колонке

группировка по колонке
filt=df['columns'] == 'колонка'
df.loc[filt]
можно добавить еще
df.loc[filt]['колонка по которой надо сделать подсчет].value_counts()

---
country_grp=df.groupby[''Country']
country_grp[''SOcial_media'].value_counts().loc[''если добавить то по стране'] - 
                                        группировка и сортировка по странам и медиа

### DataFrame.fillna
вещь - Значение,используемое для заполнения дыр (например,0),поочередно 
dict/Series/DataFrame значений с указанием,какое значение использовать для 
каждого индекса (для Series)или столбца (для DataFrame).Значения,не входящие
в dict/Series/DataFrame,не будут заполнены.Это значение не может быть списком.

### unique
есть ли уникальные значения

### индекс и колонка - взять одно значение из таблицы
df.loc[0-номер индекса, сама колонка ''']
df.loc[0,'date].day_name() - возвращает день недели

### индексация при чтении файла
> orders = pd.read_csv('orders.csv', index_col='id')

#### fillna() - при первичной обработке - замена Nan на значение - к примеру 0
df[df.Embarked.isna()] - поиск пустых значений
df = df.fillna({'Embarked': 0}) - замена на 0 - к примеру
sd['Age'].fillna(int(sd['Age'].mean()), inplace=True)  -  вещь


#### df.groupby('Pclass').agg({'Cabin':'count'}).sort_values('Cabin', ascending=False)

#### .dtype.kind
https://runebook.dev/ru/docs/numpy/reference/arrays.dtypes
# todo: Реализовать две сопрограммы. Первая с заданной периодичность(раз в 2,3 сек) пишет в файл и выводит результат.
# другая делает запрос к БД на выборку  билета и отображает поочередно  название билета (раз в 2,3 сек)

# Bonus:
# В качестве бонуса можно реализовать Telegtram - бота который в виде викторины задает
# вопросы. Вопросы можно взять из тестовой системы. После вывода бот принимает вариант ответа.
# В конце викторины выводит кол-во правильных и неправильных ответов и приз в случае успеха.
# В качестве библиотеки можно взять  библиотеку telebot. Описание по разработки и примеры найти
# в многочисленных статьях в Internet.

import asyncio
import datetime
from aiofile import async_open
import aiohttp



async def task1():
    text = f'\nНачало записи в логгер {datetime.datetime.now().time()} task 1 start'
    print(text)
    with open('logger_async.txt', 'a') as fp:
        async with async_open(fp) as afp:
            await afp.write(text)
        print('task 1 end')


async def task2():
    print('task 2 start')
    url = 'https://api.openweathermap.org/data/2.5/'
    lat = '59.9386300'
    log = '30.3141300'
    result = []
    appid = "097595ef0c992b51dab227235e2c9bef"  # <-- Put your OpenWeatherMap appid here!
    async with aiohttp.ClientSession() as session:
        conn = await session.get(
            f'{url}onecall?lat={lat}&lon={log}&exclude=hourly,daily&appid={appid}',
            ssl=False)
        result.append(await conn.json())
    kelvin = 273.
    gradus = float(result[0]['current']['temp'] - kelvin)
    print('Температура в Санкт Петербурге', "%.1f" % gradus, 'градусов')
    print('task 2 end')


async def main():
    await asyncio.gather(task1(), task2())


if __name__ == '__main__':
    asyncio.run(main())


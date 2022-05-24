# Справочник по Virtualenv
***
#### Установка Virtualenv
    pip3 install virtualenv

#### Создание среды
    virtualenv <имя среды>

#### Создание среды с утановкой версии Python
    virtualenv --python=python3.6 <имя среды>

#### Запретить использование системного site-packages (для 
####полной изоляции вашего окружения от системы
    virtualenv --no-site-packages <имя среды>

#### Заставляет окружение использовать установленные в 
####системе пакеты

    virtualenv --system-site-packages <имя среды>

#### Используется для очистки существующего окружения от 
#### пакетов и прочих изменений
    virtualenv --clear existing_venv

#### Активация
    source venv/bin/activate

#### Деактивация
    deactivate
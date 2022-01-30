[![Run Tests in main](https://github.com/PerchunPak/PingerBot/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/PerchunPak/PingerBot/actions/workflows/tests.yml)
[![Run Tests in rewrite](https://github.com/PerchunPak/PingerBot/actions/workflows/tests_rewrite.yml/badge.svg?branch=rewrite)](https://github.com/PerchunPak/PingerBot/actions/workflows/tests_rewrite.yml)
[![Run Tests in newdb](https://github.com/PerchunPak/PingerBot/actions/workflows/tests_newdb.yml/badge.svg)](https://github.com/PerchunPak/PingerBot/actions/workflows/tests_newdb.yml)

# Pinger Bot

Это почти доделанная альтернатива [RuMineBot](https://vk.com/ruminebot). По сути представляет собой её копию, только опенсорс.

## Установка

1. **Установите [Python 3.7 или выше](https://www.python.org/downloads)**

Рекомендовано [Python 3.10](https://www.python.org/downloads/release/python-3101), именно на нем тестируется бот.

2. **Клонируйте репозиторий**

Используйте `git clone https://github.com/PerchunPak/PingerBot.git` и `cd PingerBot`

3. **Установите зависимости**

Используйте `pip install -Ur requirements.txt`

4. **Создайте базу данных в формате PostGreSQL**

Вам нужна будет версия 9.5 или выше. База данных будет хранить пинги и добавленные сервера. Централизованной базы данных нет.

5. **Настройте Конфигурацию.**

В корневом каталоге есть файл под названием `config.py`, который содержит две переменные, необходимые для запуска бота. Один из них - `TOKEN`, который представляет собой строку, содержащую токен бота Discord. Другой переменной является `POSTGRES`, которая представляет собой строку, содержащую параметры подключения для базы данных Postgres, созданной на шаге 4.

## Хостинг через Docker

1. **Повторите все шаги выше.**

P.S. Докер так же запускает Postgres, так что вы можете указать стандартные данные от дата базы которые будут работать

2. **Используйте `docker build -t pingerbot .`**

3. **Запустите дата базу и бота с помощью `docker-compose up -d`**

## Запуск тестов

1. **Повторите все шаги выше.**

2. **Установите зависимости `pip install -Ur tests_requirements.txt`**

3. **Запустите проверку линта**

**`flake8 . --exclude .*,__*__,venv --count --max-complexity=10 --max-line-length=127 --ignore=E70`**

И последнее, запустите авто-форматер black командой: `black . -l 127`

4. **Запустите сами тесты командой `pytest`**

Если вы запускаете тесты через какую либо IDE, вам прийдется добавить аргумент `--no-cov`, иначе [возможно будет возникать ошибка](https://pytest-cov.readthedocs.io/en/latest/debuggers.html)

---

**Важная Заметка**: Вам нужно включить привилегию `SERVER MEMBERS` для работы бота. [Следуйте этим инструкциям.](https://discordpy.readthedocs.io/en/latest/intents.html#privileged-intents)

**Важная Заметка 2**: Нет, я не собираюсь разрешать приглашать основного бота всем, моя дата база слишком маленькая даже для нескольких серверов.

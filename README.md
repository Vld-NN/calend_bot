### Пояснения к коду:

1. Импорты:
   - requests: Используется для получения данных с веб-API.
   - calendar: Необходима для работы с календарной информацией.
   - datetime: Для работы с датами.
   - telebot: Основная библиотека для создания Telegram ботов на Python.

2. Функция get_holidays:
   - Получает данные о праздниках с помощью запроса к API holidays.github.io
   - Возвращает список объектов, где ключи name и date соответствуют названиям праздников и их датам.

3. Полилинг:
   - Метод polling() включает бесконечный полилинг бота, позволяющий ему оставаться активным.
  

### Шаги создания телеграм-бота

1. Установка необходимых пакетов
   Установите следующие пакеты:
   * pip install telegram
   * pip install python-dateutil
  
2. Запуск бота
   Запустите файл с помощью команды:
   *    python calendar_bot.py
   

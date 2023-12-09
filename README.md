Название проекта - python_basi_diploma

=====Содержание=====

----1.Установка----

Для использования бота нужно перейти на https://web.telegram.org/ 
Найти бот @FlightCityAirportbot

----2.Требования----

Все требования по необходимым пакетом можете найти в C:\Users\Айслу\pythonProject_bot\requirements.txt

----3.Описание----

При работе над проектом использовалась архитектура - монолит.

API запрос был сделан на сайте https://travel-advisor.p.rapidapi.com
Использовался 1 endpoint >> /airports/search  -- предоставляет ответ по выбранному городу
из которого нужно вытянуть "display_name" >> Название аэропортов.
С передачей параметров как "query":"Название города","locale":"Язык запроса: ru_RU"}


Содержание проекта:

<<<<<1.CONFIG_DATA >>>>>
               <<<<FILE: 1.config.py>>>>
                    ===  Загружает SITE_API, HOST_API, TOKEN из .env файла ===
                    === Создает соманды по умолчанию ===

<<<<<2.DATABASE >>>>>
== пакет для работы с базой данных Sqlite3 ==
               <<<<FILE: 1.models.py>>>>
                          ===Используя ORM peewee создана базовая модель и таблица User, 
                          состоящее из полей ID, MESSAGE, DATE
          
                <<<<FILE: 1.CRUD.py>>>>
                          ===Создан CRUDInterface для выполнения методов create and retrieve c 
                          таблицей User.

                <<<<FILE: 3.core.py>>>>
                          ===Соединение к базе данных database.db и создание таблицы User



<<<<<3.HANDLERS >>>>>
== пакет содержащий обработчиков сообщении  ==
           <<<<DEFAULT_HANDLERS>>>>
               <<<<FILE: start.py>>>>
                          === обрабатывает команду по умолчанию start и меняет состояние пользователя на said_hello.
               <<<<FILE: help.py>>>>
                          === обрабатывает команду по умолчанию help.
               <<<<FILE: echo.py>>>>
                          === обрабатывает неизвестные сообщения и когда состояние неизвестное.
          <<<<CUSTOM_HANDLERS>>>>
               <<<<FILE: on_click.py>>>>
                          === обрабатывает сообщения после команды start,состояние said_hello, содержит inlinekeyboard c callback_data: search and lookup
               <<<<FILE: callback_search.py>>>>
                          === меняет состояние пользователя на  flight_search и спрашивает город
               <<<<FILE: api_request.py>>>>
                          === обрабатывает состояние flight_search и отправляет запрос на сайт https://travel-advisor.p.rapidapi.com
               <<<<FILE: callback_lookup.py>>>>
                          === обрабатывает call.data: search и показывает содержимое таблицы User



<<<<4.KEYBOARDS>>>>>
          <<<<INLINE>>>>
                    <<<<inline_keyb.py>>>>
                          ====cодержит InlineKeyboardMarkUp
                   про возможности бота, состоит из 2 кнопок:
                                 1-кнопка. Отбраысвает на следующий обработчик с call.data == 'search'
                                 2-кнопка. Отбраысвает на следующий обработчик с call.data == 'lookup'
          <<<<REPLY>>>>
                    <<<<start_reply.py>>>>
                          ===Добавлен replykeyboard и 3 кнопки:
                                 1-кнопка. Отправляет текст Привет
                                 2-кнопка. Спрашивает номер телефона
                                 3-кнопка. Спрашивает геолокацию



<<<<<5.STATES>>>>>
          <<<<core.py>>>>
           ===Создание состоянии и памяти для состоянии



<<<<<6.UTILS >>>>>
          <<<<FILE: core.py>>>>
               === Содержит данные для отправления запросов: URL, QUERYSTRING, HEADERS, API-KEY и API-HOST в зашированном виде
          <<<<FILE: site_api_handler.py>>>>
                          === Создан SiteApiInterface для отправления и обработки API запросов. 
          <<<<FILE: default_commands.py>>>>
                          === содержит функцию которая добавляет боту команды по умолчанию
<<<<7.FILE: LOADER.PY>>>>
          === создает бот


<<<<<8.FILE MAIN.PY>>>>>
== файл для запуска программы ==

      

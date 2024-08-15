# Final-Project-on-Test-Automation
ИТОГОВЫЙ ПРОЕКТ ПО АВТОМАТИЗАЦИИ ТЕСТИРОВАНИЯ (PJ-04)

В рамках выполнения итогового проекта требуется протестировать интерфейс авторизации в личном кабинете Ростелеком Информационные Технологии.

Объект тестирования: https://b2c.passport.rt.ru

Результат работы:

Тестирование требований, Тест-кейсы и баг-отчеты представлены в гугл-таблице: [https://docs.google.com/spreadsheets/d/15_bRnwRjYazeY_O38of8pPxIuTWnatsR/edit?usp=sharing&ouid=108049235031232211561&rtpof=true&sd=true](https://docs.google.com/spreadsheets/d/1i3sbHMTyAjIxQm1xPMLqIPkOOY7vV9TmWAOrtaGZVIs/edit?usp=sharing)

Проведено ручное и автоматизированное тестирование с использованием PyTest и Selenium

Для составления и написания тест-кейсов применены техники тест-дизайна: классы эквивалентности, анализ граничных значений, предугадывание ошибок.

Комментарий по автотестам:

В файле base_data.py находятся базовые классы, процедуры, функции и локаторы для автотестов

В файле settings.py - регистрационные данные для позитивных тестов авторизации

В файле test_authorization form_functional.py - автотесты. Все тесты помечены номером, который совпадает с номером тест-кейса в файле: [https://docs.google.com/spreadsheets/d/15_bRnwRjYazeY_O38of8pPxIuTWnatsR/edit?usp=sharing&ouid=108049235031232211561&rtpof=true&sd=true](https://docs.google.com/spreadsheets/d/1i3sbHMTyAjIxQm1xPMLqIPkOOY7vV9TmWAOrtaGZVIs/edit?usp=sharing)

запуск автотестов (драйвер в одной папке с тест-скриптом)

python -m pytest -v --driver Chrome --driver-path/ /chromedriver.exe tests/test_authorization form_functional.py

В корне проекта в файле requirements.txt описаны используемые библиотеки.


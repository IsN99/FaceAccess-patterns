# PyQt-vesion-faceaccess-app
PyQt version

Реализация курсовой по паттернам и RUP в Python:

-Паттерн шлюза БД - row data gateway
-Паттерн бизнес-логики - table module 
(в данном случае предоставляет более высокоуровневый интерфейс для предыдущего паттерна)
-Паттерн GOF - хранитель (буфер сохраняющий состояние шлюза БД на один шаг назад)

Для распознания лиц используется предобученная модель из библиотеки face recognition.
Для связи клиентов с сервером используется протокол HTTP.
GUI реализован на библиотеке PyQt.

Реализованы основные прецеденты для пользователя и менеджера (для каждого свой клиент соответственно).


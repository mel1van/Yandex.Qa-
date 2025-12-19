# Это мой дипломный проект на курсе Инженер по тестированию +
# Яндекс Практикум

Описание проекта:

# 1. Тестирование функциональности веб-приложения
Чек лист для функционального тестирования web приложения (https://docs.google.com/spreadsheets/d/1xz67Ishn13nJg5rFr_LGwuyzD2sckBncQk2XOo2FRno/edit?gid=232626888#gid=232626888)
# 2. Ретест багов в мобильном приложении. Ответ приложен в итоговый отчет.
Регресс мобильного приложения (https://docs.google.com/spreadsheets/d/1F56i4gQC_1_yQ8Kosh18sudydrJgvb67xOqqtIZujn8/edit?gid=1186534874#gid=1186534874)
# 3. Регрессионное тестирование мобильного приложения по готовым тест-кейсам. Ответ приложен в итоговый отчет.
Регресс мобильного приложения (https://docs.google.com/spreadsheets/d/1F56i4gQC_1_yQ8Kosh18sudydrJgvb67xOqqtIZujn8/edit?gid=1186534874#gid=1186534874)
# 4. Работа с базой данных
Запросы расположены в файле Base.sql

Задание 1
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

запрос:

          SELECT c.login, COUNT(o.id) AS "deliveryCount" 
          FROM "Couriers" AS c 
          LEFT JOIN "Orders" AS o ON c.id = o."courierId" 
          WHERE o."inDelivery" = true 
          GROUP BY c.login;

Скриншот результата запроса Base_request1 sql.png 

Задание 2

Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.

запрос:

           SELECT track, 
              CASE 
	        WHEN finished = true THEN 2 
	        WHEN cancelled = true THEN -1 
	        WHEN "inDelivery" = true THEN 1 
	  ELSE 0 END AS status 
          FROM "Orders";

Скриншот результата запроса Base_request2 sql.png 
# 5. Автоматизация теста.

Для запуска теста необходимо в файл configuration скопировить URLстенда вида 
https://c9a2c813-ecef-4389-97c6-96155b0b05ce.serverhub.praktikum-services.ru/

### Структура проекта:
- `configuration.py` - настройки URL стенда
- `data.py` - тестовые данные
- `sender_stand_request.py` - вспомогательные функции для API запросов
- `test_order.py` - автоматизированный тест
- `Base.sql` - SQL запросы для работы с базой данных

## Установка и запуск

### Предварительные требования:
1. Установленный Python 
2. Установленная библиотека requests

### Установка зависимостей:
```bash
pip install requests

Скриншот автоматизации  Тест.png
      
Дополнительно в репозитории содержится:
Скриншот отправки запросов Postman: Postman_primer.png  

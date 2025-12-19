# Иван Мел, 38-я когорта — Финальный проект. Инженер по тестированию плюс

from datetime import datetime, timedelta

# Текущая дата + 3 дня для теста
delivery_date = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")

order_body = {
    "firstName": "Naruto",
    "lastName": "Uchiha", 
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": delivery_date,  # Используем актуальную дату
    "comment": "Sasuke, come back to Konoha",
    "color": ["BLACK"]
}
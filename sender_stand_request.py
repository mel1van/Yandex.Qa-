# Иван Мельничук, 38-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data

# Создание заказа
def create_order(body):
    url = configuration.URL_SERVICE + configuration.CREAT_ORDERS
    print(f"Отправка POST запроса на: {url}")
    print(f"Данные заказа: {body}")
    
    response = requests.post(url, json=body)
    print(f"Ответ сервера: статус {response.status_code}")
    return response

# Получение заказа по номеру трекера
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    print(f"Отправка GET запроса на: {get_order_url}")
    
    response = requests.get(get_order_url)
    return response

# Получение номера трекера из ответа
def get_track_from_response(response):
    try:
        json_response = response.json()
        print(f"Полученный JSON ответ: {json_response}")
        track_number = json_response.get("track")
        if track_number is None:
            print("Ключ 'track' не найден в ответе")
            print(f"Доступные ключи: {json_response.keys()}")
        return track_number
    except ValueError as e:
        print(f"Ошибка парсинга JSON: {e}")
        print(f"Текст ответа: {response.text}")
        raise
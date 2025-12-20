# Иван Мельничук, 38-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data

def create_order(body):
    """Создание заказа"""
    return requests.post(configuration.URL_SERVICE + configuration.CREAT_ORDERS,
                         json=body)

def get_order(track_number):
    """Получение заказа по номеру трекера"""
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    return requests.get(get_order_url)

def get_track_from_response(response):
    """Получение номера трекера из ответа"""
    return response.json()["track"]

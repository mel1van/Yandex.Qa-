# Иван Мельничук, 38-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def test_order_creation_and_retrieval():
    """Тест создания и получения заказа"""
    # Создание заказа
    create_response = sender_stand_request.create_order(data.order_body)
    assert create_response.status_code == 201, f"Ошибка создания заказа: {create_response.status_code}"
   
    # Получение номера трека
    track_number = sender_stand_request.get_track_from_response(create_response)
    
    # Получение данных заказа по треку
    order_response = sender_stand_request.get_order(track_number)
    assert order_response.status_code == 200, f"Ошибка получения заказа: {order_response.status_code}"

if __name__ == "__main__":
    test_order_creation_and_retrieval()

# Иван Мельничук, 38-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

# Тест создания и получения заказа
def test_order_creation_and_retrieval():
    print("Тест запущен...")
    
    # Создание заказа
    create_response = sender_stand_request.create_order(data.order_body)
    print(f"Статус-код создания заказа: {create_response.status_code}")
    print(f"Ответ сервера при создании: {create_response.text}")
    
    # Проверяем, что заказ создан успешно (код 201 - Created)
    assert create_response.status_code == 201, f"Ошибка создания заказа: {create_response.status_code}, текст: {create_response.text}"
    
    # Получение номера трека
    try:
        track_number = sender_stand_request.get_track_from_response(create_response)
        print(f"Номер трека заказа: {track_number}")
    except Exception as e:
        print(f"Ошибка при получении номера трека: {e}")
        print(f"Полный ответ: {create_response.json()}")
        raise
    
    # Получение данных заказа по треку
    order_response = sender_stand_request.get_order(track_number)
    print(f"Статус-код получения заказа: {order_response.status_code}")
    
    # Проверяем, что заказ найден (код 200 - OK)
    assert order_response.status_code == 200, f"Ошибка получения заказа: {order_response.status_code}, текст: {order_response.text}"
    
    print("Тест успешно завершен!")

# Запуск теста
if __name__ == "__main__":
    test_order_creation_and_retrieval()
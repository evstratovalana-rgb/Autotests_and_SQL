import sendor_stand_request
import data


def test_get_order_from_track_code_200():
    # 1. Выполнить запрос на создание заказа
    response_create = sendor_stand_request.post_new_order(data.order_body)

    # 2. Сохранить номер трека заказа
    track = response_create.json()["track"]

    # 3. Выполнить запрос на получения заказа по треку
    response_get = sendor_stand_request.get_order_from_track(track)

    # 4. Проверить, что код ответа равен 200
    assert response_get.status_code == 200

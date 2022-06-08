import requests


class TestProd:

    def test_post_phone_notify_connect_invalid_token(self):
        message = ['Подключение канала доставки уведомлений..'
                   'Неавторизован.']
        expected_message = ['Подключение канала доставки уведомлений..'
                            'Неавторизован.']

        token = 12345678910
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        request_url = f"{lk_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers)

        try:
            assert response.status_code == 401
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 401.")
        try:
            assert response.reason == 'Unauthorized'
        except AssertionError:
            message.append(f"Причина {response.reason}, а не 'Unauthorized'.")
        try:
            assert response.json()['message'] == 'Your request was made with invalid credentials.'
        except AssertionError:
            message.append('Ошибка в сообщении ошибки.')

        assert message == expected_message, message


    def test_post_phone_notify_connect_empty_params(self):
        message = ['Подключение канала доставки уведомлений..'
                   'Пустые "params".']
        expected_message = ['Подключение канала доставки уведомлений..'
                            'Пустые "params".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        request_url = f"{lk_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{'field': 'phone', 'message': 'Не указан номер телефона.'},
                                       {'field': 'channel',
                                        'message': 'Укажите один из каналов доставки уведомлений: '
                                                   'push, telegram, viber'}]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_phone_notify_connect_incorrect_phone(self):
        message = ['Подключение канала доставки уведомлений..'
                   'Запрос для стороннего номера.']
        expected_message = ['Подключение канала доставки уведомлений..'
                            'Запрос для стороннего номера.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9696588825,
                'channel': 'push'}

        request_url = f"{lk_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{
                                     "field": "phone",
                                     "message": "Номер телефона не привязан к аккаунту."
                                    }]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_phone_notify_connect_not_bezlimit_phone(self):
        message = ['Подключение канала доставки уведомлений.'
                   'Номер не Безлимит.']
        expected_message = ['Подключение канала доставки уведомлений.'
                            'Номер не Безлимит.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9000000000,
                'channel': 'push'}

        request_url = f"{lk_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        for i in response.json():
            try:
                assert i['message'] == 'Введенный номер не обслуживается в Безлимит!'
            except AssertionError:
                message.append('Ошибка в параметре "message".')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')

        assert message == expected_message, message


    def test_post_phone_notify_connect_shitty_phone(self):
        message = ['Подключение канала доставки уведомлений.'
                   'Некорректный номер.']
        expected_message = ['Подключение канала доставки уведомлений.'
                            'Некорректный номер.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 969658882,
                'channel': 'push'}

        request_url = f"{lk_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{
                                     "field": "phone",
                                     "message": "Введите номер телефона в формате 9001112233."
                                    }]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_phone_notify_connect_shitty_channel(self):
        message = ['Подключение канала доставки уведомлений.'
                   'Некорректный канал.']
        expected_message = ['Подключение канала доставки уведомлений.'
                            'Некорректный канал.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9006471111,
                'channel': 'swallow_my_♂CUM♂'}

        request_url = f"{lk_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{
                                     "field": "channel",
                                     "message": "Канал доставки уведомлений не найден"
                                    }]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_phone_notify_connect_integer_channel(self):
        message = ['Подключение канала доставки уведомлений.'
                   'Некорректный канал.']
        expected_message = ['Подключение канала доставки уведомлений.'
                            'Некорректный канал.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9006471111,
                'channel': 1544}

        request_url = f"{lk_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{
                                     "field": "channel",
                                     "message": "Канал доставки уведомлений не найден"
                                    }]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_phone_notify_connect_correct_push(self):
        message = ['Подключение канала доставки уведомлений.'
                   'Подключение "push".']
        expected_message = ['Подключение канала доставки уведомлений.'
                            'Подключение "push".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'push'}

        request_url = f"{lk_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        des_response = response.json()

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert des_response[2]['channel'] == 'push'
        except AssertionError:
            message.append(f"Параметр 'channel' {des_response[2]['channel']}, а не 'push'")
        try:
            assert des_response[2]['name'] == 'Push-уведомления'
        except AssertionError:
            message.append(f"Параметр 'name' {des_response[2]['name']}, а не 'Push-уведомления'")
        try:
            assert des_response[2]['isConnected'] is True
        except AssertionError:
            message.append(f"Параметр 'isConnected' {des_response[2]['isConnected']}, а не 'True'")
        try:
            assert des_response[2]['isAwaitingConfirmation'] is False
        except AssertionError:
            message.append(f"Параметр 'isAwaitingConfirmation' {des_response[2]['isAwaitingConfirmation']}, а не 'False'")

        assert message == expected_message, message


    def test_post_phone_notify_connect_correct_push_again(self):
        message = ['Подключение канала доставки уведомлений.'
                   'Повторное подключение "push".']
        expected_message = ['Подключение канала доставки уведомлений.'
                            'Повторное подключение "push".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'push'}

        request_url = f"{lk_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        des_response = response.json()

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert des_response == [{'field': 'phone',
                                     'message': 'Уведомления в push уже подключены'}]
        except AssertionError:
            message.append('Ошибка в ответе по каналу "push".')

        assert message == expected_message, message


    def test_post_phone_notify_disconnect_invalid_token(self):
        message = ['Отключение канала доставки уведомлений.'
                   'Неавторизован.']
        expected_message = ['Отключение канала доставки уведомлений.'
                            'Неавторизован.']

        token = 12345678910
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        request_url = f"{lk_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers)

        try:
            assert response.status_code == 401
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 401.")
        try:
            assert response.reason == 'Unauthorized'
        except AssertionError:
            message.append(f"Причина {response.reason}, а не 'Unauthorized'.")
        try:
            assert response.json()['message'] == 'Your request was made with invalid credentials.'
        except AssertionError:
            message.append('Ошибка в сообщении ошибки.')

        assert message == expected_message, message


    def test_post_phone_notify_disconnect_empty_params(self):
        message = ['Отключение канала доставки уведомлений.'
                   'Пустые "params".']
        expected_message = ['Отключение канала доставки уведомлений.'
                            'Пустые "params".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        request_url = f"{lk_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{'field': 'phone', 'message': 'Не указан номер телефона.'},
                                       {'field': 'channel',
                                        'message': 'Укажите один из каналов доставки уведомлений: '
                                                   'push, telegram, viber'}]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_phone_notify_disconnect_incorrect_phone(self):
        message = ['Отключение канала доставки уведомлений.'
                   'Запрос для стороннего номера.']
        expected_message = ['Отключение канала доставки уведомлений.'
                            'Запрос для стороннего номера.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9696588825,
                'channel': 'push'}

        request_url = f"{lk_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{
                                     "field": "phone",
                                     "message": "Номер телефона не привязан к аккаунту."
                                    }]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_phone_notify_disconnect_not_bezlimit_phone(self):
        message = ['Отключение канала доставки уведомлений.'
                   'Запрос для стороннего номера.']
        expected_message = ['Отключение канала доставки уведомлений.'
                            'Запрос для стороннего номера.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9000000000,
                'channel': 'push'}

        request_url = f"{lk_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        for i in response.json():
            try:
                assert i['message'] == 'Введенный номер не обслуживается в Безлимит!'
            except AssertionError:
                message.append('Ошибка в параметре "message".')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')

        assert message == expected_message, message

    def test_post_phone_notify_disconnect_shitty_phone(self):
        message = ['Отключение канала доставки уведомлений.'
                   'Некорректный номер.']
        expected_message = ['Отключение канала доставки уведомлений.'
                            'Некорректный номер.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 969658882,
                'channel': 'push'}

        request_url = f"{lk_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{
                                     "field": "phone",
                                     "message": "Введите номер телефона в формате 9001112233."
                                    }]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_phone_notify_disconnect_shitty_channel(self):
        message = ['Отключение канала доставки уведомлений.'
                   'Некорректный канал.']
        expected_message = ['Отключение канала доставки уведомлений.'
                            'Некорректный канал.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9006471111,
                'channel': 'swallow_my_♂CUM♂'}

        request_url = f"{lk_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{
                                     "field": "channel",
                                     "message": "Канал доставки уведомлений не найден"
                                    }]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_phone_notify_disconnect_integer_channel(self):
        message = ['Отключение канала доставки уведомлений.'
                   'Некорректный канал.']
        expected_message = ['Отключение канала доставки уведомлений.'
                            'Некорректный канал.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9006471111,
                'channel': 100500}

        request_url = f"{lk_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{
                                     "field": "channel",
                                     "message": "Канал доставки уведомлений не найден"
                                    }]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_phone_notify_disconnect_correct_push(self):
        message = ['Отключение канала доставки уведомлений.'
                   'Отключение "push".']
        expected_message = ['Отключение канала доставки уведомлений.'
                            'Отключение "push".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'push'}

        request_url = f"{lk_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)
        des_response = response.json()

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert des_response[2]['channel'] == 'push'
        except AssertionError:
            message.append(f"Параметр 'channel' {des_response[2]['channel']}, а не 'push'")
        try:
            assert des_response[2]['name'] == 'Push-уведомления'
        except AssertionError:
            message.append(f"Параметр 'name' {des_response[2]['name']}, а не 'Push-уведомления'")
        try:
            assert des_response[2]['isConnected'] is False
        except AssertionError:
            message.append(f"Параметр 'isConnected' {des_response[2]['isConnected']}, а не 'False'")
        try:
            assert des_response[2]['isAwaitingConfirmation'] is False
        except AssertionError:
            message.append(f"Параметр 'isAwaitingConfirmation' {des_response[2]['isAwaitingConfirmation']}, а не 'False'")

        assert message == expected_message, message


    def test_post_phone_notify_disconnect_correct_push_again(self):
        message = ['Отключение канала доставки уведомлений.'
                   'Повторное отключение "push".']
        expected_message = ['Отключение канала доставки уведомлений.'
                            'Повторное отключение "push".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'push'}

        request_url = f"{lk_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)
        des_response = response.json()

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert des_response[2]['channel'] == 'push'
        except AssertionError:
            message.append(f"Параметр 'channel' {des_response[2]['channel']}, а не 'push'")
        try:
            assert des_response[2]['name'] == 'Push-уведомления'
        except AssertionError:
            message.append(f"Параметр 'name' {des_response[2]['name']}, а не 'Push-уведомления'")
        try:
            assert des_response[2]['isConnected'] is False
        except AssertionError:
            message.append(f"Параметр 'isConnected' {des_response[2]['isConnected']}, а не 'False'")
        try:
            assert des_response[2]['isAwaitingConfirmation'] is False
        except AssertionError:
            message.append(f"Параметр 'isAwaitingConfirmation' {des_response[2]['isAwaitingConfirmation']}, а не 'False'")

        assert message == expected_message, message


# Проверка работы подключения других каналов + проверка работы параметра 'isAwaitingConfirmation'


    def test_post_phone_notify_connect_correct_telegram(self):
        message = ['Подключение канала доставки уведомлений.'
                   'Подключение "telegram".']
        expected_message = ['Подключение канала доставки уведомлений.'
                            'Подключение "telegram".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'telegram'}

        request_url = f"{lk_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        des_response = response.json()

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert des_response[0]['channel'] == 'telegram'
        except AssertionError:
            message.append(f"Параметр 'channel' {des_response[0]['channel']}, а не 'telegram'")
        try:
            assert des_response[0]['name'] == 'Telegram'
        except AssertionError:
            message.append(f"Параметр 'name' {des_response[0]['name']}, а не 'Telegram'")
        try:
            assert des_response[0]['isConnected'] is False
        except AssertionError:
            message.append(f"Параметр 'isConnected' {des_response[0]['isConnected']}, а не 'False'")
        try:
            assert des_response[0]['isAwaitingConfirmation'] is True
        except AssertionError:
            message.append(f"Параметр 'isAwaitingConfirmation' {des_response[0]['isAwaitingConfirmation']}, а не 'True'")

        assert message == expected_message, message


    def test_post_phone_notify_connect_correct_viber_while_telegram(self):
        message = ['Подключение канала доставки уведомлений.'
                   'Подключение "viber" вместе с "telegram".']
        expected_message = ['Подключение канала доставки уведомлений.'
                            'Подключение "viber" вместе с "telegram".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'viber'}

        request_url = f"{lk_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        des_response = response.json()

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert des_response == [{'field': 'phone',
                                     'message': 'Перед подключением уведомлений в viber '
                                                'отключите уведомления в telegram'}]
        except AssertionError:
            message.append(f"Ошибка в теле ответа.")

        assert message == expected_message, message


    def test_post_phone_notify_connect_correct_telegram_again(self):
        message = ['Подключение канала доставки уведомлений.'
                   'Повторное подключение "telegram".']
        expected_message = ['Подключение канала доставки уведомлений.'
                            'Повторное подключение "telegram".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'telegram'}

        request_url = f"{lk_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        des_response = response.json()

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert des_response == [{'field': 'phone',
                                 'message': 'Запрос на подключение уведомлений был отправлен ранее. '
                                            'Ожидается подтверждение подключения'}]
        except AssertionError:
            message.append(f"Ошибка в теле ответа.")

        assert message == expected_message, message


    def test_post_phone_notify_disconnect_correct_telegram(self):
        message = ['Отключение канала доставки уведомлений.'
                   'Отключение "telegram".']
        expected_message = ['Отключение канала доставки уведомлений.'
                            'Отключение "telegram".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'telegram'}

        request_url = f"{lk_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)
        des_response = response.json()

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert des_response[0]['channel'] == 'telegram'
        except AssertionError:
            message.append(f"Параметр 'channel' {des_response[0]['channel']}, а не 'telegram'")
        try:
            assert des_response[0]['name'] == 'Telegram'
        except AssertionError:
            message.append(f"Параметр 'name' {des_response[0]['name']}, а не 'Telegram'")
        try:
            assert des_response[0]['isConnected'] is False
        except AssertionError:
            message.append(f"Параметр 'isConnected' {des_response[0]['isConnected']}, а не 'False'")
        try:
            assert des_response[0]['isAwaitingConfirmation'] is False
        except AssertionError:
            message.append(f"Параметр 'isAwaitingConfirmation' {des_response[0]['isAwaitingConfirmation']}, а не 'False'")

        assert message == expected_message, message


    def test_post_phone_notify_connect_correct_viber(self):
        message = ['Подключение канала доставки уведомлений.'
                   'Подключение "viber".']
        expected_message = ['Подключение канала доставки уведомлений.'
                            'Подключение "viber".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'viber'}

        request_url = f"{lk_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        des_response = response.json()

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert des_response[1]['channel'] == 'viber'
        except AssertionError:
            message.append(f"Параметр 'channel' {des_response[1]['channel']}, а не 'viber'")
        try:
            assert des_response[1]['name'] == 'Viber'
        except AssertionError:
            message.append(f"Параметр 'name' {des_response[1]['name']}, а не 'Viber'")
        try:
            assert des_response[1]['isConnected'] is False
        except AssertionError:
            message.append(f"Параметр 'isConnected' {des_response[1]['isConnected']}, а не 'False'")
        try:
            assert des_response[1]['isAwaitingConfirmation'] is True
        except AssertionError:
            message.append(
                f"Параметр 'isAwaitingConfirmation' {des_response[1]['isAwaitingConfirmation']}, а не 'True'")

        assert message == expected_message, message


    def test_post_phone_notify_connect_correct_telegram_while_viber(self):
        message = ['Подключение канала доставки уведомлений.'
                   'Подключение "telegram" вместе с "viber".']
        expected_message = ['Подключение канала доставки уведомлений.'
                            'Подключение "telegram" вместе с "viber".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'telegram'}

        request_url = f"{lk_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        des_response = response.json()

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert des_response == [{'field': 'phone',
                                     'message': 'Перед подключением уведомлений в telegram '
                                                'отключите уведомления в viber'}]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_phone_notify_connect_correct_viber_again(self):
        message = ['Подключение канала доставки уведомлений.'
                   'Повторное подключение "viber".']
        expected_message = ['Подключение канала доставки уведомлений.'
                            'Повторное подключение "viber".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'viber'}

        request_url = f"{lk_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        des_response = response.json()

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert des_response == [{'field': 'phone',
                                     'message': 'Запрос на подключение уведомлений был отправлен ранее. '
                                                'Ожидается подтверждение подключения'}]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_phone_notify_disconnect_correct_viber(self):
        message = ['Отключение канала доставки уведомлений.'
                   'Отключение "viber".']
        expected_message = ['Отключение канала доставки уведомлений.'
                            'Отключение "viber".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lk_url = "https://api.lk.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'viber'}

        request_url = f"{lk_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)
        des_response = response.json()

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert des_response[1]['channel'] == 'viber'
        except AssertionError:
            message.append(f"Параметр 'channel' {des_response[1]['channel']}, а не 'viber'")
        try:
            assert des_response[1]['name'] == 'Viber'
        except AssertionError:
            message.append(f"Параметр 'name' {des_response[1]['name']}, а не 'Viber'")
        try:
            assert des_response[1]['isConnected'] is False
        except AssertionError:
            message.append(f"Параметр 'isConnected' {des_response[1]['isConnected']}, а не 'False'")
        try:
            assert des_response[1]['isAwaitingConfirmation'] is False
        except AssertionError:
            message.append(
                f"Параметр 'isAwaitingConfirmation' {des_response[1]['isAwaitingConfirmation']}, а не 'False'")

        assert message == expected_message, message

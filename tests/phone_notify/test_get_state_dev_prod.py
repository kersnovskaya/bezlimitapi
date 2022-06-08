import requests

class TestDev:

    def test_successful_getting_state_at_lk(self):
        message = ['Данные по каналам доставки уведомлений на номере.'
                   'Корректный запрос.']
        expected_message = ['Данные по каналам доставки уведомлений на номере.'
                            'Корректный запрос.']

        phone = 9006471111
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'Authorization': f'Bearer {token}'}
        params = {'phone': phone}

        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/state/"
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert i['channel'] in ('telegram', 'viber', 'push')
            except AssertionError:
                message.append(f'В параметре "channel" присутсвует некорректное значение {i["channel"]}')
            try:
                assert i['name'] in ('Telegram', 'Viber', 'Push-уведомления')
            except AssertionError:
                message.append(f'В параметре "channel" присутсвует некорректное значение {i["name"]}')
            try:
                assert i['isConnected'] is not None
            except AssertionError:
                message.append('В параметре "isConnected" отдаётся "None"')
            try:
                assert i['isAwaitingConfirmation'] is not None
            except AssertionError:
                message.append('В параметре "isAwaitingConfirmation" отдаётся "None"')

        assert message == expected_message, message

    def test_validation_getting_state_to_side_phone_at_lk(self):
        message = ['Данные по каналам доставки уведомлений на номере.'
                   'Запрос для стороннего номера.']
        expected_message = ['Данные по каналам доставки уведомлений на номере.'
                            'Запрос для стороннего номера.']

        phone = 9696588825
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'Authorization': f'Bearer {token}'}
        params = {'phone': phone}

        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/state/"
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.reason == 'Data Validation Failed.'
        except AssertionError:
            message.append(f"Причина {response.reason}, а не 'Data Validation Failed'.")
        try:
            assert response.json()[0]['field'] == 'phone'
        except AssertionError:
            message.append(f'В ошибке указано поле {response.json()[0]["field"]}, а не "phone".')
        assert response.json()[0]['message'] == 'Номер телефона не привязан к аккаунту.'

        assert message == expected_message, message


    def test_validation_getting_state_to_wrong_phone_at_lk(self):
        message = ['Данные по каналам доставки уведомлений на номере.'
                   'Некорректный номер.']
        expected_message = ['Данные по каналам доставки уведомлений на номере.'
                            'Некорректный номер.']

        phone = 9696588
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'Authorization': f'Bearer {token}'}
        params = {'phone': phone}

        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/state/"
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.reason == 'Data Validation Failed.'
        except AssertionError:
            message.append(f"Причина {response.reason}, а не 'Data Validation Failed'.")
        try:
            assert response.json()[0]['field'] == 'phone'
        except AssertionError:
            message.append(f'В ошибке указано поле {response.json()[0]["field"]}, а не "phone".')
        try:
            assert response.json()[0]['message'] == 'Введите номер телефона в формате 9001112233.'
        except AssertionError:
            message.append('Ошибка в сообщении ошибки.')

        assert message == expected_message, message


    def test_validation_getting_state_to_not_numeric_phone_at_lk(self):
        message = ['Данные по каналам доставки уведомлений на номере.'
                   'Текст в поле "phone".']
        expected_message = ['Данные по каналам доставки уведомлений на номере.'
                            'Текст в поле "phone".']

        phone = '♂CUM♂mit'
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'Authorization': f'Bearer {token}'}
        params = {'phone': phone}

        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/state/"
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 400
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 400.")
        try:
            assert response.reason == 'Bad Request'
        except AssertionError:
            message.append(f"Причина {response.reason}, а не 'Bad Request'.")
        try:
            assert type(response.json()) == dict
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
        try:
            assert response.json()['message'] == 'Неправильное значение параметра "phone".'
        except AssertionError:
            message.append('Ошибка в сообщении ошибки.')

        assert message == expected_message, message


    def test_unsuccessful_getting_notifications_without_token_at_lk(self):
        message = ['Данные по каналам доставки уведомлений на номере.'
                   'Неавторизован.']
        expected_message = ['Данные по каналам доставки уведомлений на номере.'
                            'Неавторизован.']

        phone = '♂CUM♂mit'
        token = 12345678910
        headers = {'Authorization': f'Bearer {token}'}
        params = {'phone': phone}

        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/state/"
        response = requests.get(request_url, headers=headers, params=params)

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


class TestProd:

    def test_successful_getting_state_at_lk(self):
        message = ['Данные по каналам доставки уведомлений на номере.'
                   'Корректный запрос.']
        expected_message = ['Данные по каналам доставки уведомлений на номере.'
                            'Корректный запрос.']

        phone = 9006471111
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'Authorization': f'Bearer {token}'}
        params = {'phone': phone}

        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/state/"
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert i['channel'] in ('telegram', 'viber', 'push')
            except AssertionError:
                message.append(f'В параметре "channel" присутсвует некорректное значение {i["channel"]}')
            try:
                assert i['name'] in ('Telegram', 'Viber', 'Push-уведомления')
            except AssertionError:
                message.append(f'В параметре "channel" присутсвует некорректное значение {i["name"]}')
            try:
                assert i['isConnected'] is not None
            except AssertionError:
                message.append('В параметре "isConnected" отдаётся "None"')
            try:
                assert i['isAwaitingConfirmation'] is not None
            except AssertionError:
                message.append('В параметре "isAwaitingConfirmation" отдаётся "None"')

        assert message == expected_message, message

    def test_validation_getting_state_to_side_phone_at_lk(self):
        message = ['Данные по каналам доставки уведомлений на номере.'
                   'Запрос для стороннего номера.']
        expected_message = ['Данные по каналам доставки уведомлений на номере.'
                            'Запрос для стороннего номера.']

        phone = 9696588825
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'Authorization': f'Bearer {token}'}
        params = {'phone': phone}

        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/state/"
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.reason == 'Data Validation Failed.'
        except AssertionError:
            message.append(f"Причина {response.reason}, а не 'Data Validation Failed'.")
        try:
            assert response.json()[0]['field'] == 'phone'
        except AssertionError:
            message.append(f'В ошибке указано поле {response.json()[0]["field"]}, а не "phone".')
        assert response.json()[0]['message'] == 'Номер телефона не привязан к аккаунту.'

        assert message == expected_message, message


    def test_validation_getting_state_to_wrong_phone_at_lk(self):
        message = ['Данные по каналам доставки уведомлений на номере.'
                   'Некорректный номер.']
        expected_message = ['Данные по каналам доставки уведомлений на номере.'
                            'Некорректный номер.']

        phone = 9696588
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'Authorization': f'Bearer {token}'}
        params = {'phone': phone}

        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/state/"
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.reason == 'Data Validation Failed.'
        except AssertionError:
            message.append(f"Причина {response.reason}, а не 'Data Validation Failed'.")
        try:
            assert response.json()[0]['field'] == 'phone'
        except AssertionError:
            message.append(f'В ошибке указано поле {response.json()[0]["field"]}, а не "phone".')
        try:
            assert response.json()[0]['message'] == 'Введите номер телефона в формате 9001112233.'
        except AssertionError:
            message.append('Ошибка в сообщении ошибки.')

        assert message == expected_message, message


    def test_validation_getting_state_to_not_numeric_phone_at_lk(self):
        message = ['Данные по каналам доставки уведомлений на номере.'
                   'Текст в поле "phone".']
        expected_message = ['Данные по каналам доставки уведомлений на номере.'
                            'Текст в поле "phone".']

        phone = '♂CUM♂mit'
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'Authorization': f'Bearer {token}'}
        params = {'phone': phone}

        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/state/"
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 400
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 400.")
        try:
            assert response.reason == 'Bad Request'
        except AssertionError:
            message.append(f"Причина {response.reason}, а не 'Bad Request'.")
        try:
            assert type(response.json()) == dict
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
        try:
            assert response.json()['message'] == 'Неправильное значение параметра "phone".'
        except AssertionError:
            message.append('Ошибка в сообщении ошибки.')

        assert message == expected_message, message


    def test_unsuccessful_getting_notifications_without_token_at_lk(self):
        message = ['Данные по каналам доставки уведомлений на номере.'
                   'Неавторизован.']
        expected_message = ['Данные по каналам доставки уведомлений на номере.'
                            'Неавторизован.']

        phone = '♂CUM♂mit'
        token = 12345678910
        headers = {'Authorization': f'Bearer {token}'}
        params = {'phone': phone}

        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/state/"
        response = requests.get(request_url, headers=headers, params=params)

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

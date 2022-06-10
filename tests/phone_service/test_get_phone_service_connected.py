import requests


class Test:

    def test_get_connected_service_correct(self):
        message = ['Подключенные услуги.'
                   'Корректный запрос.']
        expected_message = ['Подключенные услуги.'
                            'Корректный запрос.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        params = {'phone': 9006471111}
        lk_url = "https://lktest.bezlimit.ru/v1"

        request_url = f"{lk_url}/phone/service/connected"
        response = requests.post(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        try:
            for i in response.json():
                assert type(i['id']) == int
                assert type(i['title']) == str
                assert type(i['short_description']) == str
                assert type(i['description']) == str
                assert type(i['connection_cost']) == str
        except AssertionError:
            message.append('В ответе используются некорректные типы данных.')
        assert message == expected_message, message

    def test_get_connected_service_list_without_token(self):
        message = ['Подключенные услуги.'
                   'Не авторизован.']
        expected_message = ['Подключенные услуги.'
                            'Не авторизован.']

        token = 'gym'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        params = {'phone': 9006471111}
        lk_url = "https://lktest.bezlimit.ru/v1"

        request_url = f"{lk_url}/phone/service/connected"
        response = requests.post(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 401
        except BaseException:
            message.append(f"Код ответа {response.status_code}, а не 401.")
        try:
            assert response.reason == 'Unauthorized'
        except BaseException:
            message.append(f"Причина {response.reason}, а не 'Unauthorized'.")
        try:
            assert response.json()['message'] == 'Your request was made with invalid credentials.'
        except BaseException:
            message.append('Ошибка в сообщении ошибки.')

        assert message == expected_message, message

    def test_get_connected_service_list_not_bezlimit_phone(self):
        message = ['Подключенные услуги.'
                   'Не авторизован.']
        expected_message = ['Подключенные услуги.'
                            'Не авторизован.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        params = {'phone': 9000000000}
        lk_url = "https://lktest.bezlimit.ru/v1"

        request_url = f"{lk_url}/phone/service/connected"
        response = requests.post(request_url, headers=headers, params=params)

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

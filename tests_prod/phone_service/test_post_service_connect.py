import requests

req_url = 'https://api.lk.bezlimit.ru/v1/phone/service/connect'
test_phone = 9682221928
acc_token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'

class TestValidationProd:
    def test_unauthorized(self):
        message = ['Отключение услуги. Не авторизован.']
        expected_message = ['Отключение услуги. Не авторизован.']

        headers = {
            'accept': '*/*',
            'Authorization': 'Bearer 123456789',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(req_url, headers=headers)

        print(response.json())

        try:
            assert response.status_code == 401
        except AssertionError:
            message.append(f'Код ответа "{response.status_code}", а не "422".')
        try:
            assert response.json() == {
                'name': 'Unauthorized',
                'message': 'Your request was made with invalid credentials.',
                'code': 0,
                'status': 401
            }
        except AssertionError:
            message.append(f'Ошибка в тексте ответа: {response.json()}')

        assert message == expected_message, message


    def test_incorrect_phone_and_id(self):
        message = ['Отключение услуги. Некорректные номер и id.']
        expected_message = ['Отключение услуги. Некорректные номер и id.']

        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {acc_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            "id": 123456,
            "phone": 123456
        }

        response = requests.post(req_url, headers=headers, data=data)

        print(response.json())

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа "{response.status_code}", а не "422".')
        try:
            assert response.json() == [
                {
                    'field': 'phone',
                    'message': 'Введите номер телефона в формате 9001112233.'
                },
                {
                    'field': 'id',
                    'message': 'Услуга не найдена.'
                }
            ]
        except AssertionError:
            message.append(f'Ошибка в тексте ответа: {response.json()}')

        assert message == expected_message, message


    def test_incorrect_not_bezlimit_phone(self):
        message = ['Отключение услуги. Номер не Безлимит.']
        expected_message = ['Отключение услуги. Номер не Безлимит.']

        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {acc_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            "id": 8019,
            "phone": 9000000000
        }

        response = requests.post(req_url, headers=headers, data=data)

        print(response.json())

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа "{response.status_code}", а не "422".')
        try:
            assert response.json() == [
                {
                    'field': 'phone',
                    'message': 'Введенный номер не обслуживается в Безлимит!'
                },
                {
                    'field': 'id',
                    'message': 'Услуга не найдена.'
                }
            ]
        except AssertionError:
            message.append(f'Ошибка в тексте ответа: {response.json()}')

        assert message == expected_message, message


    def test_incorrect_string_phone(self):
        message = ['Отключение услуги. Номер в формате "str", а не "int".']
        expected_message = ['Отключение услуги. Номер в формате "str", а не "int".']

        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {acc_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            "id": '9000000000',
            "phone": 8019
        }

        response = requests.post(req_url, headers=headers, data=data)

        print(response.json())

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа "{response.status_code}", а не "422".')
        try:
            assert response.json() == [
                {
                    'field': 'phone',
                    'message': 'Введите номер телефона в формате 9001112233.'
                },
                {
                    'field': 'id',
                    'message': 'Услуга не найдена.'
                }
            ]
        except AssertionError:
            message.append(f'Ошибка в тексте ответа: {response.json()}')

        assert message == expected_message, message


    def test_incorrect_not_account_phone(self):
        message = ['Отключение услуги. Номер не привязан к аккаунту.']
        expected_message = ['Отключение услуги. Номер не привязан к аккаунту.']

        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {acc_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            "id": 8019,
            "phone": 9612224930
        }

        response = requests.post(req_url, headers=headers, data=data)

        print(response.json())

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа "{response.status_code}", а не "422".')
        try:
            assert response.json() == [
                {
                    'field': 'phone', 'message': 'Номер телефона не привязан к аккаунту.'
                },
                {
                    'field': 'id',
                    'message': 'Услуга не найдена.'
                }
            ]
        except AssertionError:
            message.append(f'Ошибка в тексте ответа: {response.json()}')

        assert message == expected_message, message


    def test_incorrect_incorrect_id(self):
        message = ['Отключение услуги. На номере нет услуги из запроса.']
        expected_message = ['Отключение услуги. На номере нет услуги из запроса.']

        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {acc_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            "id": 8019,
            "phone": 9682224036
        }

        response = requests.post(req_url, headers=headers, data=data)

        print(response.json())

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа "{response.status_code}", а не "422".')
        try:
            assert response.json() == [
                {
                    'field': 'id',
                    'message': 'Услуга не найдена.'
                }
            ]
        except AssertionError:
            message.append(f'Ошибка в тексте ответа: {response.json()}')

        assert message == expected_message, message

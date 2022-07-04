import requests
import random


req_url = 'https://lktest.bezlimit.ru/v1/phone/service/available'
test_phone = 9682221928
acc_token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'


class TestValidationDev:
    def test_unauthorized(self):
        message = ['Доступные для подключения услуги на номере. Не авторизован.']
        expected_message = ['Доступные для подключения услуги на номере. Не авторизован.']

        headers = {
            
            'Authorization': 'Bearer 123456789',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.get(req_url, headers=headers)

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
                'status': 401,
                'type': 'yii\\web\\UnauthorizedHttpException'
            }
        except AssertionError:
            message.append(f'Ошибка в тексте ответа: {response.json()}')

        assert message == expected_message, message


    def test_incorrect_phone(self):
        message = ['Доступные для подключения услуги на номере. Некорректные номер.']
        expected_message = ['Доступные для подключения услуги на номере. Некорректные номер.']

        headers = {
            
            'Authorization': f'Bearer {acc_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        params = {
            "phone": 123456
        }

        response = requests.get(req_url, headers=headers, params=params)

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
                }
            ]
        except AssertionError:
            message.append(f'Ошибка в тексте ответа: {response.json()}')

        assert message == expected_message, message


    def test_incorrect_not_bezlimit_phone(self):
        message = ['Доступные для подключения услуги на номере. Номер не Безлимит.']
        expected_message = ['Доступные для подключения услуги на номере. Номер не Безлимит.']

        headers = {
            
            'Authorization': f'Bearer {acc_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        params = {
            "phone": 9000000000
        }

        response = requests.get(req_url, headers=headers, params=params)

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
                }
            ]
        except AssertionError:
            message.append(f'Ошибка в тексте ответа: {response.json()}')

        assert message == expected_message, message


    def test_incorrect_not_account_phone(self):
        message = ['Доступные для подключения услуги на номере. Номер не привязан к аккаунту.']
        expected_message = ['Доступные для подключения услуги на номере. Номер не привязан к аккаунту.']

        headers = {
            
            'Authorization': f'Bearer {acc_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        params = {
            "phone": 9006471111
        }

        response = requests.get(req_url, headers=headers, params=params)

        print(response.json())

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа "{response.status_code}", а не "422".')
        try:
            assert response.json() == [
                {
                    'field': 'phone', 'message': 'Номер телефона не привязан к аккаунту.'
                }
            ]
        except AssertionError:
            message.append(f'Ошибка в тексте ответа: {response.json()}')

        assert message == expected_message, message


    def test_correct_request(self):
        message = ['Доступные для подключения услуги на номере. Корректный запрос.']
        expected_message = ['Доступные для подключения услуги на номере. Корректный запрос.']

        headers = {
            'Authorization': f'Bearer {acc_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        params = {
            "phone": test_phone
        }

        response = requests.get(req_url, headers=headers, params=params)

        keys = [
            'id',
            'title',
            'short_description',
            'description',
            'type',
            'payment_period',
            'connection_cost',
            'subscription_fee',
            'can_be_deferred',
            'cannot_be_disabled',
            'is_cannot_disconnect_in_lk',
            'is_hit',
            'is_confirmed_passport_required'
        ]

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа "{response.status_code}", а не "200".')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных в ответе "{type(response.json())}", а не "list".')
        for i in response.json():
            sub_keys = keys[:]
            try:
                assert type(i) == dict
            except AssertionError:
                message.append(f'В ответе услуга предоставляются в формате "{type(i)}", а не "dict".')
            try:
                if "Продли скорость" in i['title']:
                    sub_keys.append('packet_value')
                assert list(i.keys()) == sub_keys
            except AssertionError:
                difference = set(keys).difference(list(i.keys()))
                message.append(
                    'В услуге "{0}", ID = "{1}" отсутствуют ключи: {2}.'.format(
                        i['title'],
                        i['id'],
                        difference
                    )
                )


        assert message == expected_message, message


    def test_incorrect_correct_request_pagination(self):
        message = ['Доступные для подключения услуги на номере. Проверка пагинации.']
        expected_message = ['Доступные для подключения услуги на номере. Проверка пагинации.']

        headers = {

            'Authorization': f'Bearer {acc_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        page = random.randint(1, 10)
        params = {
            "phone": test_phone,
            "page": page
        }

        response = requests.get(req_url, headers=headers, params=params)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа "{response.status_code}", а не "200".')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных в ответе "{type(response.json())}", а не "list".')
        try:
            assert response.headers['x-pagination-current-page'] == str(page)
        except AssertionError:
            message.append(f'Заголовках указана текущая страница "{response.headers["x-pagination-current-page"]}",'
                           f'должно быть "{page}".')

        assert message == expected_message, message

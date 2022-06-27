import requests


class TestDev:
    def test_not_authorized(self):
        message = ['Удаление аккаунта ЛК. Не авторизован.']
        expected_message = ['Удаление аккаунта ЛК. Не авторизован.']

        phone = 9696588825
        url = f"https://lktest.bezlimit.ru/v1/system/phone/{phone}"
        headers = {'accept': '*/*'}

        response = requests.delete(url, headers=headers)

        print('\n', response.json())

        try:
            assert response.status_code == 401
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 401.')
        try:
            assert response.json() == {
                'name': 'Unauthorized',
                'message': 'Your request was made with invalid credentials.',
                'code': 0,
                'status': 401,
                'type': 'yii\\web\\UnauthorizedHttpException'
            }
        except AssertionError:
            message.append(f'Ошибка в теле ответа: {response.json()}')

        assert message == expected_message, message

    def test_not_bezlimit_phone(self):
        message = ['Удаление аккаунта ЛК. Не авторизован.']
        expected_message = ['Удаление аккаунта ЛК. Не авторизован.']

        phone = 9000000000
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        url = f"https://lktest.bezlimit.ru/v1/system/phone/{phone}"
        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {token}'
        }
        response = requests.delete(url, headers=headers)

        print('\n', response.json())

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert response.json() == [
                {
                    'field': 'phone',
                    'message': 'Введенный номер не обслуживается в Безлимит!'
                }
            ]
        except AssertionError:
            message.append(f'Ошибка в теле ответа: {response.json()}')

        assert message == expected_message, message


    def test_not_incorrect_phone(self):
        message = ['Удаление аккаунта ЛК. Не авторизован.']
        expected_message = ['Удаление аккаунта ЛК. Не авторизован.']

        phone = 1234
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        url = f"https://lktest.bezlimit.ru/v1/system/phone/{phone}"
        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {token}'
        }
        response = requests.delete(url, headers=headers)

        print('\n', response.json())

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert response.json() == [
                {
                    'field': 'phone',
                    'message': 'Введите номер телефона в формате 9001112233.'
                }
            ]
        except AssertionError:
            message.append(f'Ошибка в теле ответа: {response.json()}')

        assert message == expected_message, message

import requests


DOMAIN_DEV = 'https://lktest.bezlimit.ru/v1'
request_url = '{0}/user/auth/registration-create-account/'.format(DOMAIN_DEV)

class TestDev:
    def test_post_registration_empty_data(self):
        message = ['Регистрация номера в ЛК. Отправка пустого запроса.']
        expected_message = ['Регистрация номера в ЛК. Отправка пустого запроса.']
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "phone": None,
            "confirmedToken": None,
            "newPassword": None,
            "newPasswordRepeat": None
        }
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert response.json() == [
                {
                    'field': 'phone',
                    'message': 'Не указан номер телефона.'
                },
                {
                    'field': 'confirmedToken',
                    'message': 'Необходимо заполнить «Confirmed Token».'
                },
                {
                    'field': 'newPassword',
                    'message': 'Необходимо заполнить «New Password».'
                },
                {
                    'field': 'newPasswordRepeat',
                    'message': 'Необходимо заполнить «New Password Repeat».'
                }
            ]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message

    def test_post_registration_incorrect_data(self):
        message = ['Регистрация номера в ЛК. Отправка некорректных данных.']
        expected_message = ['Регистрация номера в ЛК. Отправка некорректных данных.']
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "phone": 1488,
            "confirmedToken": 1488,
            "newPassword": 1488,
            "newPasswordRepeat": 1488
        }
        response = requests.post(request_url, headers=headers, data=data)

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
                },
                {
                    'field': 'newPassword',
                    'message': 'Пароль должен быть не менее 8 символов.'
                },
                {
                    'field': 'newPasswordRepeat',
                    'message': 'Пароль должен быть не менее 8 символов.'
                 },
                {
                    'field': 'confirmedToken',
                    'message': 'Не верный токен подтверждения пароля!'
                }
            ]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message

    def test_post_registration_not_bezlimit_phone(self):
        message = ['Регистрация номера в ЛК. Номер не Безлимит.']
        expected_message = ['Регистрация номера в ЛК. Номер не Безлимит.']
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "phone": 9000000000,
            "confirmedToken": '1488',
            "newPassword": 'Aa123456',
            "newPasswordRepeat": 'Aa123456'
        }
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert response.json() == [
                {
                    'field': 'phone',
                    'message': 'Введенный номер не обслуживается в Безлимит!'
                },
                {
                    'field': 'confirmedToken',
                    'message': 'Не верный токен подтверждения пароля!'
                }
            ]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message

    def test_post_registration_incorrect_passwords(self):
        message = ['Регистрация номера в ЛК. Номер не Безлимит.']
        expected_message = ['Регистрация номера в ЛК. Номер не Безлимит.']
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "phone": 9618880491,
            "confirmedToken": '1488',
            "newPassword": 'хуйпиздасковорода',
            "newPasswordRepeat": 'хуйпиздасковорода'
        }
        response = requests.post(request_url, headers=headers, data=data)

        print('\n', response.json())

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert response.json() == [
                {
                    'field': 'newPassword',
                    'message': 'Ввод возможен только букв латинского алфавита (большие и маленькие), цифр, спецсимволов.'
                },
                {
                    'field': 'newPasswordRepeat',
                    'message': 'Ввод возможен только букв латинского алфавита (большие и маленькие), цифр, спецсимволов.'
                 },
                {
                    'field': 'confirmedToken',
                    'message': 'Не верный токен подтверждения пароля!'
                }
            ]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_registration_different_passwords(self):
        message = ['Регистрация номера в ЛК. Пароли не совпадают.']
        expected_message = ['Регистрация номера в ЛК. Пароли не совпадают.']
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "phone": 9618880491,
            "confirmedToken": '1488',
            "newPassword": 'Aa123456',
            "newPasswordRepeat": 'Aa12345678910'
        }
        response = requests.post(request_url, headers=headers, data=data)

        print('\n', response.json())

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert response.json() == [
                {
                    "field": "newPassword",
                    "message": "Введеные пароли не совпадают!"
                },
                {
                    'field': 'confirmedToken',
                    'message': 'Не верный токен подтверждения пароля!'
                }
            ]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message

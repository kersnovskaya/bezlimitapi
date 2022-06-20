import requests


class TestDev:

    def test_post_request_password_reset_code_very_invalid_phone(self):
        message = ['Проверка кода подтверждения для восстановления пароля. Номер на ПА.']
        expected_message = ['Проверка кода подтверждения для восстановления пароля. Номер на ПА.']

        headers = {'accept': 'application/json',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9612225034,
            "code": 123456
        }
        request_url = f"{lktest_url}/user/auth/request-password-reset-code-confirmation"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [
                {
                    "field": "phone",
                    "message": "Номер телефона не активирован!"
                }
            ]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')
        assert message == expected_message, message


    def test_post_request_password_reset_code_invalid_phone(self):
        message = ['Проверка кода подтверждения для восстановления пароля. Некорректный номер телефона.']
        expected_message = ['Проверка кода подтверждения для восстановления пароля. Некорректный номер телефона.']

        headers = {'accept': 'application/json',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }

        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 123546,
            "code": '123456'
        }

        request_url = f"{lktest_url}/user/auth/request-password-reset-code-confirmation"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [
                {
                    "field": "phone",
                    "message": "Введите номер телефона в формате 9001112233."
                }
            ]
        except AssertionError:
            message.append('В тексте ответа ошибка.')

        assert message == expected_message, message


    def test_post_request_password_reset_code_not_bezlimit_phone(self):
        message = ['Проверка кода подтверждения для восстановления пароля. Номер не Безлимит.']
        expected_message = ['Проверка кода подтверждения для восстановления пароля. Номер не Безлимит.']

        headers = {'accept': 'application/json',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }

        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9000000000,
            "code": '123456'
        }

        request_url = f"{lktest_url}/user/auth/request-password-reset-code-confirmation"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [
                {
                    "field": "phone",
                    "message": "Введенный номер не обслуживается в Безлимит!"
                }
            ]
        except AssertionError:
            message.append('В тексте ответа ошибка.')

        assert message == expected_message, message


    def test_post_request_password_reset_code_empty_phone(self):
        message = ['Запрос на восстановление пароля. Пустое поле "phone".']
        expected_message = ['Запрос на восстановление пароля. Пустое поле "phone".']

        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = None
        data = {"phone": phone,
                "code": 123456}
        headers = {"accept": "application/json"}

        request_url = f'{lktest_url}/user/auth/request-password-reset-code-confirmation'
        response = requests.post(request_url, headers=headers, data=data)
        print('\n', response.json())
        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert response.reason == 'Data Validation Failed.'
        except AssertionError:
            message.append(f'Код ответа "{response.reason}", а не "Data Validation Failed.".')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "list".')
        for i, v in enumerate(response.json()):
            try:
                assert v['message'] == 'Не указан номер телефона.'
            except AssertionError:
                message.append('Ошибка в параметре ответа "message".')
            try:
                assert v['field'] == 'phone'
            except AssertionError:
                message.append('Ошибка в параметре ответа "field".')

        assert message == expected_message, message


    def test_post_request_password_reset_code_phone_without_account(self):
        message = ['Запрос на восстановление пароля. На номере нет аккаунта ЛК/Сторонний аккаунт ЛК.']
        expected_message = ['Запрос на восстановление пароля. На номере нет аккаунта ЛК/Сторонний аккаунт ЛК.']

        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9618880491
        data = {"phone": phone,
                "code": 123456}
        headers = {"accept": "application/json"}

        request_url = f'{lktest_url}/user/auth/request-password-reset-code-confirmation'
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 200.')
        try:
            assert response.json() == {
                "message": 'Номер не найден в системе \"Безлимит ID\"'
            }
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_post_request_password_reset_code_phone_without_code(self):
        message = ['Запрос на восстановление пароля. На номере нет аккаунта ЛК/Сторонний аккаунт ЛК.']
        expected_message = ['Запрос на восстановление пароля. На номере нет аккаунта ЛК/Сторонний аккаунт ЛК.']

        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9682223055
        data = {"phone": phone,
                "code": None}
        headers = {"accept": "application/json"}

        request_url = f'{lktest_url}/user/auth/request-password-reset-code-confirmation'
        response = requests.post(request_url, headers=headers, data=data)
        print('\n', response.json())

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "list".')
        for i, v in enumerate(response.json()):
            try:
                assert v['message'] == 'Введите код подтверждения'
            except AssertionError:
                message.append('Ошибка в параметре ответа "message".')
            try:
                assert v['field'] == 'code'
            except AssertionError:
                message.append('Ошибка в параметре ответа "code".')

        assert message == expected_message, message


    def test_post_request_password_reset_code_phone_string_code(self):
        message = ['Запрос на восстановление пароля. На номере нет аккаунта ЛК/Сторонний аккаунт ЛК.']
        expected_message = ['Запрос на восстановление пароля. На номере нет аккаунта ЛК/Сторонний аккаунт ЛК.']

        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9682223055
        data = {"phone": phone,
                "code": 'None'}
        headers = {"accept": "application/json"}

        request_url = f'{lktest_url}/user/auth/request-password-reset-code-confirmation'
        response = requests.post(request_url, headers=headers, data=data)
        print('\n', response.json())

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "list".')
        for i, v in enumerate(response.json()):
            try:
                assert v['message'] == 'Значение «Код подтверждения» должно быть целым числом.'
            except AssertionError:
                message.append('Ошибка в параметре ответа "message".')
            try:
                assert v['field'] == 'code'
            except AssertionError:
                message.append('Ошибка в параметре ответа "code".')

        assert message == expected_message, message

    def test_post_request_password_reset_code_phone_incorrect_code(self):
        message = ['Запрос на восстановление пароля. На номере нет аккаунта ЛК/Сторонний номер аккаунта.']
        expected_message = ['Запрос на восстановление пароля. На номере нет аккаунта ЛК/Сторонний номер аккаунта.']

        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9612224930
        data = {"phone": phone,
                "code": 12345}
        headers = {"accept": "application/json"}

        request_url = f'{lktest_url}/user/auth/request-password-reset-code-confirmation'
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert response.json() == [
                {
                    "field": "code",
                    "message": "Проверочный код указан не верно!"
                }
            ]
        except AssertionError:
            message.append(f'Ошибка в теле ответа - {response.json()[0]["message"]}, '
                           f'должно быть "Проверочный код указан не верно!".')
        assert message == expected_message, message

import requests


def get_code(phone):
    token = 'Z1RseVcn9twtKLY84eYQf57Pw8ENZ1yks436TJHXaC2dJhcRZLJ2mGsgRBpTuFp7'
    url = "https://api.bezlimit.ru/v1"
    headers = {'accept': 'application/json',
               'authorization': 'Basic YXBpOldHZnpzQWlKYkxa',
               'Api-Token': token}
    params = {'phone': phone}
    request_url = f"{url}/queue/sms"
    response = requests.get(request_url, headers=headers, params=params)
    raw_answer = response.json()
    for i in raw_answer['items']:
        raw_code = i['text']
        break
    code = int(raw_code.split()[-1])
    print('\n', code)
    return code


def password_reset_token(phone):
    lktest_url = "https://lktest.bezlimit.ru/v1"
    code = get_code(phone)
    params = {"phone": phone,
              "code": code}
    headers = {"accept": "application/json",
               "Content-Type": "application/x-www-form-urlencoded"}

    request_url = f'{lktest_url}/user/auth/request-password-reset-code-confirmation'
    response = requests.post(request_url, headers=headers, data=params)
    print('\n', response.json())
    token = response.json()['confirmed_token']

    return token


class TestDev:
    """
    Набор кейсов для Дева ниже:
    """

    def test_reset_password_empty_data(self):
        message = ['Смена забытого пароля. Пустые "data".']
        expected_message = ['Смена забытого пароля. Пустые "data".']

        lktest_url = "https://lktest.bezlimit.ru/v1"
        params = {'phone': None,
                  'confirmedToken': None,
                  'newPassword': None,
                  'newPasswordRepeat': None}
        headers = {"accept": "*/*",
                   'Content-Type': 'application/x-www-form-urlencoded'}

        request_url = f'{lktest_url}/user/auth/reset-password'
        response = requests.put(request_url, headers=headers, data=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert type(i) == dict
            except AssertionError:
                message.append(f'Ошибка в ответе по параметру "{i["field"]}", тип данных {type(i)} а не "dict".')

        assert message == expected_message, message


    def test_reset_password_incorrect_data(self):
        message = ['Смена забытого пароля. Некорректные "data".']
        expected_message = ['Смена забытого пароля. Некорректные "data".']

        lktest_url = "https://lktest.bezlimit.ru/v1"
        params = {'phone': 1234,
                  'confirmedToken': 'None',
                  'newPassword': 'None',
                  'newPasswordRepeat': 'None'}
        headers = {"accept": "*/*",
                   'Content-Type': 'application/x-www-form-urlencoded'}

        request_url = f'{lktest_url}/user/auth/reset-password'
        response = requests.put(request_url, headers=headers, data=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert list(filter(lambda item: item['field'] == 'phone', response.json())) == [
                {
                    "field": "phone",
                    "message": "Введите номер телефона в формате 9001112233."
                }
            ]
        except AssertionError:
            message.append('Не отдаётся ответ по параметру "phone".')
        try:
            assert list(filter(lambda item: item['field'] == 'confirmedToken', response.json())) == [
                {
                    'field': 'confirmedToken',
                    'message': 'Не верный токен подтверждения пароля!'
                }
            ]
        except AssertionError:
            message.append('Не отдаётся ответ по параметру "confirmedToken".')
        try:
            assert list(filter(lambda item: item['field'] == 'newPassword', response.json())) == [
                {
                    'field': 'newPassword',
                    'message': 'Пароль должен быть не менее 8 символов.'
                }
            ]
        except AssertionError:
            message.append('Не отдаётся ответ по параметру "newPassword".')
        try:
            assert list(filter(lambda item: item['field'] == 'newPasswordRepeat', response.json())) == [
                {
                    'field': 'newPasswordRepeat',
                    'message': 'Пароль должен быть не менее 8 символов.'
                }
            ]
        except AssertionError:
            message.append('Не отдаётся ответ по параметру "newPasswordRepeat".')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert type(i) == dict
            except AssertionError:
                message.append(f'Ошибка в ответе по параметру "{i["field"]}", тип данных {type(i)} а не "dict".')

        assert message == expected_message, message


    def test_reset_password_different_passwords(self):
        message = ['Смена забытого пароля. Пароли не совпадают.']
        expected_message = ['Смена забытого пароля. Пароли не совпадают.']

        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9682224036
        token = password_reset_token(phone)
        params = {'phone': phone,
                  'confirmedToken': token,
                  'newPassword': 'Aa123456',
                  'newPasswordRepeat': 'Aa1234567'}
        headers = {"accept": "*/*",
                   'Content-Type': 'application/x-www-form-urlencoded'}

        request_url = f'{lktest_url}/user/auth/reset-password'
        response = requests.put(request_url, headers=headers, data=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert type(i) == dict
            except AssertionError:
                message.append(f'Ошибка в ответе по параметру "{i["field"]}", тип данных {type(i)} а не "dict".')
        try:
            assert response.json() == [{'field': 'newPassword', 'message': 'Введеные пароли не совпадают!'}]
        except AssertionError:
            message.append(f'В теле ответа отдаётся неверный текст: {response.json()}')
        assert message == expected_message, message


    def test_reset_password_incorrect_passwords(self):
        message = ['Смена забытого пароля. Пароли не совпадают.']
        expected_message = ['Смена забытого пароля. Пароли не совпадают.']

        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9682224036
        token = password_reset_token(phone)
        params = {'phone': phone,
                  'confirmedToken': token,
                  'newPassword': 'а!"№"!%%!',
                  'newPasswordRepeat': 'а!"№"!%%!'}
        headers = {"accept": "*/*",
                   'Content-Type': 'application/x-www-form-urlencoded'}

        request_url = f'{lktest_url}/user/auth/reset-password'
        response = requests.put(request_url, headers=headers, data=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert type(i) == dict
            except AssertionError:
                message.append(f'Ошибка в ответе по параметру "{i["field"]}", тип данных {type(i)} а не "dict".')
        try:
            assert response.json() == [
                {
                    "field": "newPassword",
                    "message": "Ввод возможен только букв латинского алфавита (большие и маленькие), цифр, спецсимволов."
                },
                {
                    "field": "newPasswordRepeat",
                    "message": "Ввод возможен только букв латинского алфавита (большие и маленькие), цифр, спецсимволов."
                }
            ]
        except AssertionError:
            message.append(f'В теле ответа отдаётся неверный текст: {response.json()}')
        assert message == expected_message, message


class TestProd:
    """
    Набор кейсов для Прода ниже:
    """
    def test_reset_password_empty_data(self):
        message = ['Смена забытого пароля. Пустые "data".']
        expected_message = ['Смена забытого пароля. Пустые "data".']

        lktest_url = "https://api/lk.bezlimit.ru/v1"
        params = {'phone': None,
                  'confirmedToken': None,
                  'newPassword': None,
                  'newPasswordRepeat': None}
        headers = {"accept": "*/*",
                   'Content-Type': 'application/x-www-form-urlencoded'}

        request_url = f'{lktest_url}/user/auth/reset-password'
        response = requests.put(request_url, headers=headers, data=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert type(i) == dict
            except AssertionError:
                message.append(f'Ошибка в ответе по параметру "{i["field"]}", тип данных {type(i)} а не "dict".')

        assert message == expected_message, message


    def test_reset_password_incorrect_data(self):
        message = ['Смена забытого пароля. Некорректные "data".']
        expected_message = ['Смена забытого пароля. Некорректные "data".']

        lktest_url = "https://api/lk.bezlimit.ru/v1"
        params = {'phone': 1234,
                  'confirmedToken': 'None',
                  'newPassword': 'None',
                  'newPasswordRepeat': 'None'}
        headers = {"accept": "*/*",
                   'Content-Type': 'application/x-www-form-urlencoded'}

        request_url = f'{lktest_url}/user/auth/reset-password'
        response = requests.put(request_url, headers=headers, data=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert list(filter(lambda item: item['field'] == 'phone', response.json())) == [
                {
                    "field": "phone",
                    "message": "Введите номер телефона в формате 9001112233."
                }
            ]
        except AssertionError:
            message.append('Не отдаётся ответ по параметру "phone".')
        try:
            assert list(filter(lambda item: item['field'] == 'confirmedToken', response.json())) == [
                {
                    'field': 'confirmedToken',
                    'message': 'Не верный токен подтверждения пароля!'
                }
            ]
        except AssertionError:
            message.append('Не отдаётся ответ по параметру "confirmedToken".')
        try:
            assert list(filter(lambda item: item['field'] == 'newPassword', response.json())) == [
                {
                    'field': 'newPassword',
                    'message': 'Пароль должен быть не менее 8 символов.'
                }
            ]
        except AssertionError:
            message.append('Не отдаётся ответ по параметру "newPassword".')
        try:
            assert list(filter(lambda item: item['field'] == 'newPasswordRepeat', response.json())) == [
                {
                    'field': 'newPasswordRepeat',
                    'message': 'Пароль должен быть не менее 8 символов.'
                }
            ]
        except AssertionError:
            message.append('Не отдаётся ответ по параметру "newPasswordRepeat".')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert type(i) == dict
            except AssertionError:
                message.append(f'Ошибка в ответе по параметру "{i["field"]}", тип данных {type(i)} а не "dict".')

        assert message == expected_message, message


    def test_reset_password_different_passwords(self):
        message = ['Смена забытого пароля. Пароли не совпадают.']
        expected_message = ['Смена забытого пароля. Пароли не совпадают.']

        lktest_url = "https://api/lk.bezlimit.ru/v1"
        phone = 9682224036
        token = password_reset_token(phone)
        params = {'phone': phone,
                  'confirmedToken': token,
                  'newPassword': 'Aa123456',
                  'newPasswordRepeat': 'Aa1234567'}
        headers = {"accept": "*/*",
                   'Content-Type': 'application/x-www-form-urlencoded'}

        request_url = f'{lktest_url}/user/auth/reset-password'
        response = requests.put(request_url, headers=headers, data=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert type(i) == dict
            except AssertionError:
                message.append(f'Ошибка в ответе по параметру "{i["field"]}", тип данных {type(i)} а не "dict".')
        try:
            assert response.json() == [{'field': 'newPassword', 'message': 'Введеные пароли не совпадают!'}]
        except AssertionError:
            message.append(f'В теле ответа отдаётся неверный текст: {response.json()}')
        assert message == expected_message, message


    def test_reset_password_incorrect_passwords(self):
        message = ['Смена забытого пароля. Пароли не совпадают.']
        expected_message = ['Смена забытого пароля. Пароли не совпадают.']

        lktest_url = "https://api/lk.bezlimit.ru/v1"
        phone = 9682224036
        token = password_reset_token(phone)
        params = {'phone': phone,
                  'confirmedToken': token,
                  'newPassword': 'а!"№"!%%!',
                  'newPasswordRepeat': 'а!"№"!%%!'}
        headers = {"accept": "*/*",
                   'Content-Type': 'application/x-www-form-urlencoded'}

        request_url = f'{lktest_url}/user/auth/reset-password'
        response = requests.put(request_url, headers=headers, data=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert type(i) == dict
            except AssertionError:
                message.append(f'Ошибка в ответе по параметру "{i["field"]}", тип данных {type(i)} а не "dict".')
        try:
            assert response.json() == [
                {
                    "field": "newPassword",
                    "message": "Ввод возможен только букв латинского алфавита (большие и маленькие), цифр, спецсимволов."
                },
                {
                    "field": "newPasswordRepeat",
                    "message": "Ввод возможен только букв латинского алфавита (большие и маленькие), цифр, спецсимволов."
                }
            ]
        except AssertionError:
            message.append(f'В теле ответа отдаётся неверный текст: {response.json()}')
        assert message == expected_message, message

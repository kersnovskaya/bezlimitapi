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


def password_reset_token(phone, url):
    message = ['Запрос на восстановление пароля. Корректный запрос.']
    expected_message = ['Запрос на восстановление пароля. Корректный запрос.']

    code = get_code(phone)
    params = {"phone": phone,
              "code": code}
    headers = {"accept": "application/json",
               "Content-Type": "application/x-www-form-urlencoded"}

    request_url = f'{url}/user/auth/request-password-reset-code-confirmation'
    response = requests.post(request_url, headers=headers, data=params)
    print('\n', response.json())
    token = response.json()['confirmed_token']
    print('\n', token)
    try:
        assert response.status_code == 201
    except AssertionError:
        message.append(f'Код ответа {response.status_code}, а не 201.')
    try:
        assert type(response.json()) == dict
    except AssertionError:
        message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
    try:
        assert type(response.json()['confirmed_token']) == str
    except AssertionError:
        message.append((f"Тип данных в параметре 'confirmed_token' "
                        f"{type(response.json()['confirmed_token'])}, а не 'str'."))
    assert message == expected_message, message
    return token


class TestDev:

    def test_code(self):
        message = ['Кейс восстановления пароля. Запрос на восстановление пароля.']
        expected_message = ['Кейс восстановления пароля. Запрос на восстановление пароля.']

        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9682224036
        params = {"phone": phone}
        headers = {"accept": "application/json"}

        request_url = f'{lktest_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 201
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 201.')
        try:
            assert type(response.json()) == dict
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
        try:
            assert type(response.json()['sending_repeated_notify']) == int
        except AssertionError:
            message.append((f"Тип данных в параметре 'sending_repeated_notify' "
                            f"{type(response.json()['sending_repeated_notify'])}, а не 'int'."))
        assert message == expected_message, message


    def test_change_password(self):
        message = ['Кейс восстановления пароля. Смена пароля.']
        expected_message = ['Кейс восстановления пароля. Смена пароля.']

        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9682224036
        token = password_reset_token(phone, lktest_url)
        params = {"phone": phone,
                  "confirmedToken": token,
                  "newPassword": "AutotestsLk123456",
                  "newPasswordRepeat": "AutotestsLk123456"}
        headers = {"accept": "*/*",
                   'Content-Type': 'application/x-www-form-urlencoded'}

        request_url = f'{lktest_url}/user/auth/reset-password'
        response = requests.put(request_url, headers=headers, data=params)

        print('\n', response.json())

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 200.')

        assert message == expected_message, message


    def test_code_again(self):
        message = ['Кейс восстановления пароля. Повторный запрос на восстановление пароля.']
        expected_message = ['Кейс восстановления пароля. Повторный запрос на восстановление пароля.']

        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9682224036
        params = {"phone": phone}
        headers = {"accept": "application/json"}

        request_url = f'{lktest_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 201
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 201.')
        try:
            assert type(response.json()) == dict
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
        try:
            assert 'confirmed_token' in response.json()
        except AssertionError:
            message.append('При повторном запросе кода подтверждения должен отдаваться токен.')

        assert message == expected_message, message


class TestProd:

    def test_code(self):
        message = ['Кейс восстановления пароля. Запрос на восстановление пароля.']
        expected_message = ['Кейс восстановления пароля. Запрос на восстановление пароля.']

        lktest_url = "https://api.lk.bezlimit.ru/v1"
        phone = 9682224036
        params = {"phone": phone}
        headers = {"accept": "application/json"}

        request_url = f'{lktest_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 201
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 201.')
        try:
            assert type(response.json()) == dict
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
        try:
            assert type(response.json()['sending_repeated_notify']) == int
        except AssertionError:
            message.append((f"Тип данных в параметре 'sending_repeated_notify' "
                            f"{type(response.json()['sending_repeated_notify'])}, а не 'int'."))
        assert message == expected_message, message


    def test_change_password(self):
        message = ['Кейс восстановления пароля. Смена пароля.']
        expected_message = ['Кейс восстановления пароля. Смена пароля.']

        lktest_url = "https://api.lk.bezlimit.ru/v1"
        phone = 9682224036
        token = password_reset_token(phone, lktest_url)
        params = {"phone": phone,
                  "confirmedToken": token,
                  "newPassword": "AutotestsLk123456",
                  "newPasswordRepeat": "AutotestsLk123456"}
        headers = {"accept": "*/*",
                   'Content-Type': 'application/x-www-form-urlencoded'}

        request_url = f'{lktest_url}/user/auth/reset-password'
        response = requests.put(request_url, headers=headers, data=params)

        print('\n', response.json())

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 200.')

        assert message == expected_message, message


    def test_code_again(self):
        message = ['Кейс восстановления пароля. Повторный запрос на восстановление пароля.']
        expected_message = ['Кейс восстановления пароля. Повторный запрос на восстановление пароля.']

        lktest_url = "https://api.lk.bezlimit.ru/v1"
        phone = 9682224036
        params = {"phone": phone}
        headers = {"accept": "application/json"}

        request_url = f'{lktest_url}/user/auth/request-password-reset/'
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 201
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 201.')
        try:
            assert type(response.json()) == dict
        except AssertionError:
            message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
        try:
            assert 'confirmed_token' in response.json()
        except AssertionError:
            message.append('При повторном запросе кода подтверждения должен отдаваться токен.')

        assert message == expected_message, message

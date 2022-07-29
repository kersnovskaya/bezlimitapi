import requests


def authorize(phone, password):
    url = "https://api.lk.bezlimit.ru/v1/user/auth/login"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {'phone': phone,
            "password": password}
    response = requests.get(url, headers=headers, data=data)

    access_token = response.json()['access_token']

    print(access_token)

    return access_token


def registration_code_confirmation(phone):
    url = "https://api.lk.bezlimit.ru/v1/user/auth/registration-code-confirmation/"
    headers = {
        "accept": "application/json",
        "Content - Type": "application / x - www - form - urlencoded"
    }
    data = {
        "phone": phone,
        "code": get_code(phone)
    }
    response = requests.get(url, headers=headers, data=data)

    print('\n', response.json())

    confirmed_token = response.json()['confirmed_token']

    return confirmed_token


def get_code(phone):
    token = 'Z1RseVcn9twtKLY84eYQf57Pw8ENZ1yks436TJHXaC2dJhcRZLJ2mGsgRBpTuFp7'
    url = "https://api.bezlimit.ru/v1/queue/sms"
    headers = {'accept': 'application/json',
               'authorization': 'Basic YXBpOldHZnpzQWlKYkxa',
               'Api-Token': token}
    params = {'phone': phone,
              "expand": "Проверочный код для регистрации в ЛК Безлимит"}
    response = requests.get(url, headers=headers, params=params)
    raw_answer = response.json()
    for i in raw_answer['items']:
        raw_code = i['text']
        break
    code = int(raw_code.split()[-1])
    print('\n', code)
    return code


DOMAIN_DEV = 'https://api.lk.bezlimit.ru/v1'

lk_admin_token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'

test_phone = 9612224930
test_password = 'Aa123456'


class TestProd:
    def test_delete_account(self):
        message = ['Сценарий удаления/создания аккаунта ЛК. Удаление аккаунта.']
        expected_message = ['Сценарий удаления/создания аккаунта ЛК. Удаление аккаунта.']
        url = f"https://api.lk.bezlimit.ru/v1/system/phone/{test_phone}"
        headers = {'accept': '*/*',
                   'Authorization': f'Bearer {lk_admin_token}'}
        response = requests.delete(url, headers=headers)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 200.')
        try:
            assert response.json() is None
        except AssertionError:
            message.append(f'Тело ответа должно быть пустым. Тело ответа {response.json()}')

        assert message == expected_message, message

    def test_authorize_after_delete(self):
        message = ['Сценарий удаления/создания аккаунта ЛК. Авторизация после удаления.']
        expected_message = ['Сценарий удаления/создания аккаунта ЛК. Авторизация после удаления.']
        url = "https://api.lk.bezlimit.ru/v1/user/auth/login"
        headers = {'accept': 'application/json',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        params = {'phone': test_phone,
                  'password': test_password}
        response = requests.post(url, headers=headers, data=params)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert response.json() == [
                {
                    "field": "phone",
                    "message": "Номер не зарегистрирован в \"Безлимит ID\""
                }
            ]
        except AssertionError:
            message.append(f'Ошибка в теле ответа. Тело ответа: {response.json()}')

        assert message == expected_message, message

    def test_is_registered_phone(self):
        message = ['Сценарий удаления/создания аккаунта ЛК. Проверяет, зарегистрирован номер или нет.']
        expected_message = ['Сценарий удаления/создания аккаунта ЛК. Проверяет, зарегистрирован номер или нет.']
        url = "https://api.lk.bezlimit.ru/v1/user/auth/is-registered-phone/"
        headers = {'accept': '*/*',
                   'Api-Token': lk_admin_token}
        params = {'phone': test_phone}
        response = requests.delete(url, headers=headers, params=params)

        try:
            assert response.status_code == 201
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 201.')
        try:
            assert response.json() == {"sending_repeated_notify": 180}
        except AssertionError:
            message.append(f'Ошибка в теле ответа. Тело ответа: {response.json()}')

        assert message == expected_message, message

    def test_registration_code_confirmation(self):
        message = ['Сценарий удаления/создания аккаунта ЛК. Проверяет код подтверждения.']
        expected_message = ['Сценарий удаления/создания аккаунта ЛК. Проверяет код подтверждения.']
        url = "https://api.lk.bezlimit.ru/v1/user/auth/registration-code-confirmation/"
        headers = {
            "accept": "application/json",
            "Content - Type": "application / x - www - form - urlencoded"
        }
        data = {
            "phone": test_phone,
            "code": get_code(test_phone)
        }
        response = requests.get(url, headers=headers, data=data)

        try:
            assert response.status_code == 201
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 201.')
        try:
            assert str(response.json()).startswith("{'confirmed_token': ")
        except AssertionError:
            message.append('В ответе не отдаётся token.')

        assert message == expected_message, message

    def test_registration_create_account(self):
        message = ['Сценарий удаления/создания аккаунта ЛК. Создание аккаунта пользователя.']
        expected_message = ['Сценарий удаления/создания аккаунта ЛК. Создание аккаунта пользователя.']
        url = "https://api.lk.bezlimit.ru/v1/user/auth/registration-create-account/"

        confirmed_token = registration_code_confirmation(test_phone)

        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "phone": test_phone,
            "confirmedToken": confirmed_token,
            "newPassword": 'Aa123456',
            "newPasswordRepeat": 'Aa123456'
        }
        response = requests.post(url, headers=headers, data=data)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 200.')
        try:
            assert str(response.json()).startswith("{'access_token'")
        except AssertionError:
            message.append(f'В ответе не отдаётся access_token, тело ответа: {response.json()}')

        assert message == expected_message, message

    def test_authorize_after_registration(self):
        message = ['Сценарий удаления/создания аккаунта ЛК. Авторизация после регистрации.']
        expected_message = ['Сценарий удаления/создания аккаунта ЛК. Авторизация после регистрации.']
        url = "https://api.lk.bezlimit.ru/v1/user/auth/login"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {'phone': test_phone,
                "password": test_password}
        response = requests.get(url, headers=headers, data=data)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 200.')
        try:
            assert str(response.json()).startswith("{'access_token'")
        except AssertionError:
            message.append(f'В ответе не отдаётся access_token, тело ответа: {response.json()}')

        assert message == expected_message, message

    def test_account_phone(self):
        message = ['Сценарий удаления/создания аккаунта ЛК. Выводит список всех номеров в аккаунте.']
        expected_message = ['Сценарий удаления/создания аккаунта ЛК. Выводит список всех номеров в аккаунте.']

        url = "https://api.lk.bezlimit.ru/v1/account/phone"

        authtoken = authorize(test_phone, test_password)

        headers = {
            "accept": "application/json",
            'Authorization': f'Bearer {authtoken}'
        }

        response = requests.get(url, headers=headers)

        print('\n', response.json())

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 200.')
        try:
            assert response.json()[0]['phone'] == test_phone
        except AssertionError:
            message.append(f'В ответе не отдаётся тестовый номер. Тело ответа: {response.json()}')

        assert message == expected_message, message

    def test_account_phone_phone(self):
        message = ['Сценарий удаления/создания аккаунта ЛК. Данные по номеру в аккаунте.']
        expected_message = ['Сценарий удаления/создания аккаунта ЛК. Данные по номеру в аккаунте.']

        url = f"https://api.lk.bezlimit.ru/v1/account/phone/{test_phone}"

        authtoken = authorize(test_phone, test_password)

        headers = {
            "accept": "application/json",
            'Authorization': f'Bearer {authtoken}'
        }
        params = {"phone": test_phone}

        response = requests.get(url, headers=headers, params=params)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 200.')
        try:
            assert response.json()['phone'] == test_phone
        except AssertionError:
            message.append(f'В ответе не отдаётся тестовый номер. Тело ответа: {response.json()}')

        assert message == expected_message, message

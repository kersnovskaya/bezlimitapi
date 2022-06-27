import requests


def authorize(phone, password):
    url = "https://lktest.bezlimit.ru/v1/user/auth/login"
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
    url = "https://lktest.bezlimit.ru/v1/user/auth/registration-code-confirmation/"
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


DOMAIN_PROD = 'https://lktest.bezlimit.ru/v1'

lk_admin_token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'

test_phone = 9618880491
test_password = 'AutotestsLk123456'


class TestProd:
    def test_delete_account(self):
        message = ['Сценарий удаления/создания аккаунта ЛК. Удаление аккаунта.']
        expected_message = ['Сценарий удаления/создания аккаунта ЛК. Удаление аккаунта.']
        url = f"https://lktest.bezlimit.ru/v1/system/phone/{test_phone}"
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

    def test_account_phone_after_delete(self):
        message = ['Сценарий удаления/создания аккаунта ЛК. Выводит список всех номеров в аккаунте.']
        expected_message = ['Сценарий удаления/создания аккаунта ЛК. Выводит список всех номеров в аккаунте.']

        url = "https://lktest.bezlimit.ru/v1/account/phone"

        headers = {
            "accept": "application/json",
            'Authorization': f'Bearer {lk_admin_token}'
        }

        response = requests.get(url, headers=headers)

        print('\n', response.json())

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 200.')
        for i in response.json():
            try:
                assert i['phone'] != test_phone
            except AssertionError:
                message.append(f'В ответе отдаётся удалённый номер. Тело ответа: {response.json()}')

        assert message == expected_message, message

    def test_account_phone_phone_after_delete(self):
        message = ['Сценарий удаления/создания аккаунта ЛК. Данные по номеру в аккаунте.']
        expected_message = ['Сценарий удаления/создания аккаунта ЛК. Данные по номеру в аккаунте.']

        url = f"https://lktest.bezlimit.ru/v1/account/phone/{test_phone}"

        headers = {
            "accept": "application/json",
            'Authorization': f'Bearer {lk_admin_token}'
        }
        params = {"phone": test_phone}

        response = requests.get(url, headers=headers, params=params)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 200.')
        try:
            assert response.json() is None
        except AssertionError:
            message.append(f'В ответе отдаётся некорректная информация. Тело ответа: {response.json()}')

        assert message == expected_message, message


    def test_is_registered_phone(self):
        message = ['Сценарий удаления/создания аккаунта ЛК. Проверяет, зарегистрирован номер или нет.']
        expected_message = ['Сценарий удаления/создания аккаунта ЛК. Проверяет, зарегистрирован номер или нет.']
        url = "https://lktest.bezlimit.ru/v1/user/auth/is-registered-phone/"
        headers = {'accept': '*/*'}
        params = {'phone': test_phone,
                  'isSendConfirmCode': False}
        response = requests.delete(url, headers=headers, params=params)

        try:
            assert response.status_code == 201
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 201.')
        try:
            assert response.json() is None
        except AssertionError:
            message.append(f'Ошибка в теле ответа. Тело ответа: {response.json()}')

        assert message == expected_message, message

    def test_post_account_phone_correct_with_name(self):
        message = ['Добавление номера в аккаунт пользователя. Корректный запрос с указанием имени.']
        expected_message = ['Добавление номера в аккаунт пользователя. Корректный запрос с указанием имени.']

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {lk_admin_token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }

        data = {
            "phone": test_phone,
            "name": 'KuRwA'
        }
        request_url = f"{DOMAIN_PROD}/account/phone"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 201
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert type(response.json()['phone']) == int
        except AssertionError:
            message.append(f"Тип данных в параметре 'phone' {type(response.json()['phone'])}, а не 'int'.")
        try:
            assert type(response.json()['name']) == str
        except AssertionError:
            message.append(f"Тип данных в параметре 'name' {type(response.json()['name'])}, а не 'str'.")
        try:
            assert type(response.json()['is_disable_delete']) == bool
        except AssertionError:
            message.append(f"Тип данных в параметре 'is_disable_delete' "
                           f"{type(response.json()['is_disable_delete'])}, а не 'bool'.")
        try:
            assert type(response.json()['is_adding_confirmed']) == bool
        except AssertionError:
            message.append(f"Тип данных в параметре 'is_adding_confirmed' "
                           f"{type(response.json()['is_adding_confirmed'])}, а не 'bool'.")
        try:
            assert type(response.json()['registrationConfirmCode']) == dict
        except AssertionError:
            message.append(f"Тип данных в параметре 'registrationConfirmCode' "
                           f"{type(response.json()['registrationConfirmCode'])}, не 'dict'.")
        try:
            assert type(response.json()['registrationConfirmCode']['sending_repeated_notify']) == int
        except AssertionError:
            message.append(f"Тип данных в параметре 'sending_repeated_notify' "
                           f"{type(response.json()['registrationConfirmCode']['sending_repeated_notify'])},"
                           f" а не 'dict'.")

        assert message == expected_message, message

    def test_post_account_phone_code_confirmation(self):

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {lk_admin_token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }

        code = get_code(test_phone)
        print(code)
        data = {
            "phone": test_phone,
            "code": code
        }
        request_url = f"{DOMAIN_PROD}/account/phone/code-confirmation"
        response = requests.post(request_url, headers=headers, data=data)
        print(response.json())
        assert response.status_code == 201, f'Проверка кода подтверждения для добавление номера в аккаунт пользователя.' \
                                            f'Код ответа {response.status_code}, а не "201".'

    def test_get_account_phone_after_adding(self):
        message = ['Данные по номеру в аккаунте. Проверка добавления номера.']
        expected_message = ['Данные по номеру в аккаунте. Проверка добавления номера.']

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {lk_admin_token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }

        data = {
            "phone": test_phone
        }
        request_url = f"{DOMAIN_PROD}/account/phone/{test_phone}"
        response = requests.get(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert response.json()['phone'] == test_phone
        except AssertionError:
            message.append(f"В параметре 'phone' указан номер {response.json()['phone']}, а не 'test_phone'.")
        try:
            assert response.json()['name'] == 'KuRwA'
        except AssertionError:
            message.append('В теле ответа имя контакта не совпадает с тем, которое было указано ранее.')
        try:
            assert response.json()['is_disable_delete'] is False
        except AssertionError:
            message.append(f"В параметре 'is_disable_delete' ответ {response.json()['is_disable_delete']},"
                           f" а не 'False'.")
        try:
            assert response.json()['is_adding_confirmed'] is True
        except AssertionError:
            message.append(f"В параметре 'is_disable_delete' ответ {response.json()['is_adding_confirmed']},"
                           f" а не 'True'.")

        assert message == expected_message, message

    def test_account_phone_phone_after_adding(self):
        message = ['Сценарий удаления/создания аккаунта ЛК. Данные по номеру в аккаунте.']
        expected_message = ['Сценарий удаления/создания аккаунта ЛК. Данные по номеру в аккаунте.']

        url = f"https://lktest.bezlimit.ru/v1/account/phone/{test_phone}"

        headers = {
            "accept": "application/json",
            'Authorization': f'Bearer {lk_admin_token}'
        }
        params = {"phone": test_phone}

        response = requests.get(url, headers=headers, params=params)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 200.')
        try:
            assert response.json()['phone'] == 9618880491
        except AssertionError:
            message.append(f'В ответе отдаётся некорректная информация. Тело ответа: {response.json()}')

        assert message == expected_message, message

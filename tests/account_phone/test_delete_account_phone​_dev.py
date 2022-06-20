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
    return code



class TestDev:

    def test_post_account_phone_invalid_token(self):
        message = ['Добавление номера в аккаунт пользователя. Неавторизован.']
        expected_message = ['Добавление номера в аккаунт пользователя. Неавторизован.']

        token = 12345678910
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9682220854
        }
        request_url = f"{lktest_url}/account/phone"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 401
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 401.")
        try:
            assert response.reason == 'Unauthorized'
        except AssertionError:
            message.append(f"Причина {response.reason}, а не 'Unauthorized'.")
        try:
            assert response.json()['message'] == 'Your request was made with invalid credentials.'
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message


    def test_post_account_phone_not_bezlimit(self):
        message = ['Добавление номера в аккаунт пользователя. Номер не Безлимит.']
        expected_message = ['Добавление номера в аккаунт пользователя. Номер не Безлимит.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9000000000
        }
        request_url = f"{lktest_url}/account/phone"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{"field": "phone",
                                        "message": "Введенный номер не обслуживается в Безлимит!"}]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message


    def test_post_account_phone_not_activated(self):
        message = ['Добавление номера в аккаунт пользователя. Номер на первичной авторизации.']
        expected_message = ['Добавление номера в аккаунт пользователя. Номер на первичной авторизации.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9612225034
        }
        request_url = f"{lktest_url}/account/phone"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{"field": "phone",
                                        "message": "Номер телефона не активирован!"}]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message


    def test_post_account_phone_invalid_phone(self):
        message = ['Добавление номера в аккаунт пользователя. Некорректный номер.']
        expected_message = ['Добавление номера в аккаунт пользователя. Некорректный номер.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 1540
        }
        request_url = f"{lktest_url}/account/phone"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [{"field": "phone",
                                        "message": "Введите номер телефона в формате 9001112233."}]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message


    def test_post_account_phone_correct_without_name(self):
        message = ['Добавление номера в аккаунт пользователя. Корректный запрос без имени.']
        expected_message = ['Добавление номера в аккаунт пользователя. Корректный запрос без имени.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9682220854
        }
        request_url = f"{lktest_url}/account/phone"
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


    def test_post_account_phone_correct_with_name(self):
        message = ['Добавление номера в аккаунт пользователя. Корректный запрос с указанием имени.']
        expected_message = ['Добавление номера в аккаунт пользователя. Корректный запрос с указанием имени.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9682220854,
            "name": 'KuRwA'
        }
        request_url = f"{lktest_url}/account/phone"
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
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        code = get_code(9682220854)
        print(code)
        data = {
            "phone": 9682220854,
            "code": code
        }
        request_url = f"{lktest_url}/account/phone/code-confirmation"
        response = requests.post(request_url, headers=headers, data=data)
        print(response.json())
        assert response.status_code == 201, f'Проверка кода подтверждения для добавление номера в аккаунт пользователя.' \
                                            f'Код ответа {response.status_code}, а не "201".'


    def test_get_account_phone_after_adding(self):
        message = ['Данные по номеру в аккаунте. Проверка добавления номера.']
        expected_message = ['Данные по номеру в аккаунте. Проверка добавления номера.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9682220854
        }
        request_url = f"{lktest_url}/account/phone/9682220854"
        response = requests.get(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert response.json()['phone'] == 9682220854
        except AssertionError:
            message.append(f"В параметре 'phone' указан номер {response.json()['phone']}, а не '9682220854'.")
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


    def test_post_account_phone_correct_again(self):
        message = ['Добавление номера в аккаунт пользователя. Корректный запрос после добавления номера.']
        expected_message = ['Добавление номера в аккаунт пользователя. Корректный запрос после добавления номера.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9682220854,
            "name": 'KuRwA'
        }
        request_url = f"{lktest_url}/account/phone"
        response = requests.post(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.json() == [
                {
                    "field": "phone",
                    "message": "Номер телефона уже добавлен в аккаунт и подтвержден"
                }
            ]
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message


    def test_delete_account_phone_invalid_token(self):
        message = ['Удаление номера из аккаунта пользователя. Не авторизован.']
        expected_message = ['Удаление номера из аккаунта пользователя. Не авторизован.']

        token = 'kzkzkzkz'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9682220854
        }
        request_url = f"{lktest_url}/account/phone/9682220854"
        response = requests.delete(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 401
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 401.")
        try:
            assert response.reason == 'Unauthorized'
        except AssertionError:
            message.append(f"Причина {response.reason}, а не 'Unauthorized'.")
        try:
            assert response.json()['message'] == 'Your request was made with invalid credentials.'
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message


    def test_delete_account_phone_invalid_phone(self):
        message = ['Удаление номера из аккаунта пользователя. Номер не привязан к аккаунту.']
        expected_message = ['Удаление номера из аккаунта пользователя. Номер не привязан к аккаунту.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9696588825
        }
        request_url = f"{lktest_url}/account/phone/9696588825"
        response = requests.delete(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 404
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 404.")
        try:
            assert response.reason == 'Not Found'
        except AssertionError:
            message.append(f"Причина {response.reason}, а не 'Not Found'.")
        try:
            assert response.json()['message'] == 'Номер не найден в аккаунте.'
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message


    def test_delete_account_phone_correct(self):
        message = ['Удаление номера из аккаунта пользователя. Корректный запрос на удаление.']
        expected_message = ['Удаление номера из аккаунта пользователя. Корректный запрос на удаление.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9682220854
        }
        request_url = f"{lktest_url}/account/phone/9682220854"
        response = requests.delete(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 204
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 204.")

        assert message == expected_message, message


    def test_get_account_phone_after_delete(self):
        message = ['Данные по номеру в аккаунте. Проверка добавления номера.']
        expected_message = ['Данные по номеру в аккаунте. Проверка добавления номера.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"
        data = {
            "phone": 9682220854
        }
        request_url = f"{lktest_url}/account/phone/9682220854"
        response = requests.get(request_url, headers=headers, data=data)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 204.")
        try:
            assert response.json() is None
        except AssertionError:
            message.append('Тело ответа должно быть пустым, в ответе присутствует текст.')

        assert message == expected_message, message

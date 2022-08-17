import requests


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


DOMAIN_DEV = 'https://lktest.bezlimit.ru/v1'
request_url = '{0}/user/auth/registration-code-confirmation/'.format(DOMAIN_DEV)

not_registred_phone = 9618880491


class TestDev:
    def test_is_registred_phone_empty_params(self):
        message = ['Проверяет код подтверждения. Отправка пустого запроса.']
        expected_message = ['Проверяет код подтверждения. Отправка пустого запроса.']
        headers = {
            "accept": "application/json",
            "Content - Type": "application / x - www - form - urlencoded"
        }
        data = {
            "phone": None,
            "code": None
        }
        response = requests.get(request_url, headers=headers, data=data)

        print('\n', response.json())

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert response.json() ==  [
                {
                    'field': 'phone',
                    'message': 'Не указан номер телефона.'
                },
                {
                    'field': 'code',
                    'message': 'Введите код подтверждения'
                }
            ]
        except AssertionError:
            message.append('Ошибка в теле ответа.')


        assert message == expected_message, message


    def test_is_registred_phone_incorrect_phone(self):
        message = ['Проверяет код подтверждения. Некорректный номер и код подтверждения.']
        expected_message = ['Проверяет код подтверждения. Некорректный номер и код подтверждения.']
        headers = {
            "accept": "application/json",
            "Content - Type": "application / x - www - form - urlencoded"
        }
        data = {
            "phone": 123456,
            "code": 'False'
        }
        response = requests.get(request_url, headers=headers, data=data)

        print('\n', response.json())

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422.')
        try:
            assert response.json() == [
                {
                    'field': 'phone',
                    'message': 'Введите Номер телефона в формате 9001112233.'
                },
                {
                    "field": "code",
                    "message": "Значение «Код подтверждения» должно быть целым числом."
                }
            ]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_is_registred_phone_not_bezlimit_phone(self):
        message = ['Проверяет код подтверждения. Номер не Безлимит.']
        expected_message = ['Проверяет код подтверждения. Номер не Безлимит.']
        headers = {
            "accept": "application/json",
            "Content - Type": "application / x - www - form - urlencoded"
        }
        data = {
            "phone": 9000000000,
            "code": 123456
        }
        response = requests.get(request_url, headers=headers, data=data)

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
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_is_registred_phone_is_registred(self):
        message = ['Проверяет код подтверждения. Номер зарегистрирован.']
        expected_message = ['Проверяет код подтверждения. Номер зарегистрирован.']
        headers = {
            "accept": "application/json",
            "Content - Type": "application / x - www - form - urlencoded"
        }
        data = {
            "phone": 9612224930,
            "code": 123456
        }
        response = requests.get(request_url, headers=headers, data=data)

        print('\n', response.json())

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 200.')
        try:
            assert response.json() == {
                "message": "Номер был найден в системе \"Безлимит ID\". "
                           "Если вы являетесь пользователем Store Безлимит вы "
                           "можете авторизоваться используя данный пароль."
            }
        except AssertionError:
            message.append(f'Ошибка в теле ответа: {response.json()}.')

        assert message == expected_message, message

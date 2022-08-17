import requests
from datetime import datetime as dt
from datetime import timedelta


DOMAIN_DEV = 'https://lktest.bezlimit.ru/v1'
request_url = '{0}/user/auth/registration-resend-code-confirmation/'.format(DOMAIN_DEV)

not_registred_phone = 9618880491

now = dt.today()
def get_time(phone):
    token = 'Z1RseVcn9twtKLY84eYQf57Pw8ENZ1yks436TJHXaC2dJhcRZLJ2mGsgRBpTuFp7'
    api_url = "https://api.bezlimit.ru/v1"
    headers = {'accept': 'application/json',
               'authorization': 'Basic YXBpOldHZnpzQWlKYkxa',
               'Api-Token': token}
    params = {'phone': phone,
              'expand': 'Проверочный код для регистрации в ЛК Безлимит'}
    url = f"{api_url}/queue/sms"
    response = requests.get(url, headers=headers, params=params)
    raw_answer = response.json()
    sended_at = raw_answer['items'][0]['added_at']

    return sended_at


class TestDev:
    def test_is_registred_phone_empty_params(self):
        message = ['Повторная отправка кода подтверждения при регистрации аккаунта . Отправка пустого запроса.']
        expected_message = ['Повторная отправка кода подтверждения при регистрации аккаунта . Отправка пустого запроса.']
        headers = {
            "accept": "application/json"
        }
        data = {
            "phone": None
        }
        response = requests.get(request_url, headers=headers, params=data)

        try:
            assert response.status_code == 400
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 400.')
        try:
            assert response.json()['name'] == 'Bad Request'
        except AssertionError:
            message.append(f'В параметре "name" - {response.json()["name"]}, а не "Bad Request".')
        try:
            assert response.json()['message'] == 'Отсутствуют обязательные параметры: phone'
        except AssertionError:
            message.append(f'В параметре "message" - {response.json()["message"]}, '
                           f'а не "Отсутствуют обязательные параметры: phone".')
        try:
            assert response.json()['code'] == 0
        except AssertionError:
            message.append(f'В параметре "code" - {response.json()["code"]}, а не "0".')

        assert message == expected_message, message


    def test_is_registred_phone_incorrect_phone(self):
        message = ['Повторная отправка кода подтверждения при регистрации аккаунта. Некорректный номер.']
        expected_message = ['Повторная отправка кода подтверждения при регистрации аккаунта. Некорректный номер.']
        headers = {
            "accept": "application/json"
        }
        data = {
            "phone": 123456
        }
        response = requests.get(request_url, headers=headers, params=data)

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
                }
            ]
        except AssertionError:
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_is_registred_phone_not_bezlimit_phone(self):
        message = ['Повторная отправка кода подтверждения при регистрации аккаунта. Номер не Безлимит.']
        expected_message = ['Повторная отправка кода подтверждения при регистрации аккаунта. Номер не Безлимит.']
        headers = {
            "accept": "application/json"
        }
        data = {
            "phone": 9000000000
        }
        response = requests.get(request_url, headers=headers, params=data)

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
        message = ['Повторная отправка кода подтверждения при регистрации аккаунта. Номер зарегистрирован.']
        expected_message = ['Повторная отправка кода подтверждения при регистрации аккаунта. Номер зарегистрирован.']
        headers = {
            "accept": "application/json"
        }
        data = {
            "phone": 9612224930
        }
        response = requests.get(request_url, headers=headers, params=data)

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
            message.append('Ошибка в теле ответа.')

        assert message == expected_message, message


    def test_is_registred_phone_not_registred_code_false(self):
        message = ['Повторная отправка кода подтверждения при регистрации аккаунта. Корректный запрос.']
        expected_message = ['Повторная отправка кода подтверждения при регистрации аккаунта. Корректный запрос.']

        string_time = str(get_time(not_registred_phone))
        sent_at = dt.strptime(string_time, '%Y-%m-%d %H:%M:%S')

        headers = {
            "accept": "application/json"
        }
        data = {
            "phone": not_registred_phone,
            "isSendConfirmCode": False
        }
        response = requests.get(request_url, headers=headers, params=data)

        try:
            assert response.status_code == 201
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 201.')
        try:
            assert "sending_repeated_notify" in response.json()
        except AssertionError:
            message.append('Ошибка в теле ответа.')
        try:
            assert now - sent_at >= timedelta(minutes=3)
        except AssertionError:
            message.append('СМС на номер было отправлено.')

        assert message == expected_message, message

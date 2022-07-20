import requests
import pytest_check as check

token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
url = 'https://api.lk.bezlimit.ru/v1/account/phone'

class Test:

    phone = 9682224036
    side_phone = 9006471111
    endpoint = '/account/phone'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Bearer {token}'
    }

    def test_correct(self):
        data = {
            'phone': self.side_phone
        }

        response = requests.post(url, headers=self.headers, data=data)

        check.equal(response.status_code, 201, f'Код ответа "{response.status_code}", а не "201".')
        check.equal(response.reason, 'Created', f'Результат запроса "{response.reason}", а не "Created".')

    def test_empty_phone(self):
        data = {}

        response = requests.post(url, headers=self.headers, data=data)

        check.equal(response.status_code, 422, f'Код ответа "{response.status_code}", а не "422".')
        check.equal(response.reason, 'Data Validation Failed.')
        check.equal(response.json()[0]['field'], 'phone')
        check.equal(response.json()[0]['message'], 'Необходимо заполнить «Номер телефона».')

    def test_long_name(self):
        name = 'test_validation_too_long_name_1'  # 31 chars
        data = {'phone': self.side_phone,
                'name': name}

        response = requests.post(url, headers=self.headers, data=data)

        check.equal(response.status_code, 422, 'Код ответа "{}", а не "422"'.format(response.status_code))
        check.equal(response.reason, 'Data Validation Failed.')
        check.equal(response.json()[0]['field'], 'name')
        check.equal(response.json()[0]['message'], 'Значение «Название телефона» должно содержать максимум 30 символов.')

    def test_unauthorized(self):
        response = requests.post(url)

        check.equal(response.status_code, 401, f'Код ответа "{response.status_code}", а не "401".')
        check.equal(response.reason, 'Unauthorized')
        check.equal(response.json()['message'], 'Your request was made with invalid credentials.')

    def test_incorrect_phone(self):
        data = {
            'phone': 900000000011111
        }
        response = requests.post(url, headers=self.headers, data=data)

        check.equal(response.status_code, 422, f'Код ответа "{response.status_code}", а не "422".')
        check.equal(response.reason, 'Data Validation Failed.')
        check.equal(
            response.json(),
            [{'field': 'phone', 'message': 'Введите номер телефона в формате 9001112233.'}],
            f'Ошибка в теле ответа: "{response.json()}"'
        )

    def test_not_bezlimit_phone(self):
        data = {
            'phone': 9000000000
        }

        response = requests.post(url, headers=self.headers, data=data)
        print('\n', response.json())

        check.equal(response.status_code, 422, f'Код ответа "{response.status_code}", а не "422".')
        check.equal(response.reason, 'Data Validation Failed.')
        check.equal(
            response.json(),
            [{'field': 'phone', 'message': 'Введенный номер не обслуживается в Безлимит!'}],
            f'Ошибка в теле ответа: "{response.json()}"'
        )

    def test_number_connected(self):
        data = {
            'phone': self.phone
        }

        response = requests.post(url, headers=self.headers, data=data)

        check.equal(response.status_code, 422, f'Код ответа "{response.status_code}", а не "422".')
        check.equal(response.reason, 'Data Validation Failed.')
        check.equal(
            response.json(),
            [{'field': 'phone', 'message': 'Номер телефона уже добавлен в аккаунт и подтвержден'}],
            f'Ошибка в теле ответа: "{response.json()}"'
        )

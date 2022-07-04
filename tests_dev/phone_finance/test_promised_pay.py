import requests


req_url = 'https://lktest.bezlimit.ru/v1/phone/finance/promised-payment'
test_phone = 9682221928
not_bezlimit_phone = 9000000000
not_in_account_phone = 9006471111
not_repaid_phone = 9618880491

acc_token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'

class TestPromisedPay:
    def test_unauthorized(self):
        message = ['Обещанный платёж. Не авторизован.']
        expected_message = ['Обещанный платёж. Не авторизован.']

        token = 'asshole'
        
        
        data = {'phone': test_phone}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(req_url, headers=headers, data=data)

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
            message.append('Ошибка в тексте ошибки.')

        assert message == expected_message, message

    def test_incorrect_phone(self):
        message = ['Обещанный платёж. Некорректный номер.']
        expected_message = ['Обещанный платёж. Некорректный номер.']

        
        
        data = {'phone': 1234}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {acc_token}',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(req_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.reason == 'Data Validation Failed.'
        except AssertionError:
            message.append(f"Причина '{response.reason}', а не 'Data Validation Failed.'.")
        try:
            assert response.json() == [
                {
                    "field": "phone",
                    "message": "Введите номер телефона в формате 9001112233."
                }
            ]
        except AssertionError:
            message.append('Ошибка в тексте ошибки: "{0}".'.format(response.json()))

        assert message == expected_message, message

    def test_not_in_account_phone(self):
        message = ['Обещанный платёж. Номер не привязан к аккаунту.']
        expected_message = ['Обещанный платёж. Номер не привязан к аккаунту.']

        
        
        data = {'phone': not_in_account_phone}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {acc_token}',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(req_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.reason == 'Data Validation Failed.'
        except AssertionError:
            message.append(f"Причина '{response.reason}', а не 'Data Validation Failed.'.")
        try:
            assert response.json() == [
                {
                    "field": "phone",
                    "message": "Номер телефона не привязан к аккаунту."
                }
            ]
        except AssertionError:
            message.append('Ошибка в тексте ошибки: "{0}".'.format(response.json()))

        assert message == expected_message, message

    def test_not_bezlimit_phone(self):
        message = ['Обещанный платёж. Номер не Безлимит.']
        expected_message = ['Обещанный платёж. Номер не Безлимит.']

        
        
        data = {'phone': not_bezlimit_phone}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {acc_token}',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(req_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.reason == 'Data Validation Failed.'
        except AssertionError:
            message.append(f"Причина '{response.reason}', а не 'Data Validation Failed.'.")
        try:
            assert response.json() == [
                {
                    "field": "phone",
                    "message": "Введенный номер не обслуживается в Безлимит!"
                }
            ]
        except AssertionError:
            message.append('Ошибка в тексте ошибки: "{0}".'.format(response.json()))

        assert message == expected_message, message

    def test_pp_not_repaid(self):
        message = ['Обещанный платёж. Номер не Безлимит.']
        expected_message = ['Обещанный платёж. Номер не Безлимит.']

        data = {'phone': not_repaid_phone}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {acc_token}',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(req_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.reason == 'Data Validation Failed.'
        except AssertionError:
            message.append(f"Причина '{response.reason}', а не 'Data Validation Failed.'.")
        try:
            assert response.json() == [
                {
                    "field": "phone",
                    "message": "Данная услуга вам не доступна."
                               " Обещанный платеж был предоставлен ранее."
                               " Для пользования услугой погасите предыдущий долг."
                }
            ]
        except AssertionError:
            message.append('Ошибка в тексте ошибки: "{0}".'.format(response.json()))

        assert message == expected_message, message


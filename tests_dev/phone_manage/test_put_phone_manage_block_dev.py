import requests


class TestDev:

    def test_phone_manage_block_without_token(self):
        token = 12345678910
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/manage/block-save"
        phone = 9682224036

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': f'application/x-www-form-urlencoded'}
        data = {'phone': phone}

        response = requests.put(request_url, headers=headers, data=data)

        assert response.status_code == 401
        assert response.reason == 'Unauthorized'
        assert response.json()['message'] == 'Your request was made with invalid credentials.'

    def test_phone_manage_block_not_bezlimit_phone(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/manage/block-save"
        phone = 9000000000

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': f'application/x-www-form-urlencoded'}
        data = {'phone': phone}

        response = requests.put(request_url, headers=headers, data=data)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert type(response.json()) == list
        for i in response.json():
            assert i['message'] == 'Введенный номер не обслуживается в Безлимит!'

    def test_phone_manage_block_not_in_account_phone(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/manage/block-save"
        phone = 9682220793

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': f'application/x-www-form-urlencoded'}
        data = {'phone': phone}

        response = requests.put(request_url, headers=headers, data=data)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert type(response.json()) == list
        for i in response.json():
            assert i['message'] == 'Номер телефона не привязан к аккаунту.'

    def test_phone_manage_block_incorrect_phone(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/manage/block-save"
        phone = 9682220

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': f'application/x-www-form-urlencoded'}
        data = {'phone': phone}

        response = requests.put(request_url, headers=headers, data=data)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert type(response.json()) == list
        for i in response.json():
            assert i['message'] == 'Введите номер телефона в формате 9001112233.'

    def test_phone_manage_block_without_contact_phone(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/manage/block-save"
        phone = 9682224036

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': f'application/x-www-form-urlencoded'}
        data = {'phone': phone}

        response = requests.put(request_url, headers=headers, data=data)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert type(response.json()) == list
        for i in response.json():
            assert i['message'] == 'Блокировка по сохранению не выполнена.'

    def test_phone_manage_block_without_passport_phone(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/manage/block-save"
        phone = 9618880491

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': f'application/x-www-form-urlencoded'}
        data = {'phone': phone}

        response = requests.put(request_url, headers=headers, data=data)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert type(response.json()) == list
        for i in response.json():
            assert i['message'] == 'Блокировка по сохранению не выполнена.'

    def test_phone_manage_block_without_correct_phone(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/manage/block-save"
        phone = 9682223055

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': f'application/x-www-form-urlencoded'}
        data = {'phone': phone}

        response = requests.put(request_url, headers=headers, data=data)

        assert response.status_code == 200
        assert type(response.json()) == list
        for i in response.json():
            assert i['message'] == 'Блокировка по сохранению не выполнена.'


    def test_phone_manage_unblock_without_token(self):
        token = 12345678910
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/manage/unblock-save"
        phone = 9682224036

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': f'application/x-www-form-urlencoded'}
        data = {'phone': phone}

        response = requests.put(request_url, headers=headers, data=data)

        assert response.status_code == 401
        assert response.reason == 'Unauthorized'
        assert response.json()['message'] == 'Your request was made with invalid credentials.'

    def test_phone_manage_unblock_not_bezlimit_phone(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/manage/block-save"
        phone = 9000000000

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': f'application/x-www-form-urlencoded'}
        data = {'phone': phone}

        response = requests.put(request_url, headers=headers, data=data)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert type(response.json()) == list
        for i in response.json():
            assert i['message'] == 'Введенный номер не обслуживается в Безлимит!'

    def test_phone_manage_unblock_not_in_account_phone(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/manage/block-save"
        phone = 9682220793

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': f'application/x-www-form-urlencoded'}
        data = {'phone': phone}

        response = requests.put(request_url, headers=headers, data=data)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert type(response.json()) == list
        for i in response.json():
            assert i['message'] == 'Номер телефона не привязан к аккаунту.'

    def test_phone_manage_unblock_incorrect_phone(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/manage/block-save"
        phone = 9682220

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': f'application/x-www-form-urlencoded'}
        data = {'phone': phone}

        response = requests.put(request_url, headers=headers, data=data)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert type(response.json()) == list
        for i in response.json():
            assert i['message'] == 'Введите номер телефона в формате 9001112233.'

    def test_phone_manage_unblock_without_contact_phone(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/manage/block-save"
        phone = 9682224036

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': f'application/x-www-form-urlencoded'}
        data = {'phone': phone}

        response = requests.put(request_url, headers=headers, data=data)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert type(response.json()) == list
        for i in response.json():
            assert i['message'] == 'Блокировка по сохранению не выполнена.'

    def test_phone_manage_unblock_without_passport_phone(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/manage/block-save"
        phone = 9618880491

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': f'application/x-www-form-urlencoded'}
        data = {'phone': phone}

        response = requests.put(request_url, headers=headers, data=data)

        assert response.status_code == 422
        assert response.reason == 'Data Validation Failed.'
        assert type(response.json()) == list
        for i in response.json():
            assert i['message'] == 'Блокировка по сохранению не выполнена.'

    def test_phone_manage_unblock_without_correct_phone(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/manage/block-save"
        phone = 9682223055

        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}',
                   'Content-Type': f'application/x-www-form-urlencoded'}
        data = {'phone': phone}

        response = requests.put(request_url, headers=headers, data=data)

        assert response.status_code == 200
        assert type(response.json()) == list
        for i in response.json():
            assert i['message'] == 'Блокировка по сохранению не выполнена.'

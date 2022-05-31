import requests


class TestDev:

    def test_successful_getting_count_new_notifications_to_one_phone_at_lk(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phones = [9682224036]
        request_url = f"{lktest_url}/phone/notify/count-new-notifications?phones%5B%5D={phones[0]}"

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)

        assert response.status_code == 200
        assert type(response.json()) == list
        for i in response.json():
            assert phones[0] in i.values()
            assert type(i['phone']) == int
            assert type(i['count_unread_messages']) == int

    def test_unsuccessful_getting_count_new_notifications_without_token_at_lk(self):
        token = 12345678910
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phones = [9682224036]
        request_url = f"{lktest_url}/phone/notify/count-new-notifications?phones%5B%5D={phones[0]}"

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)

        assert response.status_code == 401
        assert response.reason == 'Unauthorized'
        assert response.json()['message'] == 'Your request was made with invalid credentials.'

    def test_unsuccessful_getting_count_new_notifications_several_phones(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phones = [9682224036, 9682223055, 9618880491]
        request_url = f"{lktest_url}/phone/notify/count-new-notifications?phones%5B%5D={phones[0]}" \
                      f"&phones%5B%5D={phones[1]}" \
                      f"&phones%5B%5D={phones[2]}"

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)
        print(response.json())
        assert response.status_code == 200
        assert type(response.json()) == list
        for i in response.json():
            assert i['phone'] in phones
            assert type(i['phone']) == int
            assert type(i['count_unread_messages']) == int

    def test_unsuccessful_getting_count_new_notifications_all_phones(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/count-new-notifications"

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)
        phones = [9682224036, 9682223055, 9682221928, 9618880491]

        assert response.status_code == 200
        assert type(response.json()) == list
        for i in response.json():
            assert i['phone'] in phones
            assert type(i['phone']) == int
            assert type(i['count_unread_messages']) == int

    def test_unsuccessful_getting_count_new_notifications_with_shitty_phones(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"

        headers = {'Authorization': f'Bearer {token}'}
        phones = [9682224036, 9682223055, 9682221928, 9618880491]
        shitty_phones = [9006471111, 9682220854, 9682220793]

        request_url = f"{lktest_url}/phone/notify/count-new-notifications?phones%5B%5D={phones[0]}" \
                      f"?phones%5B%5D={phones[1]}" \
                      f"?phones%5B%5D={phones[2]}" \
                      f"?phones%5B%5D={phones[3]}" \
                      f"?phones%5B%5D={shitty_phones[0]}" \
                      f"?phones%5B%5D={shitty_phones[1]}" \
                      f"?phones%5B%5D={shitty_phones[2]}"

        response = requests.get(request_url, headers=headers)

        assert response.status_code == 200
        assert type(response.json()) == list
        for i in response.json():
            assert i['phone'] in phones
            assert i['phone'] not in shitty_phones
            assert type(i['phone']) == int
            assert type(i['count_unread_messages']) == int


class TestProd:

    def test_successful_getting_count_new_notifications_to_one_phone_at_lk(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lk_url = "https://api.lk.bezlimit.ru/v1"
        phones = [9682224036]
        request_url = f"{lk_url}/phone/notify/count-new-notifications?phones%5B%5D={phones[0]}"

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)

        assert response.status_code == 200
        assert type(response.json()) == list
        for i in response.json():
            assert phones[0] in i.values()
            assert type(i['phone']) == int
            assert type(i['count_unread_messages']) == int

    def test_unsuccessful_getting_count_new_notifications_without_token_at_lk(self):
        token = 12345678910
        lk_url = "https://api.lk.bezlimit.ru/v1"
        phones = [9682224036]
        request_url = f"{lk_url}/phone/notify/count-new-notifications?phones%5B%5D={phones[0]}"

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)

        assert response.status_code == 401
        assert response.reason == 'Unauthorized'
        assert response.json()['message'] == 'Your request was made with invalid credentials.'

    def test_unsuccessful_getting_count_new_notifications_several_phones(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lk_url = "https://api.lk.bezlimit.ru/v1"
        phones = [9682224036, 9682223055, 9618880491]
        request_url = f"{lk_url}/phone/notify/count-new-notifications?phones%5B%5D={phones[0]}" \
                      f"&phones%5B%5D={phones[1]}" \
                      f"&phones%5B%5D={phones[2]}"

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)
        print(response.json())
        assert response.status_code == 200
        assert type(response.json()) == list
        for i in response.json():
            assert i['phone'] in phones
            assert type(i['phone']) == int
            assert type(i['count_unread_messages']) == int

    def test_unsuccessful_getting_count_new_notifications_all_phones(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lk_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lk_url}/phone/notify/count-new-notifications"

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)
        phones = [9682224036, 9682223055, 9682221928, 9618880491]

        assert response.status_code == 200
        assert type(response.json()) == list
        for i in response.json():
            assert i['phone'] in phones
            assert type(i['phone']) == int
            assert type(i['count_unread_messages']) == int

    def test_unsuccessful_getting_count_new_notifications_with_shitty_phones(self):
        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lk_url = "https://api.lk.bezlimit.ru/v1"

        headers = {'Authorization': f'Bearer {token}'}
        phones = [9682224036, 9682223055, 9682221928, 9618880491]
        shitty_phones = [9006471111, 9682220854, 9682220793]

        request_url = f"{lk_url}/phone/notify/count-new-notifications?phones%5B%5D={phones[0]}" \
                      f"?phones%5B%5D={phones[1]}" \
                      f"?phones%5B%5D={phones[2]}" \
                      f"?phones%5B%5D={phones[3]}" \
                      f"?phones%5B%5D={shitty_phones[0]}" \
                      f"?phones%5B%5D={shitty_phones[1]}" \
                      f"?phones%5B%5D={shitty_phones[2]}"

        response = requests.get(request_url, headers=headers)

        assert response.status_code == 200
        assert type(response.json()) == list
        for i in response.json():
            assert i['phone'] in phones
            assert i['phone'] not in shitty_phones
            assert type(i['phone']) == int
            assert type(i['count_unread_messages']) == int

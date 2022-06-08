import requests


class TestDev:

    def test_successful_getting_count_new_notifications_to_one_phone_at_lk(self):
        message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. Корректный запрос, один номер.']
        expected_message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. '
                            'Корректный запрос, один номер.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phones = [9682224036]
        request_url = f"{lktest_url}/phone/notify/count-new-notifications?phones%5B%5D={phones[0]}"

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert phones[0] in i.values()
            except AssertionError:
                message.append(f'В параметре "phones" передаётся номер {i.values()} вместо {phones[0]}.')
            try:
                assert type(i['phone']) == int
            except AssertionError:
                message.append(f'Параметр "phone" имеет тип данных {type(i["phone"])}, а не "int:.')
            try:
                assert type(i['count_unread_messages']) == int
            except AssertionError:
                message.append(f'Параметр "phone" имеет тип данных {type(i["count_unread_messages"])}, а не "int:.')

        assert message == expected_message, message

    def test_unsuccessful_getting_count_new_notifications_without_token_at_lk(self):
        message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. Неавторизован.']
        expected_message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. '
                            'Неавторизован.']

        token = 12345678910
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phones = [9682224036]
        request_url = f"{lktest_url}/phone/notify/count-new-notifications?phones%5B%5D={phones[0]}"

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)

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

    def test_unsuccessful_getting_count_new_notifications_several_phones(self):
        message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. '
                   'Корректный запрос, несколько номеров.']
        expected_message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. '
                            'Корректный запрос, несколько номеров.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phones = [9682224036, 9682223055, 9618880491]
        request_url = f"{lktest_url}/phone/notify/count-new-notifications?phones%5B%5D={phones[0]}" \
                      f"&phones%5B%5D={phones[1]}" \
                      f"&phones%5B%5D={phones[2]}"

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)
        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert i['phone'] in phones
            except AssertionError:
                message.append(f'Указан номер {i["phone"]} не из запроса.')
            try:
                assert type(i['phone']) == int
            except AssertionError:
                message.append(f'Параметр "phone" имеет тип данных {type(i["phone"])}, а не "int:.')
            try:
                assert type(i['count_unread_messages']) == int
            except AssertionError:
                message.append(f'Параметр "phone" имеет тип данных {type(i["count_unread_messages"])}, а не "int:.')

        assert message == expected_message, message

    def test_unsuccessful_getting_count_new_notifications_all_phones(self):
        message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. '
                   'Корректный запрос, все номера.']
        expected_message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. '
                            'Корректный запрос, все номера.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/count-new-notifications"

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)
        phones = [9682224036, 9682223055, 9682221928, 9618880491]

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert i['phone'] in phones
            except AssertionError:
                message.append(f'Указан номер {i["phone"]} не из запроса.')
            try:
                assert type(i['phone']) == int
            except AssertionError:
                message.append(f'Параметр "phone" имеет тип данных {type(i["phone"])}, а не "int:.')
            try:
                assert type(i['count_unread_messages']) == int
            except AssertionError:
                message.append(f'Параметр "phone" имеет тип данных {type(i["count_unread_messages"])}, а не "int:.')

        assert message == expected_message, message

    def test_unsuccessful_getting_count_new_notifications_with_shitty_phones(self):
        message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. '
                   'Корректный запрос, все номера.']
        expected_message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. '
                            'Корректный запрос, все номера.']

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

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert i['phone'] in phones
            except AssertionError:
                message.append(f'Указан номер {i["phone"]} не из запроса.')
            try:
                assert i['phone'] not in shitty_phones
            except AssertionError:
                message.append(f'Указан некорректный номер {i["phone"]} из запроса.')
            try:
                assert type(i['phone']) == int
            except AssertionError:
                message.append(f'Параметр "phone" имеет тип данных {type(i["phone"])}, а не "int:.')
            try:
                assert type(i['count_unread_messages']) == int
            except AssertionError:
                message.append(f'Параметр "phone" имеет тип данных {type(i["count_unread_messages"])}, а не "int:.')

        assert message == expected_message, message

class TestProd:

    def test_successful_getting_count_new_notifications_to_one_phone_at_lk(self):
        message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. Корректный запрос, один номер.']
        expected_message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. '
                            'Корректный запрос, один номер.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        phones = [9682224036]
        request_url = f"{lktest_url}/phone/notify/count-new-notifications?phones%5B%5D={phones[0]}"

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert phones[0] in i.values()
            except AssertionError:
                message.append(f'В параметре "phones" передаётся номер {i.values()} вместо {phones[0]}.')
            try:
                assert type(i['phone']) == int
            except AssertionError:
                message.append(f'Параметр "phone" имеет тип данных {type(i["phone"])}, а не "int:.')
            try:
                assert type(i['count_unread_messages']) == int
            except AssertionError:
                message.append(f'Параметр "phone" имеет тип данных {type(i["count_unread_messages"])}, а не "int:.')

        assert message == expected_message, message

    def test_unsuccessful_getting_count_new_notifications_without_token_at_lk(self):
        message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. Неавторизован.']
        expected_message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. '
                            'Неавторизован.']

        token = 12345678910
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        phones = [9682224036]
        request_url = f"{lktest_url}/phone/notify/count-new-notifications?phones%5B%5D={phones[0]}"

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)

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

    def test_unsuccessful_getting_count_new_notifications_several_phones(self):
        message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. '
                   'Корректный запрос, несколько номеров.']
        expected_message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. '
                            'Корректный запрос, несколько номеров.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        phones = [9682224036, 9682223055, 9618880491]
        request_url = f"{lktest_url}/phone/notify/count-new-notifications?phones%5B%5D={phones[0]}" \
                      f"&phones%5B%5D={phones[1]}" \
                      f"&phones%5B%5D={phones[2]}"

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)
        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert i['phone'] in phones
            except AssertionError:
                message.append(f'Указан номер {i["phone"]} не из запроса.')
            try:
                assert type(i['phone']) == int
            except AssertionError:
                message.append(f'Параметр "phone" имеет тип данных {type(i["phone"])}, а не "int:.')
            try:
                assert type(i['count_unread_messages']) == int
            except AssertionError:
                message.append(f'Параметр "phone" имеет тип данных {type(i["count_unread_messages"])}, а не "int:.')

        assert message == expected_message, message

    def test_unsuccessful_getting_count_new_notifications_all_phones(self):
        message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. '
                   'Корректный запрос, все номера.']
        expected_message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. '
                            'Корректный запрос, все номера.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lktest_url}/phone/notify/count-new-notifications"

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers)
        phones = [9682224036, 9682223055, 9682221928, 9618880491]

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert i['phone'] in phones
            except AssertionError:
                message.append(f'Указан номер {i["phone"]} не из запроса.')
            try:
                assert type(i['phone']) == int
            except AssertionError:
                message.append(f'Параметр "phone" имеет тип данных {type(i["phone"])}, а не "int:.')
            try:
                assert type(i['count_unread_messages']) == int
            except AssertionError:
                message.append(f'Параметр "phone" имеет тип данных {type(i["count_unread_messages"])}, а не "int:.')

        assert message == expected_message, message

    def test_unsuccessful_getting_count_new_notifications_with_shitty_phones(self):
        message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. '
                   'Корректный запрос, все номера.']
        expected_message = ['Количество непрочитанных уведомлений по всем номерам в аккаунте. '
                            'Корректный запрос, все номера.']

        token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
        lktest_url = "https://api.lk.bezlimit.ru/v1"

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

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
        for i in response.json():
            try:
                assert i['phone'] in phones
            except AssertionError:
                message.append(f'Указан номер {i["phone"]} не из запроса.')
            try:
                assert i['phone'] not in shitty_phones
            except AssertionError:
                message.append(f'Указан некорректный номер {i["phone"]} из запроса.')
            try:
                assert type(i['phone']) == int
            except AssertionError:
                message.append(f'Параметр "phone" имеет тип данных {type(i["phone"])}, а не "int:.')
            try:
                assert type(i['count_unread_messages']) == int
            except AssertionError:
                message.append(f'Параметр "phone" имеет тип данных {type(i["count_unread_messages"])}, а не "int:.')

        assert message == expected_message, message

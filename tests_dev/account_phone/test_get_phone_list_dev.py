import requests

class Test:

    def test_successful_getting_phone_list_at_lk(self):
        message = ['Выводит список всех номеров в аккаунте. Корректный запрос.']
        expected_message = ['Выводит список всех номеров в аккаунте. Корректный запрос.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        headers = {'Authorization': f'Bearer {token}'}
        phone = 9006471111

        request_url = f'{lktest_url}/account/phone'
        response = requests.get(request_url, headers=headers)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f"Тип данных в ответе {type(response.json())}, а не 'list'.")
        try:
            assert response.json()[0]['phone'] == phone
        except AssertionError:
            message.append(f'Первый номер аккаунта {response.json()[0]["phone"]}, а не {phone}')

        head = response.headers
        try:
            assert head['X-Pagination-Total-Count'] and \
               head['X-Pagination-Page-Count'] and \
               head['X-Pagination-Current-Page']
        except AssertionError:
            message.append('Отсутствуют обязательные заголовки в ответе.')
        try:
            assert head['X-Pagination-Per-Page'] == '10'
        except AssertionError:
            message.append(f'Значение в параметре "X-Pagination-Per-Page": {head["X-Pagination-Per-Page"]}, а не "10"')

        assert message == expected_message, message

    def test_getting_phone_list_with_query_fields(self):
        message = ['Выводит список всех номеров в аккаунте. Корректный запрос с "fields".']
        expected_message = ['Выводит список всех номеров в аккаунте. Корректный запрос с "fields".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"

        queries_fields = ['phone', 'name', 'is_disable_delete', 'is_adding_confirmed']

        for field in queries_fields:
            request_url = f'{lktest_url}/account/phone'
            headers = {'accept': 'application/json',
                       'Authorization': f'Bearer {token}'}
            params = {'fields': field}
            response = requests.get(request_url, headers=headers, params=params)
            try:
                assert response.status_code == 200
            except AssertionError:
                message.append(f"Код ответа {response.status_code}, а не 200.")
            try:
                assert type(response.json()) == list
            except AssertionError:
                message.append(f"Тип данных в ответе {type(response.json())}, а не 'list'.")

            for i in response.json():
                for v in i:
                    short_fields = queries_fields[:]
                    short_fields.remove(field)
                    try:
                        assert v not in short_fields
                    except AssertionError:
                        message.append(f'В параметрах ответа присутствуют типы данных кроме "{v}".')
                        break

        assert message == expected_message, message


    def test_getting_phone_list_with_one_query_expand_at_lk(self):
        message = ['Выводит список всех номеров в аккаунте. Корректный запрос с "expand".']
        expected_message = ['Выводит список всех номеров в аккаунте. Корректный запрос с "expand".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        headers = {'Authorization': f'Bearer {token}'}
        params = {'expand': 'phoneInfo'}

        request_url = f'{lktest_url}/account/phone'
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f"Тип данных в ответе {type(response.json())}, а не 'list'.")
        try:
            assert all([i.get('phoneInfo', None) for i in response.json()]) is not None
        except AssertionError:
            message.append(f"В ответе не отдаётся информация 'phoneInfo'.")

        assert message == expected_message, message

    def test_unsuccessful_getting_phone_list_without_token_at_lk(self):
        message = ['Выводит список всех номеров в аккаунте. Корректный запрос с "expand".']
        expected_message = ['Выводит список всех номеров в аккаунте. Корректный запрос с "expand".']

        token = 12345678910
        lktest_url = "https://lktest.bezlimit.ru/v1"
        headers = {'Authorization': f'Bearer {token}'}

        request_url = f'{lktest_url}/account/phone'
        response = requests.get(request_url, headers=headers)

        try:
            assert response.status_code == 401
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 401.")
        try:
            assert response.reason == 'Unauthorized'
        except AssertionError:
            message.append(f'Причина "{response.reason}", а не "Unauthorized"')
        try:
            assert response.json()['message'] == 'Your request was made with invalid credentials.'
        except AssertionError:
            message.append('Ошибка в тексте ответа.')

        assert message == expected_message, message

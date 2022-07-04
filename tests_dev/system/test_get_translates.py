import requests


request_url = 'https://lktest.bezlimit.ru/v1/system/translates'


class TestDev:
    def test_system_translates_correct(self):
        message = ['Список доступных языков и переводов. Корректный запрос.']
        expected_message = ['Список доступных языков и переводов. Корректный запрос.']

        headers = {'accept': 'application/json'}
        response = requests.get(request_url, headers=headers)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не "200".')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных ответа {type(response.json())}, а не "list".')
        try:
            assert response.json()[0]['code'] == 'en-US'
        except AssertionError:
            message.append(f'В параметре "code" ответа значение {response.json()[0]["code"]}, а не "en-US".')
        try:
            assert response.json()[0]['title'] == 'English'
        except AssertionError:
            message.append(f'В параметре "code" ответа значение {response.json()[0]["title"]}, а не "English".')
        try:
            assert response.json()[1]['code'] == 'ru-RU'
        except AssertionError:
            message.append(f'В параметре "code" ответа значение {response.json()[1]["code"]}, а не "ru-RU".')
        try:
            assert response.json()[1]['title'] == 'Русский'
        except AssertionError:
            message.append(f'В параметре "code" ответа значение {response.json()[1]["title"]}, а не "Русский".')

        assert message == expected_message, message


    def test_system_translates_expand_fields(self):
        message = ['Список доступных языков и переводов. Корректный запрос.']
        expected_message = ['Список доступных языков и переводов. Корректный запрос.']

        headers = {'accept': 'application/json'}
        params = {'expand': 'messages'}
        response = requests.get(request_url, headers=headers, params=params)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не "200".')
        try:
            assert type(response.json()) == list
        except AssertionError:
            message.append(f'Тип данных ответа {type(response.json())}, а не "list".')
        try:
            assert response.json()[0]['code'] == 'en-US'
        except AssertionError:
            message.append(f'В параметре "code" ответа значение {response.json()[0]["code"]}, а не "en-US".')
        try:
            assert response.json()[0]['title'] == 'English'
        except AssertionError:
            message.append(f'В параметре "code" ответа значение {response.json()[0]["title"]}, а не "English".')
        try:
            assert response.json()[1]['code'] == 'ru-RU'
        except AssertionError:
            message.append(f'В параметре "code" ответа значение {response.json()[1]["code"]}, а не "ru-RU".')
        try:
            assert response.json()[1]['title'] == 'Русский'
        except AssertionError:
            message.append(f'В параметре "code" ответа значение {response.json()[1]["title"]}, а не "Русский".')
        try:
            assert response.json()[1].get('messages')
        except AssertionError:
            message.append('Отсутствует доп. поле "messages".')
        assert message == expected_message, message


    def test_system_translates_query_fields(self):
        message = ['Список доступных языков и переводов. Корректный запрос.']
        expected_message = ['Список доступных языков и переводов. Корректный запрос.']

        headers = {'accept': 'application/json'}
        queries_fields = ['code', 'title', 'updated_at']

        for field in queries_fields:
            params = {'fields': field}
            response = requests.get(request_url, headers=headers, params=params)

            try:
                assert response.status_code == 200
            except AssertionError:
                message.append(f'Код ответа {response.status_code}, а не "200".')
            try:
                assert type(response.json()) == list
            except AssertionError:
                message.append(f'Тип данных ответа {type(response.json())}, а не "list".')

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

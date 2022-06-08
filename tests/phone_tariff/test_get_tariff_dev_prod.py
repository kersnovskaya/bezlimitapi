import requests
import random


class TestDev:

	def test_successful_getting_tariff_at_lk(self):
		message = ['Выводит текущий тариф на номере. Корректный запрос.']
		expected_message = ['Выводит текущий тариф на номере. Корректный запрос.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://lktest.bezlimit.ru/v1"
		request_url = f"{lktest_url}/phone/tariff/9006471111"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}

		response = requests.get(request_url, headers=headers)

		try:
			assert response.status_code == 200
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 200.')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
		try:
			assert type(response.json()['id']) == int
		except AssertionError:
			message.append('Тип данных в параметре "id" не "int".')
		try:
			assert response.json()['name'] is not None
		except AssertionError:
			message.append('В параметре "name" передаётся None.')

		assert message == expected_message

	def test_successful_getting_tariff_for_second_phone_at_lk(self):
		message = ['Выводит текущий тариф на номере. Корректный запрос для стороннего номера аккаунта.']
		expected_message = ['Выводит текущий тариф на номере. Корректный запрос для стороннего номера аккаунта.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://lktest.bezlimit.ru/v1"
		request_url = f"{lktest_url}/phone/tariff/9032417766"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}

		response = requests.get(request_url, headers=headers)

		try:
			assert response.status_code == 200
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 200.')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
		try:
			assert type(response.json()['id']) == int
		except AssertionError:
			message.append('Тип данных в параметре "id" не "int".')
		try:
			assert response.json()['name'] is not None
		except AssertionError:
			message.append('В параметре "name" передаётся None.')

		assert message == expected_message

	def test_successful_getting_tariff_with_one_random_field_at_lk(self):
		message = ['Выводит текущий тариф на номере. Запрос с заполненным параметром "fields".']
		expected_message = ['Выводит текущий тариф на номере. Запрос с заполненным параметром "fields".']

		queries_fields = ['id', 'name', 'subscription_fee', 'packet_minutes', 'packet_sms', 'packet_internet']
		random_field = queries_fields[random.randrange(0, len(queries_fields), 1)]

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://lktest.bezlimit.ru/v1"
		request_url = f"{lktest_url}/phone/tariff/9006471111"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}
		params = {'fields': random_field}

		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 200
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 200.')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
		try:
			assert len(response.json()) == 1
		except AssertionError:
			message.append('Количество элементов в ответе превышает 1.')
		try:
			assert response.json()[random_field]
		except AssertionError:
			message.append(f'В ответе отдаётся параметр, не соответствующий параметру в запросе{random_field}.')

		assert message == expected_message


	def test_successful_getting_tariff_with_adding_random_expand_at_lk(self):
		message = ['Выводит текущий тариф на номере. Запрос с заполненным параметром "expand".']
		expected_message = ['Выводит текущий тариф на номере. Запрос с заполненным параметром "expand".']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://lktest.bezlimit.ru/v1"
		request_url = f"{lktest_url}/phone/tariff/9006471111"

		queries_fields = ['description']
		random_field = queries_fields[random.randrange(0, len(queries_fields), 1)]

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}
		params = {'expand': random_field}

		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 200
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 200.')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
		try:
			assert response.json()[random_field]
		except AssertionError:
			message.append(f'В ответе отдаётся параметр, не соответствующий параметру в запросе{random_field}.')

		assert message == expected_message


	def test_unsuccessful_getting_tariff_for_side_phone_at_lk(self):
		message = ['Выводит текущий тариф на номере. Запрос для стороннего номера.']
		expected_message = ['Выводит текущий тариф на номере. Запрос для стороннего номера.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://lktest.bezlimit.ru/v1"
		request_url = f"{lktest_url}/phone/tariff/9696588825"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}
		params = {}

		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 404
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 404.')
		try:
			assert response.reason == 'Not Found'
		except AssertionError:
			message.append(f'Причина ошибки {response.reason}, а не "Not Found".')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
		try:
			assert response.json()['message'] == 'Номер телефона не привязан к аккаунту.'
		except AssertionError:
			message.append('Ошибка в параметре "message".')

		assert message == expected_message

	def test_unsuccessful_getting_tariff_for_not_bezlimit_phone_at_lk(self):
		message = ['Выводит текущий тариф на номере. Номер не Безлимит.']
		expected_message = ['Выводит текущий тариф на номере. Номер не Безлимит.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://lktest.bezlimit.ru/v1"
		request_url = f"{lktest_url}/phone/tariff/9000000000"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}
		params = {}

		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 404
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 404.')
		try:
			assert response.reason == 'Not Found'
		except AssertionError:
			message.append(f'Причина ошибки {response.reason}, а не "Not Found".')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
		try:
			assert response.json()['message'] == 'Введенный номер не обслуживается в Безлимит!'
		except AssertionError:
			message.append('Ошибка в параметре "message".')

		assert message == expected_message

	def test_unsuccessful_getting_tariff_at_lk_without_token(self):
		message = ['Выводит текущий тариф на номере. Номер не Безлимит.']
		expected_message = ['Выводит текущий тариф на номере. Номер не Безлимит.']

		token = 12345678910
		lktest_url = "https://lktest.bezlimit.ru/v1"
		request_url = f"{lktest_url}/phone/tariff/9006471111"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}
		params = {}

		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 401
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 401.')
		try:
			assert response.reason == 'Unauthorized'
		except AssertionError:
			message.append(f'Причина ошибки {response.reason}, а не "Unauthorized".')
		try:
			assert response.json()['message'] == 'Your request was made with invalid credentials.'
		except AssertionError:
			message.append('Ошибка в параметре "message".')

		assert message == expected_message


class TestProd:

	def test_successful_getting_tariff_at_lk(self):
		message = ['Выводит текущий тариф на номере. Корректный запрос.']
		expected_message = ['Выводит текущий тариф на номере. Корректный запрос.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://api.lk.bezlimit.ru/v1"
		request_url = f"{lktest_url}/phone/tariff/9006471111"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}

		response = requests.get(request_url, headers=headers)

		try:
			assert response.status_code == 200
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 200.')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
		try:
			assert type(response.json()['id']) == int
		except AssertionError:
			message.append('Тип данных в параметре "id" не "int".')
		try:
			assert response.json()['name'] is not None
		except AssertionError:
			message.append('В параметре "name" передаётся None.')

		assert message == expected_message

	def test_successful_getting_tariff_for_second_phone_at_lk(self):
		message = ['Выводит текущий тариф на номере. Корректный запрос для стороннего номера аккаунта.']
		expected_message = ['Выводит текущий тариф на номере. Корректный запрос для стороннего номера аккаунта.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://api.lk.bezlimit.ru/v1"
		request_url = f"{lktest_url}/phone/tariff/9032417766"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}

		response = requests.get(request_url, headers=headers)

		try:
			assert response.status_code == 200
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 200.')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
		try:
			assert type(response.json()['id']) == int
		except AssertionError:
			message.append('Тип данных в параметре "id" не "int".')
		try:
			assert response.json()['name'] is not None
		except AssertionError:
			message.append('В параметре "name" передаётся None.')

		assert message == expected_message

	def test_successful_getting_tariff_with_one_random_field_at_lk(self):
		message = ['Выводит текущий тариф на номере. Запрос с заполненным параметром "fields".']
		expected_message = ['Выводит текущий тариф на номере. Запрос с заполненным параметром "fields".']

		queries_fields = ['id', 'name', 'subscription_fee', 'packet_minutes', 'packet_sms', 'packet_internet']
		random_field = queries_fields[random.randrange(0, len(queries_fields), 1)]

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://api.lk.bezlimit.ru/v1"
		request_url = f"{lktest_url}/phone/tariff/9006471111"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}
		params = {'fields': random_field}

		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 200
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 200.')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
		try:
			assert len(response.json()) == 1
		except AssertionError:
			message.append('Количество элементов в ответе превышает 1.')
		try:
			assert response.json()[random_field]
		except AssertionError:
			message.append(f'В ответе отдаётся параметр, не соответствующий параметру в запросе{random_field}.')

		assert message == expected_message


	def test_successful_getting_tariff_with_adding_random_expand_at_lk(self):
		message = ['Выводит текущий тариф на номере. Запрос с заполненным параметром "expand".']
		expected_message = ['Выводит текущий тариф на номере. Запрос с заполненным параметром "expand".']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://api.lk.bezlimit.ru/v1"
		request_url = f"{lktest_url}/phone/tariff/9006471111"

		queries_fields = ['description']
		random_field = queries_fields[random.randrange(0, len(queries_fields), 1)]

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}
		params = {'expand': random_field}

		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 200
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 200.')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
		try:
			assert response.json()[random_field]
		except AssertionError:
			message.append(f'В ответе отдаётся параметр, не соответствующий параметру в запросе{random_field}.')

		assert message == expected_message


	def test_unsuccessful_getting_tariff_for_side_phone_at_lk(self):
		message = ['Выводит текущий тариф на номере. Запрос для стороннего номера.']
		expected_message = ['Выводит текущий тариф на номере. Запрос для стороннего номера.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://api.lk.bezlimit.ru/v1"
		request_url = f"{lktest_url}/phone/tariff/9696588825"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}
		params = {}

		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 404
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 404.')
		try:
			assert response.reason == 'Not Found'
		except AssertionError:
			message.append(f'Причина ошибки {response.reason}, а не "Not Found".')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
		try:
			assert response.json()['message'] == 'Номер телефона не привязан к аккаунту.'
		except AssertionError:
			message.append('Ошибка в параметре "message".')

		assert message == expected_message

	def test_unsuccessful_getting_tariff_for_not_bezlimit_phone_at_lk(self):
		message = ['Выводит текущий тариф на номере. Номер не Безлимит.']
		expected_message = ['Выводит текущий тариф на номере. Номер не Безлимит.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://api.lk.bezlimit.ru/v1"
		request_url = f"{lktest_url}/phone/tariff/9000000000"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}
		params = {}

		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 404
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 404.')
		try:
			assert response.reason == 'Not Found'
		except AssertionError:
			message.append(f'Причина ошибки {response.reason}, а не "Not Found".')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
		try:
			assert response.json()['message'] == 'Введенный номер не обслуживается в Безлимит!'
		except AssertionError:
			message.append('Ошибка в параметре "message".')

		assert message == expected_message

	def test_unsuccessful_getting_tariff_at_lk_without_token(self):
		message = ['Выводит текущий тариф на номере. Номер не Безлимит.']
		expected_message = ['Выводит текущий тариф на номере. Номер не Безлимит.']

		token = 12345678910
		lktest_url = "https://api.lk.bezlimit.ru/v1"
		request_url = f"{lktest_url}/phone/tariff/9006471111"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}
		params = {}

		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 401
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 401.')
		try:
			assert response.reason == 'Unauthorized'
		except AssertionError:
			message.append(f'Причина ошибки {response.reason}, а не "Unauthorized".')
		try:
			assert response.json()['message'] == 'Your request was made with invalid credentials.'
		except AssertionError:
			message.append('Ошибка в параметре "message".')

		assert message == expected_message

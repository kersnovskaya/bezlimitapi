import requests


class TestDev:

	def test_successful_getting_available_tariffs_at_lk(self):
		message = ['Выводит доступные для смены тарифы. Корректный запрос.']
		expected_message = ['Выводит доступные для смены тарифы. Корректный запрос.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://lktest.bezlimit.ru/v1"
		number = 9006471111
		request_url = f"{lktest_url}/phone/tariff/available/{number}"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}

		response = requests.get(request_url, headers=headers)

		try:
			assert response.status_code == 200
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 200.')
		try:
			assert type(response.json()) == list
		except AssertionError:
			message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
		for i in response.json():
			try:
				assert type(i['id']) == int
			except AssertionError:
				message.append(f'Тип данных параметра "id" не "int".')
			try:
				assert i['name'] is not None
			except AssertionError:
				message.append(f'Параметр "name" пустой.')

		assert message == expected_message, message

	def test_successful_getting_available_tariffs_for_second_phone_at_lk(self):
		message = ['Выводит доступные для смены тарифы. Корректный запрос для стороннего номера аккаунта.']
		expected_message = ['Выводит доступные для смены тарифы. Корректный запрос для стороннего номера аккаунта.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://lktest.bezlimit.ru/v1"
		number = 9032417766
		request_url = f"{lktest_url}/phone/tariff/available/{number}"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}

		response = requests.get(request_url, headers=headers)

		try:
			assert response.status_code == 200
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 200.')
		try:
			assert type(response.json()) == list
		except AssertionError:
			message.append(f'Тип данных тела ответа {type(response.json())}, а не "list".')
		for i in response.json():
			try:
				assert type(i['id']) == int
			except AssertionError:
				message.append(f'Тип данных параметра "id" не "int".')
			try:
				assert i['name'] is not None
			except AssertionError:
				message.append(f'Параметр "name" пустой.')

		assert message == expected_message, message

	def test_unsuccessful_getting_available_tariffs_for_side_phone_at_lk(self):
		message = ['Выводит доступные для смены тарифы. Запрос для стороннего номера.']
		expected_message = ['Выводит доступные для смены тарифы. Запрос для стороннего номера.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://lktest.bezlimit.ru/v1"
		number = 9696588825
		request_url = f"{lktest_url}/phone/tariff/available/{number}"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}

		response = requests.get(request_url, headers=headers)

		try:
			assert response.status_code == 404
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 404.')
		try:
			assert response.reason == 'Not Found'
		except AssertionError:
			message.append(f'Причина ошибки {response.reason}, а не "Not Found".')
		try:
			assert response.json()['message'] == 'Номер телефона не привязан к аккаунту.'
		except AssertionError:
			message.append('Ошибка в параметре "message".')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных тела ответа {type(response.json())}, а не "dict".')

		assert message == expected_message, message

	def test_unsuccessful_getting_available_tariffs_for_wrong_phone_at_lk(self):
		message = ['Выводит доступные для смены тарифы. Некорректный номер.']
		expected_message = ['Выводит доступные для смены тарифы. Некорректный номер.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://lktest.bezlimit.ru/v1"
		number = 917980661313
		request_url = f"{lktest_url}/phone/tariff/available/{number}"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}

		response = requests.get(request_url, headers=headers)

		try:
			assert response.status_code == 404
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 404.')
		try:
			assert response.reason == 'Not Found'
		except AssertionError:
			message.append(f'Причина ошибки {response.reason}, а не "Not Found".')
		try:
			assert response.json()['message'] == 'Введите номер телефона в формате 9001112233.'
		except AssertionError:
			message.append('Ошибка в параметре "message".')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных тела ответа {type(response.json())}, а не "dict".')

		assert message == expected_message, message

	def test_unsuccessful_getting_available_tariffs_not_bezlimit_phone_at_lk(self):
		message = ['Выводит доступные для смены тарифы. Номер не Безлимит.']
		expected_message = ['Выводит доступные для смены тарифы. Номер не Безлимит.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		lktest_url = "https://lktest.bezlimit.ru/v1"
		number = 9000000000
		request_url = f"{lktest_url}/phone/tariff/available/{number}"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}

		response = requests.get(request_url, headers=headers)

		try:
			assert response.status_code == 404
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 404.')
		try:
			assert response.reason == 'Not Found'
		except AssertionError:
			message.append(f'Причина ошибки {response.reason}, а не "Not Found".')
		try:
			assert response.json()['message'] == 'Введенный номер не обслуживается в Безлимит!'
		except AssertionError:
			message.append('Ошибка в параметре "message".')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных тела ответа {type(response.json())}, а не "dict".')

		assert message == expected_message, message

	def test_unsuccessful_getting_available_tariffs_without_token_at_lk(self):
		message = ['Выводит доступные для смены тарифы. Неавторизован.']
		expected_message = ['Выводит доступные для смены тарифы. Неавторизован.']

		token = 'kurwa'
		lktest_url = "https://lktest.bezlimit.ru/v1"
		number = 9000000000
		request_url = f"{lktest_url}/phone/tariff/available/{number}"

		headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}

		response = requests.get(request_url, headers=headers)
		print(response)
		print(response.json())

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

		assert message == expected_message, message

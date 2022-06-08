import requests

class TestDev:

	def test_post_phone_download_agreement_invalid_token(self):
		message = ['Скачивание договора пользовательского обслуживания номера. Неавторизован.']
		expected_message = ['Скачивание договора пользовательского обслуживания номера. Неавторизован.']

		token = 12345678910
		headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
		lktest_url = "https://lktest.bezlimit.ru/v1"
		data = {"phone": 9006471111}
		request_url = f"{lktest_url}/phone/info/download-user-service-agreement"
		response = requests.post(request_url, headers=headers, params=data)

		try:
			assert response.status_code == 401
		except AssertionError:
			message.append(f"Код ответа {response.status_code}, а не 401.'")
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных тела ответа {type(response.json())}, а не "dict".')
		try:
			assert response.reason == 'Unauthorized'
		except AssertionError:
			message.append(f'Причина ошибки {response.reason}, а не "Unauthorized".')
		try:
			assert response.json()['message'] == 'Your request was made with invalid credentials.'
		except AssertionError:
			message.append('Ошибка в параметре "message".')

		assert message == expected_message

	def test_post_phone_download_agreement_empty_params(self):
		message = ['Скачивание договора пользовательского обслуживания номера. Пустые "params".']
		expected_message = ['Скачивание договора пользовательского обслуживания номера. Пустые "params".']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
		lktest_url = "https://lktest.bezlimit.ru/v1"

		request_url = f"{lktest_url}/phone/info/download-user-service-agreement"
		response = requests.post(request_url, headers=headers)

		try:
			assert response.status_code == 400
		except AssertionError:
			message.append(f"Код ответа {response.status_code}, а не 400.'")
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных тела ответа {type(response.json())}, а не "dict".')
		try:
			assert response.json()['message'] == 'Отсутствуют обязательные параметры: phone'
		except AssertionError:
			message.append('Ошибка в параметре "message".')

		assert message == expected_message, message

	def test_post_phone_download_agreement_incorrect_number(self):
		message = ['Скачивание договора пользовательского обслуживания номера. Номер не Безлимит.']
		expected_message = ['Скачивание договора пользовательского обслуживания номера. Номер не Безлимит.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		headers = {'accept': '*/*',
				   'Authorization': f'Bearer {token}'}
		lktest_url = "https://lktest.bezlimit.ru/v1"
		data = {"phone": 9000000000}
		request_url = f"{lktest_url}/phone/info/download-user-service-agreement"
		response = requests.post(request_url, headers=headers, params=data)

		try:
			assert response.status_code == 422
		except AssertionError:
			message.append(f"Код ответа {response.status_code}, а не 422.'")
		try:
			assert [{"field": "phone", "message": "Введенный номер не обслуживается в Безлимит!"}] == response.json()
		except AssertionError:
			message.append('Ошибка в параметре "message".')

		assert message == expected_message, message

	def test_post_phone_download_agreement_non_account_number(self):
		message = ['Скачивание договора пользовательского обслуживания номера. Запрос для стороннего номера.']
		expected_message = ['Скачивание договора пользовательского обслуживания номера. Запрос для стороннего номера.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		headers = {'accept': '*/*',
				   'Authorization': f'Bearer {token}'}
		lktest_url = "https://lktest.bezlimit.ru/v1"
		data = {"phone": 9696588825}
		request_url = f"{lktest_url}/phone/info/download-user-service-agreement"
		response = requests.post(request_url, headers=headers, params=data)

		try:
			assert response.status_code == 422
		except AssertionError:
			message.append(f"Код ответа {response.status_code}, а не 422.'")
		try:
			assert response.json() == [{"field": "phone",
									"message": "Номер телефона не привязан к аккаунту."}]
		except AssertionError:
			message.append('Ошибка в параметре "message".')

		assert message == expected_message, message

	def test_post_phone_download_agreement_correct_number(self):
		message = ['Скачивание договора пользовательского обслуживания номера. Корректный запрос.']
		expected_message = ['Скачивание договора пользовательского обслуживания номера. Корректный запрос.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		headers = {'accept': '*/*',
				   'Authorization': f'Bearer {token}'}
		lktest_url = "https://lktest.bezlimit.ru/v1"
		data = {"phone": 9006471111}
		request_url = f"{lktest_url}/phone/info/download-user-service-agreement"
		response = requests.post(request_url, headers=headers, params=data)

		try:
			assert response.status_code == 200
		except AssertionError:
			message.append(f"Код ответа {response.status_code}, а не 200.")
		try:
			assert response.headers['Content-Type'] == 'application/pdf'
		except AssertionError:
			message.append(f"В заголовках ответа нет параметра 'content-type: application/pdf'.")

		assert message == expected_message, message

	def test_post_phone_download_agreement_too_long_number(self):
		message = ['Скачивание договора пользовательского обслуживания номера. Некорректный номер.']
		expected_message = ['Скачивание договора пользовательского обслуживания номера. Некорректный номер.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		headers = {'accept': '*/*',
				   'Authorization': f'Bearer {token}'}
		lktest_url = "https://lktest.bezlimit.ru/v1"
		data = {"phone": 9006471111566481516846165168461}
		request_url = f"{lktest_url}/phone/info/download-user-service-agreement"
		response = requests.post(request_url, headers=headers, params=data)
		print(response)
		print(response.json())

		try:
			assert response.status_code == 400
		except AssertionError:
			message.append(f"Код ответа {response.status_code}, а не 400.")
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных тела ответа {type(response.json())}, а не "dict".')
		assert response.json()['message'] == 'Неправильное значение параметра "phone".'

		assert message == expected_message, message


class TestProd:

	def test_post_phone_download_agreement_invalid_token(self):
		message = ['Скачивание договора пользовательского обслуживания номера. Неавторизован.']
		expected_message = ['Скачивание договора пользовательского обслуживания номера. Неавторизован.']

		token = 12345678910
		headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
		lktest_url = "https://api.lk.bezlimit.ru/v1"
		data = {"phone": 9006471111}
		request_url = f"{lktest_url}/phone/info/download-user-service-agreement"
		response = requests.post(request_url, headers=headers, params=data)

		try:
			assert response.status_code == 401
		except AssertionError:
			message.append(f"Код ответа {response.status_code}, а не 401.'")
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных тела ответа {type(response.json())}, а не "dict".')
		try:
			assert response.reason == 'Unauthorized'
		except AssertionError:
			message.append(f'Причина ошибки {response.reason}, а не "Unauthorized".')
		try:
			assert response.json()['message'] == 'Your request was made with invalid credentials.'
		except AssertionError:
			message.append('Ошибка в параметре "message".')

		assert message == expected_message

	def test_post_phone_download_agreement_empty_params(self):
		message = ['Скачивание договора пользовательского обслуживания номера. Пустые "params".']
		expected_message = ['Скачивание договора пользовательского обслуживания номера. Пустые "params".']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
		lktest_url = "https://api.lk.bezlimit.ru/v1"

		request_url = f"{lktest_url}/phone/info/download-user-service-agreement"
		response = requests.post(request_url, headers=headers)

		try:
			assert response.status_code == 400
		except AssertionError:
			message.append(f"Код ответа {response.status_code}, а не 400.'")
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных тела ответа {type(response.json())}, а не "dict".')
		try:
			assert response.json()['message'] == 'Отсутствуют обязательные параметры: phone'
		except AssertionError:
			message.append('Ошибка в параметре "message".')

		assert message == expected_message, message

	def test_post_phone_download_agreement_incorrect_number(self):
		message = ['Скачивание договора пользовательского обслуживания номера. Номер не Безлимит.']
		expected_message = ['Скачивание договора пользовательского обслуживания номера. Номер не Безлимит.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		headers = {'accept': '*/*',
				   'Authorization': f'Bearer {token}'}
		lktest_url = "https://api.lk.bezlimit.ru/v1"
		data = {"phone": 9000000000}
		request_url = f"{lktest_url}/phone/info/download-user-service-agreement"
		response = requests.post(request_url, headers=headers, params=data)

		try:
			assert response.status_code == 422
		except AssertionError:
			message.append(f"Код ответа {response.status_code}, а не 422.'")
		try:
			assert [{"field": "phone", "message": "Введенный номер не обслуживается в Безлимит!"}] == response.json()
		except AssertionError:
			message.append('Ошибка в параметре "message".')

		assert message == expected_message, message

	def test_post_phone_download_agreement_non_account_number(self):
		message = ['Скачивание договора пользовательского обслуживания номера. Запрос для стороннего номера.']
		expected_message = ['Скачивание договора пользовательского обслуживания номера. Запрос для стороннего номера.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		headers = {'accept': '*/*',
				   'Authorization': f'Bearer {token}'}
		lktest_url = "https://api.lk.bezlimit.ru/v1"
		data = {"phone": 9696588825}
		request_url = f"{lktest_url}/phone/info/download-user-service-agreement"
		response = requests.post(request_url, headers=headers, params=data)

		try:
			assert response.status_code == 422
		except AssertionError:
			message.append(f"Код ответа {response.status_code}, а не 422.'")
		try:
			assert response.json() == [{"field": "phone",
									"message": "Номер телефона не привязан к аккаунту."}]
		except AssertionError:
			message.append('Ошибка в параметре "message".')

		assert message == expected_message, message

	def test_post_phone_download_agreement_correct_number(self):
		message = ['Скачивание договора пользовательского обслуживания номера. Корректный запрос.']
		expected_message = ['Скачивание договора пользовательского обслуживания номера. Корректный запрос.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		headers = {'accept': '*/*',
				   'Authorization': f'Bearer {token}'}
		lktest_url = "https://api.lk.bezlimit.ru/v1"
		data = {"phone": 9006471111}
		request_url = f"{lktest_url}/phone/info/download-user-service-agreement"
		response = requests.post(request_url, headers=headers, params=data)

		try:
			assert response.status_code == 200
		except AssertionError:
			message.append(f"Код ответа {response.status_code}, а не 200.")
		try:
			assert response.headers['Content-Type'] == 'application/pdf'
		except AssertionError:
			message.append(f"В заголовках ответа нет параметра 'content-type: application/pdf'.")

		assert message == expected_message, message

	def test_post_phone_download_agreement_too_long_number(self):
		message = ['Скачивание договора пользовательского обслуживания номера. Некорректный номер.']
		expected_message = ['Скачивание договора пользовательского обслуживания номера. Некорректный номер.']

		token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
		headers = {'accept': '*/*',
				   'Authorization': f'Bearer {token}'}
		lktest_url = "https://api.lk.bezlimit.ru/v1"
		data = {"phone": 9006471111566481516846165168461}
		request_url = f"{lktest_url}/phone/info/download-user-service-agreement"
		response = requests.post(request_url, headers=headers, params=data)
		print(response)
		print(response.json())

		try:
			assert response.status_code == 400
		except AssertionError:
			message.append(f"Код ответа {response.status_code}, а не 400.")
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных тела ответа {type(response.json())}, а не "dict".')
		assert response.json()['message'] == 'Неправильное значение параметра "phone".'

		assert message == expected_message, message

import requests

class TestDev:

	def test_successful_request_for_reset_password_at_lk(self):
		message = ['Запрос на восстановление пароля. Корректный запрос.']
		expected_message = ['Запрос на восстановление пароля. Корректный запрос.']

		lktest_url = "https://lktest.bezlimit.ru/v1"
		phone = 9006471111
		params = {"phone": phone}
		headers = {"accept": "application/json"}

		request_url = f'{lktest_url}/user/auth/request-password-reset/'
		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 201
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 201.')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
		try:
			assert type(response.json()['sending_repeated_notify']) == int
		except AssertionError:
			message.append((f"Тип данных в параметре 'sending_repeated_notify' "
							f"{type(response.json()['sending_repeated_notify'])}, а не 'int'."))
		assert message == expected_message, message


	def test_validation_request_for_reset_password_to_side_phone_at_lk(self):
		message = ['Запрос на восстановление пароля. Ввод не основного номера.']
		expected_message = ['Запрос на восстановление пароля. Ввод не основного номера.']

		lktest_url = "https://lktest.bezlimit.ru/v1"
		phone = 9614828609
		params = {"phone": phone}
		headers = {"accept": "application/json"}

		request_url = f'{lktest_url}/user/auth/request-password-reset/'
		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 422
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 422.')
		try:
			assert response.reason == 'Data Validation Failed.'
		except AssertionError:
			message.append(f'Причина {response.reason}, а не "Data Validation Failed".')
		try:
			assert response.json()[0]['field'] == 'phone'
		except AssertionError:
			message.append(f"В причине ошибки указано поле {response.json()[0]['field']}, а не 'phone'.")
		try:
			assert response.json()[0]['message'] == 'Восстановить пароль можно только на номере, с которого зарегистрирован аккаунт.'
		except AssertionError:
			message.append('Ошибка в тексте ошибки.')
		assert message == expected_message, message


	def test_validation_request_for_reset_password_to_second_phone_at_lk(self):
		message = ['Запрос на восстановление пароля. Ввод не основного номера.']
		expected_message = ['Запрос на восстановление пароля. Ввод не основного номера.']

		lktest_url = "https://lktest.bezlimit.ru/v1"
		phone = 9682224854
		params = {"phone": phone}
		headers = {"accept": "application/json"}

		request_url = f'{lktest_url}/user/auth/request-password-reset/'
		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 422
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 422.')
		try:
			assert response.reason == 'Data Validation Failed.'
		except AssertionError:
			message.append(f'Причина {response.reason}, а не "Data Validation Failed".')
		try:
			assert response.json()[0]['field'] == 'phone'
		except AssertionError:
			message.append(f"В причине ошибки указано поле {response.json()[0]['field']}, а не 'phone'.")
		try:
			assert response.json()[0]['message'] == 'Восстановить пароль можно только на номере, с которого зарегистрирован аккаунт.'
		except AssertionError:
			message.append('Ошибка в тексте ошибки.')

		assert message == expected_message, message


	def test_validation_request_for_reset_password_to_not_bezlimit_phone_at_lk(self):
		message = ['Запрос на восстановление пароля. Ввод номера не Безлимит.']
		expected_message = ['Запрос на восстановление пароля. Ввод номера не Безлимит.']

		lktest_url = "https://lktest.bezlimit.ru/v1"
		phone = 9000000000
		params = {"phone": phone}
		headers = {"accept": "application/json"}

		request_url = f'{lktest_url}/user/auth/request-password-reset/'
		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 422
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 422.')
		try:
			assert response.reason == 'Data Validation Failed.'
		except AssertionError:
			message.append(f'Причина {response.reason}, а не "Data Validation Failed".')
		try:
			assert response.json()[0]['field'] == 'phone'
		except AssertionError:
			message.append(f"В причине ошибки указано поле {response.json()[0]['field']}, а не 'phone'.")
		try:
			assert response.json()[0]['message'] == 'Введенный номер не обслуживается в Безлимит!'
		except AssertionError:
			message.append('Ошибка в тексте ошибки.')

		assert message == expected_message, message


	def test_validation_request_for_reset_password_to_wrong_phone_at_lk(self):
		message = ['Запрос на восстановление пароля. Некорректный номер.']
		expected_message = ['Запрос на восстановление пароля. Некорректный номер.']

		lktest_url = "https://lktest.bezlimit.ru/v1"
		phone = 90000000
		params = {"phone": phone}
		headers = {"accept": "application/json"}

		request_url = f'{lktest_url}/user/auth/request-password-reset/'
		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 422
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 422.')
		try:
			assert response.reason == 'Data Validation Failed.'
		except AssertionError:
			message.append(f'Причина {response.reason}, а не "Data Validation Failed".')
		try:
			assert response.json()[0]['field'] == 'phone'
		except AssertionError:
			message.append(f"В причине ошибки указано поле {response.json()[0]['field']}, а не 'phone'.")
		try:
			assert response.json()[0]['message'] == 'Введите номер телефона в формате 9001112233.'
		except AssertionError:
			message.append('Ошибка в тексте ошибки.')

		assert message == expected_message, message


	def test_validation_request_for_reset_password_to_non_numeric_phone_at_lk(self):
		message = ['Запрос на восстановление пароля. Ввод номера в формате строки.']
		expected_message = ['Запрос на восстановление пароля. Ввод номера в формате строки.']

		lktest_url = "https://lktest.bezlimit.ru/v1"
		phone = 'dick'
		params = {"phone": phone}
		headers = {"accept": "application/json"}

		request_url = f'{lktest_url}/user/auth/request-password-reset/'
		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 400
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 400.')
		try:
			assert response.reason == 'Bad Request'
		except AssertionError:
			message.append(f'Причина {response.reason}, а не "Bad Request".')
		try:
			assert response.json()['message'] == 'Неправильное значение параметра "phone".'
		except AssertionError:
			message.append('Ошибка в тексте ошибки.')

		assert message == expected_message, message


	def test_validation_request_for_reset_password_to_empty_phone_at_lk(self):
		message = ['Запрос на восстановление пароля. Отправка пустого номера.']
		expected_message = ['Запрос на восстановление пароля. Отправка пустого номера.']

		lktest_url = "https://lktest.bezlimit.ru/v1"
		params = {"phone": None}
		headers = {"accept": "application/json"}

		request_url = f'{lktest_url}/user/auth/request-password-reset/'
		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 400
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 400.')
		try:
			assert response.reason == 'Bad Request'
		except AssertionError:
			message.append(f'Причина {response.reason}, а не "Bad Request".')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
		try:
			assert response.json()['message'] == 'Отсутствуют обязательные параметры: phone'
		except AssertionError:
			message.append('Ошибка в тексте ошибки.')

		assert message == expected_message, message


class TestProd:

	def test_successful_request_for_reset_password_at_lk(self):
		message = ['Запрос на восстановление пароля. Корректный запрос.']
		expected_message = ['Запрос на восстановление пароля. Корректный запрос.']

		lktest_url = "https://api.lk.bezlimit.ru/v1"
		phone = 9006471111
		params = {"phone": phone}
		headers = {"accept": "application/json"}

		request_url = f'{lktest_url}/user/auth/request-password-reset/'
		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 201
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 201.')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
		try:
			assert type(response.json()['sending_repeated_notify']) == int
		except AssertionError:
			message.append((f"Тип данных в параметре 'sending_repeated_notify' "
						    f"{type(response.json()['sending_repeated_notify'])}, а не 'int'."))
		assert message == expected_message, message

	def test_validation_request_for_reset_password_to_side_phone_at_lk(self):
		message = ['Запрос на восстановление пароля. Ввод не основного номера.']
		expected_message = ['Запрос на восстановление пароля. Ввод не основного номера.']

		lktest_url = "https://api.lk.bezlimit.ru/v1"
		phone = 9614828609
		params = {"phone": phone}
		headers = {"accept": "application/json"}

		request_url = f'{lktest_url}/user/auth/request-password-reset/'
		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 422
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 422.')
		try:
			assert response.reason == 'Data Validation Failed.'
		except AssertionError:
			message.append(f'Причина {response.reason}, а не "Data Validation Failed".')
		try:
			assert response.json()[0]['field'] == 'phone'
		except AssertionError:
			message.append(f"В причине ошибки указано поле {response.json()[0]['field']}, а не 'phone'.")
		try:
			assert response.json()[0][
					   'message'] == 'Восстановить пароль можно только на номере, с которого зарегистрирован аккаунт.'
		except AssertionError:
			message.append('Ошибка в тексте ошибки.')
		assert message == expected_message, message

	def test_validation_request_for_reset_password_to_second_phone_at_lk(self):
		message = ['Запрос на восстановление пароля. Ввод не основного номера.']
		expected_message = ['Запрос на восстановление пароля. Ввод не основного номера.']

		lktest_url = "https://api.lk.bezlimit.ru/v1"
		phone = 9682224854
		params = {"phone": phone}
		headers = {"accept": "application/json"}

		request_url = f'{lktest_url}/user/auth/request-password-reset/'
		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 422
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 422.')
		try:
			assert response.reason == 'Data Validation Failed.'
		except AssertionError:
			message.append(f'Причина {response.reason}, а не "Data Validation Failed".')
		try:
			assert response.json()[0]['field'] == 'phone'
		except AssertionError:
			message.append(f"В причине ошибки указано поле {response.json()[0]['field']}, а не 'phone'.")
		try:
			assert response.json()[0][
					   'message'] == 'Восстановить пароль можно только на номере, с которого зарегистрирован аккаунт.'
		except AssertionError:
			message.append('Ошибка в тексте ошибки.')

		assert message == expected_message, message

	def test_validation_request_for_reset_password_to_not_bezlimit_phone_at_lk(self):
		message = ['Запрос на восстановление пароля. Ввод номера не Безлимит.']
		expected_message = ['Запрос на восстановление пароля. Ввод номера не Безлимит.']

		lktest_url = "https://api.lk.bezlimit.ru/v1"
		phone = 9000000000
		params = {"phone": phone}
		headers = {"accept": "application/json"}

		request_url = f'{lktest_url}/user/auth/request-password-reset/'
		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 422
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 422.')
		try:
			assert response.reason == 'Data Validation Failed.'
		except AssertionError:
			message.append(f'Причина {response.reason}, а не "Data Validation Failed".')
		try:
			assert response.json()[0]['field'] == 'phone'
		except AssertionError:
			message.append(f"В причине ошибки указано поле {response.json()[0]['field']}, а не 'phone'.")
		try:
			assert response.json()[0]['message'] == 'Введенный номер не обслуживается в Безлимит!'
		except AssertionError:
			message.append('Ошибка в тексте ошибки.')

		assert message == expected_message, message

	def test_validation_request_for_reset_password_to_wrong_phone_at_lk(self):
		message = ['Запрос на восстановление пароля. Некорректный номер.']
		expected_message = ['Запрос на восстановление пароля. Некорректный номер.']

		lktest_url = "https://api.lk.bezlimit.ru/v1"
		phone = 90000000
		params = {"phone": phone}
		headers = {"accept": "application/json"}

		request_url = f'{lktest_url}/user/auth/request-password-reset/'
		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 422
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 422.')
		try:
			assert response.reason == 'Data Validation Failed.'
		except AssertionError:
			message.append(f'Причина {response.reason}, а не "Data Validation Failed".')
		try:
			assert response.json()[0]['field'] == 'phone'
		except AssertionError:
			message.append(f"В причине ошибки указано поле {response.json()[0]['field']}, а не 'phone'.")
		try:
			assert response.json()[0]['message'] == 'Введите номер телефона в формате 9001112233.'
		except AssertionError:
			message.append('Ошибка в тексте ошибки.')

		assert message == expected_message, message

	def test_validation_request_for_reset_password_to_non_numeric_phone_at_lk(self):
		message = ['Запрос на восстановление пароля. Ввод номера в формате строки.']
		expected_message = ['Запрос на восстановление пароля. Ввод номера в формате строки.']

		lktest_url = "https://api.lk.bezlimit.ru/v1"
		phone = 'dick'
		params = {"phone": phone}
		headers = {"accept": "application/json"}

		request_url = f'{lktest_url}/user/auth/request-password-reset/'
		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 400
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 400.')
		try:
			assert response.reason == 'Bad Request'
		except AssertionError:
			message.append(f'Причина {response.reason}, а не "Bad Request".')
		try:
			assert response.json()['message'] == 'Неправильное значение параметра "phone".'
		except AssertionError:
			message.append('Ошибка в тексте ошибки.')

		assert message == expected_message, message

	def test_validation_request_for_reset_password_to_empty_phone_at_lk(self):
		message = ['Запрос на восстановление пароля. Отправка пустого номера.']
		expected_message = ['Запрос на восстановление пароля. Отправка пустого номера.']

		lktest_url = "https://api.lk.bezlimit.ru/v1"
		params = {"phone": None}
		headers = {"accept": "application/json"}

		request_url = f'{lktest_url}/user/auth/request-password-reset/'
		response = requests.get(request_url, headers=headers, params=params)

		try:
			assert response.status_code == 400
		except AssertionError:
			message.append(f'Код ответа {response.status_code}, а не 400.')
		try:
			assert response.reason == 'Bad Request'
		except AssertionError:
			message.append(f'Причина {response.reason}, а не "Bad Request".')
		try:
			assert type(response.json()) == dict
		except AssertionError:
			message.append(f'Тип данных в ответе {type(response.json())}, а не "dict".')
		try:
			assert response.json()['message'] == 'Отсутствуют обязательные параметры: phone'
		except AssertionError:
			message.append('Ошибка в тексте ошибки.')

		assert message == expected_message, message


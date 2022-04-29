import requests


class Test:

    def test_post_phone_notify_connect_invalid_token(self):
        token = 12345678910
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        request_url = f"{lktest_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 401
        assert response.json() == {'code': 0,
                                   'message': 'Your request was made with invalid credentials.',
                                   'name': 'Unauthorized',
                                   'status': 401,
                                   'type': 'yii\\web\\UnauthorizedHttpException'}


    def test_post_phone_notify_connect_empty_params(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        request_url = f"{lktest_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'phone',
                                    'message': 'Не указан номер телефона.'},
                                   {'field': 'channel',
                                   'message': 'Укажите один из каналов доставки уведомлений: push, telegram, viber'}]


    def test_post_phone_notify_connect_incorrect_phone(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9696588825,
                'channel': 'push'}

        request_url = f"{lktest_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{
                                     "field": "phone",
                                     "message": "Номер телефона не привязан к аккаунту."
                                    }]


    def test_post_phone_notify_connect_not_bezlimit_phone(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9000000000,
                'channel': 'push'}

        request_url = f"{lktest_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{
                                     "field": "phone",
                                     "message": "Введенный номер не обслуживается в Безлимит!"
                                    }]


    def test_post_phone_notify_connect_shitty_phone(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 969658882,
                'channel': 'push'}

        request_url = f"{lktest_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{
                                     "field": "phone",
                                     "message": "Введите номер телефона в формате 9001112233."
                                    }]


    def test_post_phone_notify_connect_shitty_channel(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9006471111,
                'channel': 'swallow_my_♂CUM♂'}

        request_url = f"{lktest_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{
                                     "field": "channel",
                                     "message": "Канал доставки уведомлений не найден"
                                    }]


    def test_post_phone_notify_connect_integer_channel(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9006471111,
                'channel': 100500}

        request_url = f"{lktest_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{
                                     "field": "channel",
                                     "message": "Канал доставки уведомлений не найден"
                                    }]


    def test_post_phone_notify_connect_correct_push(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'push'}

        request_url = f"{lktest_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        des_response = response.json()
        print(des_response)

        assert response.status_code == 200
        assert {'channel': 'push', 'name': 'Push-уведомления', 'isConnected': True, 'isAwaitingConfirmation': False} \
               in des_response



    def test_post_phone_notify_connect_correct_push_again(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'push'}

        request_url = f"{lktest_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        des_response = response.json()
        print(des_response)

        assert response.status_code == 422
        assert des_response == [{'field': 'phone',
                                 'message': 'Уведомления в push уже подключены'}]


# Секция отключения канала уведомлений


    def test_post_phone_notify_disconnect_invalid_token(self):
        token = 12345678910
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        request_url = f"{lktest_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 401
        assert response.json() == {'code': 0,
                                   'message': 'Your request was made with invalid credentials.',
                                   'name': 'Unauthorized',
                                   'status': 401,
                                   'type': 'yii\\web\\UnauthorizedHttpException'}

    def test_post_phone_notify_disconnect_empty_params(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        request_url = f"{lktest_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{'field': 'phone',
                                    'message': 'Не указан номер телефона.'},
                                   {'field': 'channel',
                                    'message': 'Укажите один из каналов доставки уведомлений: push, telegram, viber'}]


    def test_post_phone_notify_disconnect_incorrect_phone(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9696588825,
                'channel': 'push'}

        request_url = f"{lktest_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{
            "field": "phone",
            "message": "Номер телефона не привязан к аккаунту."
        }]

    def test_post_phone_notify_disconnect_not_bezlimit_phone(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9000000000,
                'channel': 'push'}

        request_url = f"{lktest_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{
            "field": "phone",
            "message": "Введенный номер не обслуживается в Безлимит!"
        }]

    def test_post_phone_notify_disconnect_shitty_phone(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 969658882,
                'channel': 'push'}

        request_url = f"{lktest_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{
            "field": "phone",
            "message": "Введите номер телефона в формате 9001112233."
        }]

    def test_post_phone_notify_disconnect_shitty_channel(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9006471111,
                'channel': 'swallow_my_♂CUM♂'}

        request_url = f"{lktest_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{
            "field": "channel",
            "message": "Канал доставки уведомлений не найден"
        }]

    def test_post_phone_notify_disconnect_integer_channel(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9006471111,
                'channel': 100500}

        request_url = f"{lktest_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        print(response.json())

        assert response.status_code == 422
        assert response.json() == [{
            "field": "channel",
            "message": "Канал доставки уведомлений не найден"
        }]

    def test_post_phone_notify_disconnect_correct_push(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'push'}

        request_url = f"{lktest_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        des_response = response.json()
        print(des_response)

        assert response.status_code == 200
        assert {'channel': 'push', 'name': 'Push-уведомления', 'isConnected': False, 'isAwaitingConfirmation': False} \
               in des_response

    def test_post_phone_notify_disconnect_correct_push_again(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'push'}

        request_url = f"{lktest_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        des_response = response.json()
        print(des_response)

        assert response.status_code == 200
        assert {'channel': 'push', 'name': 'Push-уведомления', 'isConnected': False, 'isAwaitingConfirmation': False} \
               in des_response


# Проверка работы подключения других каналов + проверка работы параметра 'isAwaitingConfirmation'


    def test_post_phone_notify_connect_correct_telegram(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'telegram'}

        request_url = f"{lktest_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        des_response = response.json()
        print(des_response)

        assert response.status_code == 200
        assert {'channel': 'telegram', 'name': 'Telegram', 'isConnected': False, 'isAwaitingConfirmation': True} \
               in des_response


    def test_post_phone_notify_connect_correct_viber_while_telegram(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'viber'}

        request_url = f"{lktest_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        des_response = response.json()
        print(des_response)

        assert response.status_code == 422
        assert des_response == [{'field': 'phone',
                                 'message': 'Перед подключением уведомлений в viber отключите уведомления в telegram'}]


    def test_post_phone_notify_connect_correct_telegram_again(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'telegram'}

        request_url = f"{lktest_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        des_response = response.json()
        print(des_response)

        assert response.status_code == 422
        assert des_response == [{'field': 'phone',
                                 'message': 'Запрос на подключение уведомлений был отправлен ранее. '
                                            'Ожидается подтверждение подключения'}]


    def test_post_phone_notify_disconnect_correct_telegram(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'telegram'}

        request_url = f"{lktest_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        des_response = response.json()
        print(des_response)

        assert response.status_code == 200
        assert {'channel': 'telegram', 'name': 'Telegram', 'isConnected': False, 'isAwaitingConfirmation': False} \
               in des_response


    def test_post_phone_notify_connect_correct_viber(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'viber'}

        request_url = f"{lktest_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        des_response = response.json()
        print(des_response)

        assert response.status_code == 200
        assert {'channel': 'viber', 'name': 'Viber', 'isConnected': False, 'isAwaitingConfirmation': True} \
               in des_response


    def test_post_phone_notify_connect_correct_telegram_while_viber(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'telegram'}

        request_url = f"{lktest_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        des_response = response.json()
        print(des_response)

        assert response.status_code == 422
        assert des_response == [{'field': 'phone',
                                 'message': 'Перед подключением уведомлений в telegram отключите уведомления в viber'}]


    def test_post_phone_notify_connect_correct_viber_again(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'viber'}

        request_url = f"{lktest_url}/phone/notify/connect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        des_response = response.json()
        print(des_response)

        assert response.status_code == 422
        assert des_response == [{'field': 'phone',
                                 'message': 'Запрос на подключение уведомлений был отправлен ранее. '
                                            'Ожидается подтверждение подключения'}]


    def test_post_phone_notify_disconnect_correct_viber(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'
                   }
        lktest_url = "https://lktest.bezlimit.ru/v1"

        data = {'phone': 9682221451,
                'channel': 'viber'}

        request_url = f"{lktest_url}/phone/notify/disconnect"
        response = requests.post(request_url, headers=headers, data=data)
        print(response)
        des_response = response.json()
        print(des_response)

        assert response.status_code == 200
        assert {'channel': 'viber', 'name': 'Viber', 'isConnected': False, 'isAwaitingConfirmation': False} \
               in des_response

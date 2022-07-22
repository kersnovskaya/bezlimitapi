import requests


url = 'https://api.store.dev.bezlimit.ru/v2/users/change-password'
email = 'api_store_autotest@bezlimit.ru'
headers = {
    'Authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
    'accept': 'application/json',
    'Api-Token': 'IJMcp2KDTiGU05YpYwvd2zWqcfiVJzfsyazLPppAfr-iB5GWkTIoW0tFZZ3UP4Tq',
    'Content-Type': 'application/x-www-form-urlencoded'
}
old_password = 'QualityAssurance'
new_password = 'StickYourFingerInMyAss'

class TestValidation:
    def test_empty_data(self):
        data = {
            'password': None,
            'password_new': None,
            'password_new_repeat': None,
            'code': None
        }

        response = requests.put(url, headers=headers, data=data)

        assert response.json() == [
            {
                'field': 'password',
                'message': 'Не заполнено поле "Текущий пароль"'
            },
            {
                'field': 'password_new',
                'message': 'Не заполнено поле "Новый пароль"'
            },
            {
                'field': 'password_new_repeat',
                'message': 'Не заполнено поле "Новый пароль повторно"'
            }
        ]


class TestNegative:
    def test_unauthorized(self):
        headers_special = {
            'Authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.put(url, headers=headers_special)

        assert response.status_code == 401
        assert response.json() == {
            "name": "Unauthorized",
            "message": "Your request was made with invalid credentials.",
            "code": 0,
            "status": 401,
            "type": "yii\\web\\UnauthorizedHttpException"
        }

    def test_incorrect_password(self):
        data = {
            'password': 'Hentai',
            'password_new': new_password,
            'password_new_repeat': new_password,
            'code': None
        }

        response = requests.put(url, headers=headers, data=data)

        assert response.status_code == 422
        assert response.json() == [{'field': 'password', 'message': 'Пароль не совпадает с текущим паролем'}]

    def test_different_passwords(self):
        data = {
            'password': old_password,
            'password_new': new_password,
            'password_new_repeat': new_password + 'э',
            'code': None
        }

        response = requests.put(url, headers=headers, data=data)

        assert response.status_code == 422
        assert response.json() == [
            {
                'field': 'password_new',
                'message': '"Новый пароль" должен совпадать с "Новый пароль повторно".'
            }
        ]

    def test_incorrect_code(self):
        data = {
            'password': old_password,
            'password_new': new_password,
            'password_new_repeat': new_password,
            'code': 'None'
        }

        response = requests.put(url, headers=headers, data=data)

        assert response.status_code == 422
        assert response.json() == [
            {
                'field': 'code',
                'message': 'Неправильный код подтверждения'
            }
        ]


class TestPositive:
    def test_rimming(self):
        pass

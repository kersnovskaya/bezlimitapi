import requests


url = 'https://api.store.bezlimit.ru/v2/users/login'
headers = {
    'authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
}

login = 'autotest'
password = 'QualityAssurance'


class TestValidation:
    def test_empty_data(self):
        params = {
            'login': None,
            'password': None
        }

        response = requests.post(url, headers=headers, data=params)
        des_res = response.json()

        assert response.status_code == 422
        assert des_res == [
            {
                'field': 'login',
                'message': 'Для продолжения введите логин!'
            },
            {
                'field': 'password',
                'message': 'Для продолжения введите пароль!'
            }
        ]

    def test_russian_log_and_pass(self):
        params = {
            'login': 'пиписька',
            'password': 'пиписька'
        }

        response = requests.post(url, headers=headers, data=params)
        des_res = response.json()

        assert response.status_code == 422
        assert des_res == [
            {
                'field': 'login',
                'message': 'Разрешенные символы: буквы латинского алфавита (большие и маленькие), цифры, спецсимволы.'
            },
            {'field': 'password',
             'message': 'Разрешенные символы: буквы латинского алфавита (большие и маленькие), цифры, спецсимволы.'
             }
        ]


class TestNegative:
    def test_incorrect_password(self):
        params = {
            'login': login,
            'password': 'asshole'
        }

        response = requests.post(url, headers=headers, data=params)
        des_res = response.json()

        assert response.status_code == 422
        assert des_res == [
            {
                'field': 'password',
                'message': 'Введен неверный логин или пароль.'
            }
        ]

    def test_incorrect_login(self):
        params = {
            'login': 'login',
            'password': 'password'
        }

        response = requests.post(url, headers=headers, data=params)
        des_res = response.json()

        assert response.status_code == 422
        assert des_res == [
            {
                'field': 'login',
                'message': 'Введенный логин не найден в системе'
            }
        ]


class TestPositive:
    def test_correct_auth(self):
        params = {
            'login': login,
            'password': password
        }

        response = requests.post(url, headers=headers, data=params)
        des_res = response.json()

        assert response.status_code == 200
        assert des_res == {
            'token': 'IJMcp2KDTiGU05YpYwvd2zWqcfiVJzfsyazLPppAfr-iB5GWkTIoW0tFZZ3UP4Tq'
        }

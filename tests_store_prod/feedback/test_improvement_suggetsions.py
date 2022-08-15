import requests


url = 'https://api.store.bezlimit.ru/v2/feedback/improvement-suggestions'


class TestNegative:

    headers = {
        'Authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    def test_unauthorized(self):
        response = requests.post(url, headers=self.headers)

        assert response.json() == {
            "name": "Unauthorized",
            "message": "Your request was made with invalid credentials.",
            "code": 0,
            "status": 401,
            "type": "yii\\web\\UnauthorizedHttpException"
        }, 'Ошибка в теле ответа.'

    def test_empty_data(self):
        self.headers.update({'Api-Token': 'Kyu8SyaqOyCQCOBTJQ93580ig_xLh1UsU2JS2i07Tt5WnJ9tc6XGqXHlrDXEUyiH'})

        response = requests.post(url, headers=self.headers)

        assert response.status_code == 422
        assert response.json() == [
            {
                'field': 'comment',
                'message': 'Необходимо заполнить «Comment».'
            },
            {
                'field': 'source',
                'message': 'Значение «Source» неверно.'
            },
            {
                'field': 'email',
                'message': 'Необходимо заполнить «Email».'
            }
        ]

    def test_incorrect_data(self):
        self.headers.update({'Api-Token': 'Kyu8SyaqOyCQCOBTJQ93580ig_xLh1UsU2JS2i07Tt5WnJ9tc6XGqXHlrDXEUyiH'})
        params = {
            'email': 10,
            'comment': 12,
            'source': 13
        }

        response = requests.post(url, headers=self.headers, data=params)

        assert response.status_code == 422
        assert response.json() == [
            {
                'field': 'source',
                'message': 'Значение «Source» неверно.'
            },
            {
                'field': 'email',
                'message': 'Значение «Email» не является правильным email адресом.'
            }
        ]

class TestPositive:

    headers = {
        'Authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Api-Token': 'Kyu8SyaqOyCQCOBTJQ93580ig_xLh1UsU2JS2i07Tt5WnJ9tc6XGqXHlrDXEUyiH'
    }

    def test_correct_mobile(self):
        params = {
            'email': 'test@test.ru',
            'comment': '12',
            'source': 'mobile'
        }

        response = requests.post(url, headers=self.headers, data=params)

        assert response.status_code == 200
        assert response.json() is True

    def test_correct_web(self):
        params = {
            'email': 'test@test.ru',
            'comment': '12',
            'source': 'web'
        }

        response = requests.post(url, headers=self.headers, data=params)

        assert response.status_code == 200
        assert response.json() is True

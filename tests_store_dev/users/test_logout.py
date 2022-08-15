import requests


url = 'https://api.store.dev.bezlimit.ru/v2/users/logout'
token = 'IJMcp2KDTiGU05YpYwvd2zWqcfiVJzfsyazLPppAfr-iB5GWkTIoW0tFZZ3UP4Tq'


class Test:
    def test_correct(self):
        headers = {
            'authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
            'accept': 'application/json',
            'Api-Token': token
        }

        response = requests.post(url, headers=headers)

        assert response.status_code == 200
        assert response.json() is True

    def test_unauthorized(self):
        headers = {
            'authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
            'accept': 'application/json',
            'Api-Token': "Hobo's_Penis"
        }

        response = requests.post(url, headers=headers)

        assert response.status_code == 401
        assert response.reason == 'Unauthorized'

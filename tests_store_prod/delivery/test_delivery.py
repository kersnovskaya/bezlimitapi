import requests


url = 'https://api.store.bezlimit.ru/v2/delivery'
token0 = 'Kyu8SyaqOyCQCOBTJQ93580ig_xLh1UsU2JS2i07Tt5WnJ9tc6XGqXHlrDXEUyiH'
token1 = 'jxrOOpE33Zb944m8w5KUXhgIHPGHS1V0zO1wbphFnXNZSjL-Sa5_KGwYwndejafJ'
token2 = 'plq-rqmPaSlZ1bpN-LFYZX_WMQOjiuWVK8-2WnUG8n-AyBhprQgSVdXfE58Al9nW'
headers = {
    'Authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
    'accept': 'application/json'
}


class TestNegative:
    def test_unauthorized(self):
        response = requests.get(url, headers=headers)

        assert response.json() == {
            "name": "Unauthorized",
            "message": "Your request was made with invalid credentials.",
            "code": 0,
            "status": 401,
            "type": "yii\\web\\UnauthorizedHttpException"
        }

class TestValidation:
    def test_incorrect_params(self):
        headers.update({'Api-Token': token0})
        params = {
            'is_archived': 121424,
            'page': 1,
            'per_page': 1
        }
        response = requests.get(url, headers=headers, params=params)

        assert response.json()


class TestPositive:
    def test_correct_lvl0(self):
        headers.update({'Api-Token': token0})

        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        assert type(response.json()['items']) == list
        assert type(response.json()['_meta']) == dict

    def test_correct_lvl1(self):
        headers.update({'Api-Token': token1})

        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        assert type(response.json()['items']) == list
        assert type(response.json()['_meta']) == dict

    def test_correct_lvl2(self):
        headers.update({'Api-Token': token2})

        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        assert type(response.json()['items']) == list
        assert type(response.json()['_meta']) == dict

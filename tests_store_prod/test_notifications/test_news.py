import requests

url = 'https://api.store.bezlimit.ru/v2/notifications/news'

class TestNegative:

    headers = {
        'Authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
        'accept': 'application/json'
    }

    def test_unauthorized(self):
        response = requests.get(url, headers=self.headers)

        assert response.status_code == 401
        assert response.json() == {
            'code': 0,
            'message': 'Your request was made with invalid credentials.',
            'name': 'Unauthorized',
            'status': 401
        }

class TestPositive:
    headers = {
        'Authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
        'accept': 'application/json',
        'Api-Token': 'Kyu8SyaqOyCQCOBTJQ93580ig_xLh1UsU2JS2i07Tt5WnJ9tc6XGqXHlrDXEUyiH'
    }

    fields = ('id', 'preview_image', 'title', 'preview_text', 'text', 'published_date')

    def test_correct_without_fields(self):
        response = requests.get(url, headers=self.headers)

        assert response.status_code == 200
        for element in response.json()['items']:
            assert type(element['id']) == int
            assert type(element['preview_image']) == str
            assert type(element['title']) == str
            assert type(element['preview_text']) == str
            assert type(element['text']) == str
            assert type(element['published_date']) == str

    def test_correct_fields(self):
        for field in self.fields:
            params = {
                'fields': field
            }
            response = requests.get(url, headers=self.headers, params=params)

            for i in response.json()['items']:
                assert len(i) == 1
                for key in i:
                    assert key == field

import requests


class Test:

    def test_resource_office_images_prod(self):
        lk_url = "https://api.lk.bezlimit.ru/v1"
        request_url = f"{lk_url}/resource/office-images"
        response = requests.get(request_url)

        assert response.status_code == 200, f'Код ответа {response.status_code}, а не 200.'
        assert type(response.json()) == list, f'Тип данных ответа {type(response.json())}, а не "list".'
        for i in response.json():
            assert i['url'] is not None, 'В ответе отсутствует ссылка.'


    def test_resource_office_images_dev(self):
        lk_url = "https://lktest.bezlimit.ru/v1"
        request_url = f"{lk_url}/resource/office-images"
        response = requests.get(request_url)

        assert response.status_code == 200, f'Код ответа {response.status_code}, а не 200.'
        assert type(response.json()) == list, f'Тип данных ответа {type(response.json())}, а не "list".'
        for i in response.json():
            assert i['url'] is not None, 'В ответе отсутствует ссылка.'

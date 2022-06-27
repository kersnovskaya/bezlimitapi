import requests

class Test:


    def test_resource_tariff_correct_id(self):
        lktest_url = "https://lktest.bezlimit.ru/v1"
        tariff_id = 5687                            # Сюда прикручивается тариф, по которому есть картинки
        data = {"url": "string"}                    # Сюда пихнуть корректный url

        request_url = f"{lktest_url}/resource/tariff/{tariff_id}"
        response = requests.get(request_url)
        print(response)
        print(response.json())

        assert response.status_code == 200, f'Код ответа {response.status_code}, а не 200.'


    def test_resource_tariff_false_id(self):
        lktest_url = "https://lktest.bezlimit.ru/v1"
        tariff_id = 1488                            # Сюда прикручивается что угодно

        request_url = f"{lktest_url}/resource/tariff/{tariff_id}"
        response = requests.get(request_url)
        print(response)
        print(response.json())

        assert response.json() is None
        assert response.status_code == 200, f'Код ответа {response.status_code}, а не 200.'

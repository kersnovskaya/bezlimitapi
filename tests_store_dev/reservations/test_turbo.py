import requests


url = 'https://api.store.dev.bezlimit.ru/v2/reservations/turbo'
headers = {
    'Authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==',
    'accept': 'application/json'
}
autotest_token = 'IJMcp2KDTiGU05YpYwvd2zWqcfiVJzfsyazLPppAfr-iB5GWkTIoW0tFZZ3UP4Tq'
token0 = 'Kyu8SyaqOyCQCOBTJQ93580ig_xLh1UsU2JS2i07Tt5WnJ9tc6XGqXHlrDXEUyiH'
token1 = 'jxrOOpE33Zb944m8w5KUXhgIHPGHS1V0zO1wbphFnXNZSjL-Sa5_KGwYwndejafJ'
token2 = 'plq-rqmPaSlZ1bpN-LFYZX_WMQOjiuWVK8-2WnUG8n-AyBhprQgSVdXfE58Al9nW'


def search_phone(token):
    url_phones = 'https://api.store.dev.bezlimit.ru/v2/phones'
    headers_phones = {
        'accept': 'application/json',
        'Api-Token': token,
        'Authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw=='
    }
    params_phones = {
        'type': 'standard',
        'service_limit': '450'
    }
    response = requests.get(url_phones, params=params_phones, headers=headers_phones)
    clear_number = response.json()['items'][0]['phone']

    return clear_number


def reservation_search(token):
    url_reservations = 'https://api.store.dev.bezlimit.ru/v2/reservations'
    headers_reservations = {
        'accept': 'application/json',
        'Api-Token': token,
        'Authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw=='
    }
    response = requests.get(url_reservations, headers=headers_reservations)
    reservation_id = response.json()['items'][0]['id']

    return reservation_id


class TestNegative:
    def test_unauthorized(self):
        response = requests.post(url, headers=headers)

        assert response.status_code == 401
        assert response.json() == {
            'code': 0,
            'message': 'Your request was made with invalid credentials.',
            'name': 'Unauthorized',
            'status': 401,
            'type': 'yii\\web\\UnauthorizedHttpException'
        }

    def test_shitty_phone_lvl0(self):
        headers.update({'Api-Token': token0})
        data = {
            'phone': 9000000000
        }

        response = requests.post(url, headers=headers, data=data)

        assert response.json() == {
            'name': 'Not Found',
            'message': 'Номер телефона 9000000000 не найден',
            'code': 0,
            'status': 404,
            'type': 'yii\\web\\NotFoundHttpException'
        }

    def test_shitty_phone_lvl1(self):
        headers.update({'Api-Token': token1})
        data = {
            'phone': 9000000000
        }

        response = requests.post(url, headers=headers, data=data)

        assert response.json() == {
            'name': 'Not Found',
            'message': 'Номер телефона 9000000000 не найден',
            'code': 0,
            'status': 404,
            'type': 'yii\\web\\NotFoundHttpException'
        }

    def test_shitty_phone_lvl2(self):
        headers.update({'Api-Token': token2})
        data = {
            'phone': 9000000000
        }

        response = requests.post(url, headers=headers, data=data)

        assert response.json() == {
            'name': 'Not Found',
            'message': 'Номер телефона 9000000000 не найден',
            'code': 0,
            'status': 404,
            'type': 'yii\\web\\NotFoundHttpException'
        }

    def test_too_much_lvl0(self):
        headers.update({'Api-Token': token0})
        phone = search_phone(token0)
        data = {
            'phone': phone
        }

        response = requests.post(url, headers=headers, data=data)

        assert response.status_code == 430
        assert response.json() == {
            'name': 'Error',
            'message': 'Достигнут лимит на бронирование номеров',
            'code': 0,
            'status': 430,
            'type': 'yii\\web\\HttpException'
        }



class TestPositive:
    def test_correct_autotest(self):
        headers.update({'Api-Token': autotest_token})
        phone = search_phone(token1)
        data = {
            'phone': phone
        }

        response = requests.post(url, headers=headers, data=data)
        des_res = response.json()
        print('\n', des_res)

        assert des_res['phone_number'] == phone
        assert type(des_res['id']) == int
        assert type(des_res['phone_number']) == int
        assert type(des_res['sim']) == str
        assert type(des_res['tariff_id']) == int
        assert type(des_res['dealer_id']) == int
        assert type(des_res['is_activated']) == bool
        assert type(des_res['pay_type']) == str
        assert type(des_res['created_at']) == str
        assert type(des_res['removed_at']) == str

    def test_correct_lvl2(self):
        headers.update({'Api-Token': token2})
        phone = search_phone(token2)
        data = {
            'phone': phone
        }

        response = requests.post(url, headers=headers, data=data)

        print('\n', response.json())

    def test_delete(self):
        url_delete = f'https://api.store.dev.bezlimit.ru/v2/reservations/{reservation_search(autotest_token)}'
        headers.update({'Api-Token': autotest_token})

        response = requests.delete(url_delete, headers=headers)

        assert response.status_code == 204

import random
import requests
import datetime


url = 'https://lktest.bezlimit.ru/v1'
test_phone = 9682221928
acc_token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'


def service_connected(token, phone, status=None):
    request_url = "https://lktest.bezlimit.ru/v1/phone/service/connected"

    params = {
        'phone': phone,
        'status': status
    }
    headers = {'accept': 'application/json',
               'Authorization': f'Bearer {token}'}
    response = requests.get(request_url, headers=headers, params=params)

    return response.json()

def service_available(token, phone):
    request_url = "https://lktest.bezlimit.ru/v1/phone/service/available"

    params = {
        'phone': phone
    }
    headers = {'accept': 'application/json',
               'Authorization': f'Bearer {token}'}
    response = requests.get(request_url, headers=headers, params=params)

    return response.json()


class TestCommonService:

    def test_service_connect(self):
        req_url = f'{url}/phone/service/connect'
        id_s = []
        raw_service_id = service_available(acc_token, test_phone)
        for service_id in raw_service_id:
            if service_id['can_be_deferred'] is False:
                id_s.append(service_id['id'])
        data = {
            'id': random.choice(id_s),
            'phone': test_phone
        }
        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {acc_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(req_url, headers=headers, data=data)

        print('\n', response.json())

    def test_service_disconnect(self):
        req_url = f'{url}/phone/service/disconnect'
        id_s = []
        raw_service_id = service_connected(acc_token, test_phone)
        for service_id in raw_service_id:
            id_s.append(service_id['id'])
        data = {
            'id': random.choice(id_s),
            'phone': test_phone
        }
        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {acc_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(req_url, headers=headers, data=data)

        print('\n', response.json())


class TestDeferredService:

    def test_service_connect(self):
        req_url = f'{url}/phone/service/connect'
        id_s = []
        raw_service_id = service_available(acc_token, test_phone)
        for service_id in raw_service_id:
            if service_id['can_be_deferred'] is True:
                id_s.append(service_id['id'])
        connect_date = datetime.datetime.today() + datetime.timedelta(days=2)
        connect_date_str = str(connect_date).split()[0]
        disconnect_date = connect_date + datetime.timedelta(days=5)
        disconnect_date_str = str(disconnect_date).split()[0]
        data = {
            'id': random.choice(id_s),
            'phone': test_phone,
            'connectDate': connect_date_str,
            'disconnectDate': disconnect_date_str
        }
        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {acc_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(req_url, headers=headers, data=data)

        print('\n', response.json())

    def test_service_disconnect(self):
        req_url = f'{url}/phone/service/disconnect'
        id_s = []
        raw_service_id = service_connected(acc_token, test_phone)
        for service_id in raw_service_id:
            id_s.append(service_id['id'])
        data = {
            'id': random.choice(id_s),
            'phone': test_phone
        }
        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {acc_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(req_url, headers=headers, data=data)

        print('\n', response.json())

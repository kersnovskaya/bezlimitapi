import requests

url = 'https://lktest.bezlimit.ru/v1/phone/notify/register-push-token'
token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'
headers = {
    'accept': 'application/json',
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/x-www-form-urlencoded'
}


class TestValidation:
    def test_empty_data(self):
        data = {
            'platform': None,
            'token': None,
            'device_data': None
        }

        response = requests.post(url, headers=headers, data=data)

        assert response.json() == {
            'name': 'Internal Server Error',
            'message': 'Возникла внутренняя ошибка сервера.',
            'code': 0,
            'status': 500
        }


class TestNegative:
    def test_unauthorized(self):
        shitty_headers = {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(url, headers=shitty_headers)

        assert response.status_code == 401
        assert response.json() == {
            'code': 0,
            'message': 'Your request was made with invalid credentials.',
            'name': 'Unauthorized',
            'status': 401,
            'type': 'yii\\web\\UnauthorizedHttpException'
        }


class TestPositive:
    def test_correct_ios(self):
        data = {
            'platform': 'ios',
            'token': 'None',
            'device_data': {
                'deviceName': 'IPhone     *     10',
                'deviceVersion': '10',
                'identifier': '*****',
                'platformVersion': 'Instance of     *     IOSBuildVersion',
                'appVersion': '0.6.1 13'}
        }

        response = requests.post(url, headers=headers, data=data)

        assert response.status_code == 201

    def test_correct_android(self):
        data = {
            'platform': 'android',
            'token': 'None',
            'device_data': {
                'deviceName': 'ONEPLUS     *     A6010',
                'deviceVersion': '10',
                'identifier': '*****',
                'platformVersion': 'Instance of     *     AndroidBuildVersion',
                'appVersion': '0.6.1 13'}
        }

        response = requests.post(url, headers=headers, data=data)

        assert response.status_code == 201

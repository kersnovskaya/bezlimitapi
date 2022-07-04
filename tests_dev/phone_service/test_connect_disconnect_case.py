import requests


req_url = 'https://lktest.bezlimit.ru/v1/phone/service/available'
test_phone = 9682221928
acc_token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'

class TestCase:

    def test_get_phone_service_connected_correct_without_status(self):
        message = ['Подключенные услуги. Корректный запрос без статуса.']
        expected_message = ['Подключенные услуги. Корректный запрос без статуса.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        phone = 9006471111
        request_url = f"{lktest_url}/phone/service/connected"

        params = {'phone': phone}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {token}'}
        response = requests.get(request_url, headers=headers, params=params)

        
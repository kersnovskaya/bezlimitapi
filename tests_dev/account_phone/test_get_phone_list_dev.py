import random
import requests

class Test:

    def test_successful_getting_phone_list_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        headers = {'Authorization': f'Bearer {token}'}
        phone = 9006471111

        request_url = f'{lktest_url}/account/phone'
        response = requests.get(request_url, headers=headers)

        assert response.status_code == 200
        assert type(response.json()) == list
        assert response.json()[0]['phone'] == phone

        head = response.headers
        assert head['X-Pagination-Total-Count'] and \
               head['X-Pagination-Page-Count'] and \
               head['X-Pagination-Current-Page']
        assert head['X-Pagination-Per-Page'] == '10'

    def test_getting_phone_list_with_one_random_query_field_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        headers = {'Authorization': f'Bearer {token}'}

        queries_fields = ['phone', 'name', 'is_disable_delete', 'is_adding_confirmed']
        random_field = queries_fields[random.randrange(0, len(queries_fields), 1)]

        request_url = f'{lktest_url}/account/phone'
        response = requests.get(request_url, headers=headers)

        print(response.status_code)
        print(response.json())

        assert response.status_code == 200
        assert type(response.json()) == list
        assert set([len(i) for i in response.json()]) == {4}
        assert all([i.get(random_field, None) for i in response.json()]) is not None

    def test_getting_phone_list_with_one_query_expand_at_lk(self):
        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        lktest_url = "https://lktest.bezlimit.ru/v1"
        headers = {'Authorization': f'Bearer {token}'}

        request_url = f'{lktest_url}/account/phone'
        response = requests.get(request_url, headers=headers)

        assert response.status_code == 200
        assert type(response.json()) == list
        assert all([i.get('phoneInfo', None) for i in response.json()]) is not None

    def test_unsuccessful_getting_phone_list_without_token_at_lk(self):
        token = 12345678910
        lktest_url = "https://lktest.bezlimit.ru/v1"
        headers = {'Authorization': f'Bearer {token}'}

        request_url = f'{lktest_url}/account/phone'
        response = requests.get(request_url, headers=headers)

        assert response.status_code == 401
        assert response.reason == 'Unauthorized'
        assert response.json()['message'] == 'Your request was made with invalid credentials.'

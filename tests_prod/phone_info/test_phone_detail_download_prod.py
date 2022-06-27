import random
import requests
from datetime import datetime
from datetime import timedelta


def date_generate(days):
    """
    Данная функция генерирует случайные даты в промежутке с 2202-03-01 по текущую дату.
    В переменной функции передаётся количество дней между начальной и конечной датой.
    """
    start = datetime.today() + (datetime.today() - datetime(year=2021, month=3, day=1)) * random.random()
    maxdate = str(start).split()[0]
    maxfiledate = maxdate.split('-')
    maxfiledate.reverse()
    endfiledate = '.'.join(maxfiledate)

    end = start - timedelta(days=days)
    mindate = str(end).split()[0]
    minfiledate = mindate.split('-')
    minfiledate.reverse()
    startfiledate = '.'.join(minfiledate)

    return maxdate, endfiledate, mindate, startfiledate


class Test:


    def test_get_phone_detail_download_without_token(self):
        message = ['Скачивание детализации. Неавторизован.']
        expected_message = ['Скачивание детализации. Неавторизован.']

        token = 12345678910
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9006471111,
            "periodStart": "2022-01-01",
            "periodEnd": "2022-03-01",
            "type": "0"
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)

        try:
            assert response.status_code == 401
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 401')
        try:
            assert response.reason == 'Unauthorized'
        except AssertionError:
            message.append(f"Причина {response.reason}, а не 'Unauthorized'.")

        assert message == expected_message, message


    def test_get_phone_detail_download_correct_credentials_type_0(self):
        message = ['Скачивание детализации. Корректный запрос, тип-0.']
        expected_message = ['Скачивание детализации. Корректный запрос, тип-0.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        phone = 9006471111

        ourdates = date_generate(30)

        data = {
            "phone": phone,
            "periodStart": ourdates[2],
            "periodEnd": ourdates[0],
            "type": "0"
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 200')
        try:
            assert response.headers['content-type'] == 'application/pdf'
        except AssertionError:
            message.append('Возможно не отдаётся pdf.файл.')
        try:
            assert response.headers['content-disposition'] == f'attachment; ' \
                                                              f'filename="Detail-{phone}-{ourdates[3]}-{ourdates[1]}.pdf"'
        except AssertionError:
            message.append('Номер и дата в pdf.файле не совпадает с запросом.')
        assert message == expected_message, message


    def test_get_phone_detail_download_correct_credentials_type_1(self):
        message = ['Скачивание детализации. Корректный запрос, тип-1.']
        expected_message = ['Скачивание детализации. Корректный запрос, тип-1.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        phone = 9006471111

        ourdates = date_generate(30)

        data = {
            "phone": phone,
            "periodStart": ourdates[2],
            "periodEnd": ourdates[0],
            "type": "1"
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 200')
        try:
            assert response.headers['content-type'] == 'application/pdf'
        except AssertionError:
            message.append('Возможно не отдаётся pdf.файл.')
        try:
            assert response.headers['content-disposition'] == f'attachment; ' \
                                                              f'filename="Detail-{phone}-{ourdates[3]}-{ourdates[1]}.pdf"'
        except AssertionError:
            message.append('Номер и дата в pdf.файле не совпадает с запросом.')
        assert message == expected_message, message

    def test_get_phone_detail_download_correct_credentials_type_2(self):
        message = ['Скачивание детализации. Корректный запрос, тип-2.']
        expected_message = ['Скачивание детализации. Корректный запрос, тип-2.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        phone = 9006471111

        ourdates = date_generate(30)

        data = {
            "phone": phone,
            "periodStart": ourdates[2],
            "periodEnd": ourdates[0],
            "type": "2"
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 200')
        try:
            assert response.headers['content-type'] == 'application/pdf'
        except AssertionError:
            message.append('Возможно не отдаётся pdf.файл.')
        try:
            assert response.headers['content-disposition'] == f'attachment; ' \
                                                              f'filename="Detail-{phone}-{ourdates[3]}-{ourdates[1]}.pdf"'
        except AssertionError:
            message.append('Номер и дата в pdf.файле не совпадает с запросом.')
        assert message == expected_message, message


    def test_get_phone_detail_download_non_bezlimit_number(self):
        message = ['Скачивание детализации. Номер не Безлимит.']
        expected_message = ['Скачивание детализации. Номер не Безлимит.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9000000000,
            "periodStart": "2022-01-01",
            "periodEnd": "2022-03-01",
            "type": "0"
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422')
        try:
            assert response.json() == [{'field': 'phone', 'message': 'Введенный номер не обслуживается в Безлимит!'}]
        except AssertionError:
            message.append(f'Ошибка в тексте ответа.')
        assert message == expected_message, message


    def test_get_phone_detail_download_wrong_number(self):
        message = ['Скачивание детализации. Запрос для стороннего номера.']
        expected_message = ['Скачивание детализации. Запрос для стороннего номера.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9696588825,
            "periodStart": "2022-01-01",
            "periodEnd": "2022-03-01",
            "type": "0"
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422')
        try:
            assert response.json() == [{'field': 'phone', 'message': 'Номер телефона не привязан к аккаунту.'}]
        except AssertionError:
            message.append(f'Ошибка в тексте ответа.')
        assert message == expected_message, message



    def test_get_phone_detail_download_over_three_months(self):
        message = ['Скачивание детализации. Запрос на период более 3-х месяцев.']
        expected_message = ['Скачивание детализации. Запрос на период более 3-х месяцев.']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 9006471111,
            "periodStart": "2022-01-01",
            "periodEnd": "2022-04-01",
            "type": "0"
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422')
        try:
            assert response.json() == [{'field': 'periodEnd',
                                    'message': 'Период детализации не должен превышать 3 месяца.'}]
        except AssertionError:
            message.append(f'Ошибка в тексте ответа.')

        assert message == expected_message, message


    def test_get_phone_detail_download_wrong_params(self):
        message = ['Скачивание детализации. Некорректные "params".']
        expected_message = ['Скачивание детализации. Некорректные "params".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": 806471111,
            "periodStart": "01-01-2022",
            "periodEnd": "04-2022-01",
            "type": "5"
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 422')
        try:
            assert response.json() == [{'field': 'phone', 'message': 'Введите номер телефона в формате 9001112233.'},
                                   {'field': 'periodStart', 'message': 'Дата должна быть в формате Y-m-d'},
                                   {'field': 'periodEnd', 'message': 'Дата должна быть в формате Y-m-d'},
                                   {'field': 'type', 'message': 'Разрешенные типы детализаций: 0, 1, 2'}]
        except AssertionError:
            message.append(f'Ошибка в тексте ответа.')

        assert message == expected_message, message


    def test_get_phone_detail_download_empty_params(self):
        message = ['Скачивание детализации. Незаполненные "params".']
        expected_message = ['Скачивание детализации. Незаполненные "params".']

        token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
        headers = {'accept': '*/*', 'Authorization': f'Bearer {token}'}
        lktest_url = "https://api.lk.bezlimit.ru/v1"
        data = {
            "phone": "",
            "periodStart": "",
            "periodEnd": "",
            "type": ""
        }
        request_url = f"{lktest_url}/phone/detail/download"
        response = requests.get(request_url, headers=headers, params=data)


        try:
            assert response.status_code == 400
        except AssertionError:
            message.append(f'Код ответа {response.status_code}, а не 400')
        try:
            assert response.reason == 'Bad Request'
        except AssertionError:
            message.append(f"Причина {response.reason}, а не 'Bad Request'.")

        assert message == expected_message, message

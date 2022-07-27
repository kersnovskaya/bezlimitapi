import time
import requests
from selenium.webdriver import Chrome, ActionChains, Keys
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(scope='class')
def set_up_browser():
    options = Options()
    options.headless = False
    driver = Chrome(
        options=options,
        executable_path=r'C:\Users\morozov_i\PycharmProjects\automationSkillbox\driver\chromedriver.exe',
    )
    driver.implicitly_wait(15)

    driver.get('https://bill.bezlimit.ru/site/login')

    yield driver

    driver.quit()


req_url = 'https://lktest.bezlimit.ru/v1/phone/finance/promised-payment'
test_phone = 9682221928
not_bezlimit_phone = 9000000000
not_in_account_phone = 9612224930
not_repaid_phone = 9618880491

invalid_token = 'asshole'
acc_token = 'NEKTX5ZvPNovEEmkL-8tKxcPJBuCx16v5sQCox8b483zOvfEsCwcSwrjicpWDqDI'

class TestValidation:
    def test_unauthorized(self):
        message = ['Обещанный платёж. Не авторизован.']
        expected_message = ['Обещанный платёж. Не авторизован.']

        data = {'phone': test_phone}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {invalid_token}',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(req_url, headers=headers, data=data)

        try:
            assert response.status_code == 401
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 401.")
        try:
            assert response.reason == 'Unauthorized'
        except AssertionError:
            message.append(f"Причина {response.reason}, а не 'Unauthorized'.")
        try:
            assert response.json()['message'] == 'Your request was made with invalid credentials.'
        except AssertionError:
            message.append('Ошибка в тексте ошибки.')

        assert message == expected_message, message

    def test_incorrect_phone(self):
        message = ['Обещанный платёж. Некорректный номер.']
        expected_message = ['Обещанный платёж. Некорректный номер.']

        data = {'phone': 1234}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {acc_token}',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(req_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.reason == 'Data Validation Failed.'
        except AssertionError:
            message.append(f"Причина '{response.reason}', а не 'Data Validation Failed.'.")
        try:
            assert response.json() == [
                {
                    "field": "phone",
                    "message": "Введите номер телефона в формате 9001112233."
                }
            ]
        except AssertionError:
            message.append('Ошибка в тексте ошибки: "{0}".'.format(response.json()))

        assert message == expected_message, message

    def test_not_in_account_phone(self):
        message = ['Обещанный платёж. Номер не привязан к аккаунту.']
        expected_message = ['Обещанный платёж. Номер не привязан к аккаунту.']

        data = {'phone': not_in_account_phone}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {acc_token}',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(req_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.reason == 'Data Validation Failed.'
        except AssertionError:
            message.append(f"Причина '{response.reason}', а не 'Data Validation Failed.'.")
        try:
            assert response.json() == [
                {
                    "field": "phone",
                    "message": "Номер телефона не привязан к аккаунту."
                }
            ]
        except AssertionError:
            message.append('Ошибка в тексте ошибки: "{0}".'.format(response.json()))

        assert message == expected_message, message

    def test_not_bezlimit_phone(self):
        message = ['Обещанный платёж. Номер не Безлимит.']
        expected_message = ['Обещанный платёж. Номер не Безлимит.']

        data = {'phone': not_bezlimit_phone}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {acc_token}',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(req_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.reason == 'Data Validation Failed.'
        except AssertionError:
            message.append(f"Причина '{response.reason}', а не 'Data Validation Failed.'.")
        try:
            assert response.json() == [
                {
                    "field": "phone",
                    "message": "Введенный номер не обслуживается в Безлимит!"
                }
            ]
        except AssertionError:
            message.append('Ошибка в тексте ошибки: "{0}".'.format(response.json()))

        assert message == expected_message, message

    def test_pp_not_repaid(self):
        message = ['Обещанный платёж. ОП на номере не погашен.']
        expected_message = ['Обещанный платёж. ОП на номере не погашен.']

        data = {'phone': not_repaid_phone}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {acc_token}',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(req_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.reason == 'Data Validation Failed.'
        except AssertionError:
            message.append(f"Причина '{response.reason}', а не 'Data Validation Failed.'.")
        try:
            assert response.json() == [
                {
                    "field": "phone",
                    "message": "Данная услуга вам не доступна."
                               " Обещанный платеж был предоставлен ранее."
                               " Для пользования услугой погасите предыдущий долг."
                }
            ]
        except AssertionError:
            message.append('Ошибка в тексте ошибки: "{0}".'.format(response.json()))

        assert message == expected_message, message

class Test200WithWeb(object):
    @pytest.mark.dependency()
    def test_put_payment(self, set_up_browser):
        driver = set_up_browser
        action_chains = ActionChains(driver)

        login_input = driver.find_element(By.ID, 'loginform-username')
        login_input.send_keys('morozov_i')
        password_input = driver.find_element(By.ID, 'loginform-password')
        password_input.send_keys('Takkurwatak1')
        button_enter = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[4]/div[2]/div[1]/button')
        button_enter.click()
        time.sleep(3)
        driver.get('https://bill.bezlimit.ru/phone/card/finances/9618880491')
        driver.find_element(By.XPATH, '//*[@id="plusform-sum"]').send_keys('15')
        driver.find_element(By.XPATH, '//*[@id="plusform-description"]').send_keys('Автотест ОП')
        ass = driver.find_element(By.XPATH, '//*[@id="w2"]/div[3]/div[2]/div/span/span[1]/span')
        action_chains.click(ass).send_keys('14' + Keys.ENTER).perform()
        driver.find_element(By.XPATH, '//button[@class="btn btn-primary btn-sm btn-labeled fal fa-ruble"]').click()
        assert driver.find_element(By.XPATH, '//div[@class="alert-success alert fade in"]').text == "×\nПринят платёж [сумма: 15,00 ₽]"

    @pytest.mark.dependency()
    def test_correct(self):
        message = ['Обещанный платёж. Корректный запрос.']
        expected_message = ['Обещанный платёж. Корректный запрос.']

        data = {'phone': not_repaid_phone}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {acc_token}',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(req_url, headers=headers, data=data)

        try:
            assert response.status_code == 200
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 200.")
        try:
            assert response.json()['message'] == "Обещанный платеж на сумму 15 руб. внесен."
        except AssertionError:
            message.append('Ошибка в тексте ошибки: "{0}".'.format(response.json()['message']))
        try:
            assert type(response.json()['expiration_at']) == str
        except AssertionError:
            message.append(
                'Тип данных в параметре "expiration_at": "{0}", а не "str".'
                .format(response.json()['message'])
            )

        assert message == expected_message, message

    @pytest.mark.dependency()
    def test_correct_again(self):
        message = ['Обещанный платёж. Запрос с активным ОП.']
        expected_message = ['Обещанный платёж. Запрос с активным ОП.']

        data = {'phone': not_repaid_phone}
        headers = {'accept': 'application/json',
                   'Authorization': f'Bearer {acc_token}',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(req_url, headers=headers, data=data)

        try:
            assert response.status_code == 422
        except AssertionError:
            message.append(f"Код ответа {response.status_code}, а не 422.")
        try:
            assert response.reason == 'Data Validation Failed.'
        except AssertionError:
            message.append(f"Причина '{response.reason}', а не 'Data Validation Failed.'.")
        try:
            assert response.json() == [
                {
                    'field': 'phone',
                    'message': 'Данная услуга вам не доступна. На вашем номере уже есть действующий обещанный платеж.'
                }
            ]
        except AssertionError:
            message.append('Ошибка в тексте ошибки: "{0}".'.format(response.json()))

        assert message == expected_message, message

    @pytest.mark.dependency(depends=["Test200WithWeb::test_correct", "Test200WithWeb::test_put_payment"])
    def test_delete_promised_payment(self, set_up_browser):
        driver = set_up_browser

        driver.get(
            'https://bill.bezlimit.ru/finance/plus?PlusSearch%5Bid%5D=&PlusSearch%5Bphone_number%5D=9618880491&PlusSearch%5Baccount_id%5D=&PlusSearch%5BanyPayment%5D=&PlusSearch%5Bdate%5D%5B0%5D=&PlusSearch%5Bdate%5D%5B1%5D=&PlusSearch%5Bdescription%5D=&PlusSearch%5Bpayment_category_id%5D=&PlusSearch%5Bcreated%5D%5B0%5D=&PlusSearch%5Bcreated%5D%5B1%5D=&PlusSearch%5Buser%5D=&PlusSearch%5Bpay_type%5D=&PlusSearch%5Bpay_system%5D='
        )
        driver.find_element(By.XPATH, '//button[@title="Удалить"]').click()
        driver.find_element(By.ID, 'plusdeleteform-deletion_comment').send_keys('Автотест ОП')
        driver.find_element(By.XPATH, '//div[@class="modal-footer"]/button[contains(text(), "Удалить")]').click()

        time.sleep(3)

        driver.get(
            'https://bill.bezlimit.ru/finance/plus?PlusSearch%5Bid%5D=&PlusSearch%5Bphone_number%5D=9618880491&PlusSearch%5Baccount_id%5D=&PlusSearch%5BanyPayment%5D=&PlusSearch%5Bdate%5D%5B0%5D=&PlusSearch%5Bdate%5D%5B1%5D=&PlusSearch%5Bdescription%5D=&PlusSearch%5Bpayment_category_id%5D=&PlusSearch%5Bcreated%5D%5B0%5D=&PlusSearch%5Bcreated%5D%5B1%5D=&PlusSearch%5Buser%5D=&PlusSearch%5Bpay_type%5D=&PlusSearch%5Bpay_system%5D='
        )
        driver.find_element(By.XPATH, '//button[@title="Удалить"]').click()
        driver.find_element(By.ID, 'plusdeleteform-deletion_comment').send_keys('Автотест ОП')
        driver.find_element(By.XPATH, '//div[@class="modal-footer"]/button[contains(text(), "Удалить")]').click()

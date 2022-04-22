import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def sber_url(lk_url):
    token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
    headers = {'accept': 'application/json',
               'Authorization': f'Bearer {token}',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    lk_url = "https://api.lk.bezlimit.ru/v1"
    data = {
        "phone": 9006471111,
        "amount": 30,
        "successUrl": "https://bezlimit.ru/payment/?page=success&phone=9006471111&amount=30",
        "failUrl": "https://bezlimit.ru/payment/?page=error&phone=9006471111&amount=30"
    }
    request_url = f"{lk_url}/phone/finance/payment-sber"
    response = requests.post(request_url, headers=headers, data=data)
    des_response = str(response.json())
    return des_response


url_prod = sber_url("https://api.lk.bezlimit.ru/v1").split(': ')[1].replace("'", "").replace("}", "")
url_dev = sber_url("https://lktest.bezlimit.ru/v1").split(': ')[1].replace("'", "").replace("}", "")

print(url_prod)
print(url_dev)

chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\Users\morozov_i\PycharmProjects\bezlimitapi\driver\chromedriver.exe')

input_card = 5364150664099019
input_date = 0o327
input_cvc = 662


for url in (url_prod, url_dev):
    driver.get(url)
    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[3]/form/div[8]/button')
    except:
        print('Неудача0.')
    time.sleep(5)
    for _ in range(3):
        card = driver.find_element(By.XPATH, '//*[@id="pan"]')
        date = driver.find_element(By.XPATH, '//*[@id="expiry"]')
        cvc = driver.find_element(By.XPATH, '//*[@id="cvc"]')

        card.send_keys(input_card)
        date.send_keys(input_date)
        cvc.send_keys(input_cvc)
        time.sleep(2)

        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[3]/form/div[8]/button')
        button.click()

        time.sleep(5)
    try:
        driver.find_element(By.XPATH, '/html/body/main/div/div[1]/button')
    except:
        print('Неудача1.')

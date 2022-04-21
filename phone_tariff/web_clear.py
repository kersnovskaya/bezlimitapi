from tests.phone_tariff.test_put_phone_tariff_change import Test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\Users\morozov_i\PycharmProjects\bezlimitapi\driver\chromedriver.exe')


def authorize():
    driver.get('https://bill.bezlimit.ru/site/login')

    time.sleep(7)

    login_input = driver.find_element(By.ID, 'loginform-username')

    login_input.send_keys('morozov_i')

    password_input = driver.find_element(By.ID, 'loginform-password')

    password_input.send_keys('Takkurwatak1')

    button_enter = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[4]/div[2]/div[1]/button')

    button_enter.click()


authorize()

driver.get('https://bill.bezlimit.ru/phone/card/tasks/9006471111')


status_list = driver.find_element(By.XPATH, f'//*[@id="grid-container"]/table/tbody/tr[1]/td[8]/a')
status_list.click()

select = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[5]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/div[2]/div/form/div/div[1]/div[1]/select'))
select.select_by_value('3')

button1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[5]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/div[2]/div/form/div/div[1]/div[2]/button[1]')
button1.click()

time.sleep(2)

status_list = driver.find_element(By.XPATH, f'//*[@id="grid-container"]/table/tbody/tr[2]/td[8]/a')
status_list.click()

select = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[5]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/table/tbody/tr[2]/td[8]/div/div[2]/div/form/div/div[1]/div[1]/select'))
select.select_by_value('3')

button2 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div[5]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/table/tbody/tr[2]/td[8]/div/div[2]/div/form/div/div[1]/div[2]/button[1]')
button2.click()

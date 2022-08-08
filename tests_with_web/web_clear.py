from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path=r'C:\Users\morozov_i\PycharmProjects\bezlimitapi\driver\chromedriver.exe')


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
driver.get('https://bill.bezlimit.ru/phone/card/tasks/9621110832')
time.sleep(10)
status_list = driver.find_elements(By.XPATH, '//a[@class="editable editable-click"]')
status_list[0].click()
driver.find_element(By.XPATH, '//select[@class="form-control input-sm"]').click()
driver.find_element(By.XPATH, '//div[@class="editable-input"]//option[@value="3"]').click()
driver.find_element(By.XPATH, '//i[@class="fa fa-check"]').click()
time.sleep(5)
status_list[1].click()
driver.find_element(By.XPATH, '//select[@class="form-control input-sm"]').click()
driver.find_element(By.XPATH, '//div[@class="editable-input"]//option[@value="3"]').click()
driver.find_element(By.XPATH, '//i[@class="fa fa-check"]').click()

import requests

# porn = [
#   {
#     "phone": 9006471111
#   },
#   {
#     "phone": 9032417766
#   },
#   {
#     "phone": 9032526426
#   },
#   {
#     "phone": 9064442514
#   },
#   {
#     "phone": 9064442671
#   },
#   {
#     "phone": 9064603113
#   },
#   {
#     "phone": 9605554826
#   },
#   {
#     "phone": 9612229359
#   },
#   {
#     "phone": 9618885971
#   },
#   {
#     "phone": 9633243809
#   },
#   {
#     "phone": 9633244519
#   },
#   {
#     "phone": 9654513918
#   },
#   {
#     "phone": 9654514087
#   },
#   {
#     "phone": 9672999985
#   },
#   {
#     "phone": 9682220793
#   },
#   {
#     "phone": 9682220854
#   },
#   {
#     "phone": 9682221451
#   },
#   {
#     "phone": 9682223481
#   },
#   {
#     "phone": 9682224854
#   }
# ]
#
# asshole = [
#   {
#     "phone": 9006471111
#   },
#   {
#     "phone": 9032417766
#   },
#   {
#     "phone": 9032526426
#   },
#   {
#     "phone": 9039944222
#   },
#   {
#     "phone": 9064442671
#   },
#   {
#     "phone": 9064603113
#   },
#   {
#     "phone": 9090691313
#   },
#   {
#     "phone": 9092224586
#   },
#   {
#     "phone": 9587774144
#   },
#   {
#     "phone": 9605554826
#   },
#   {
#     "phone": 9612229359
#   },
#   {
#     "phone": 9614828609
#   },
#   {
#     "phone": 9618885971
#   },
#   {
#     "phone": 9633243809
#   },
#   {
#     "phone": 9633244519
#   },
#   {
#     "phone": 9682220793
#   }
# ]
#
# sex = []
# shmex = []
# for i in porn:
#     sex.append(i['phone'])
#
# for i in asshole:
#   shmex.append(i['phone'])
#
# print(len(sex))
#
# anal = [9006471111,
#
#         9032417766,
#
#         9032526426,
#
#         9039944222,
#
#         9064442514,
#
#         9064442671,
#
#         9064603113,
#
#         9090691313,
#
#         9605554826,
#
#         9612229359,
#
#         9614828609,
#
#         9618885971,
#
#         9633243809,
#
#         9633244519,
#
#         9654513918,
#
#         9654514087,
#
#         9672999985,
#
#         9682220854,
#
#         9682221451,
#
#         9682223481,
#
#         9682224854,
#
#         9682224918]
#
#
# print(len(anal))
# print(len(shmex))
#
# print(set(anal).difference(sex))
# print(set(anal).difference(shmex))


# a_list = [1, 2, 3]
# count = 0
#
# for i in a_list:
#     shit = a_list[:]
#     shit.remove(i)
#     count += 1

# import random
# from datetime import datetime
# from datetime import timedelta
#
#
# def date_generate(days):
#     start = datetime.today() + (datetime.today() - datetime(year=2021, month=3, day=1)) * random.random()
#     maxdate = str(start).split()[0]
#     maxfiledate = maxdate.split('-')
#     maxfiledate.reverse()
#     endfiledate = '.'.join(maxfiledate)
#
#     end = start - timedelta(days=days)
#     mindate = str(end).split()[0]
#     minfiledate = mindate.split('-')
#     minfiledate.reverse()
#     startfiledate = '.'.join(minfiledate)
#
#     return maxdate, endfiledate, mindate, startfiledate
#
#
# print(date_generate(30)[0])


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

driver.get('https://bill.bezlimit.ru/phone/card/tasks/9612224930')


status_list = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[5]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/table/tbody/tr[1]/td[8]/a')
status_list.click()

select = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[5]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/div[2]/div/form/div/div[1]/div[1]/select'))
select.select_by_value('3')

button1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[5]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/div[2]/div/form/div/div[1]/div[2]/button[1]')
button1.click()

time.sleep(2)

status_list = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[5]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/table/tbody/tr[2]/td[8]/a')
status_list.click()

select = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[5]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/table/tbody/tr[2]/td[8]/div/div[2]/div/form/div/div[1]/div[1]/select'))
select.select_by_value('3')

button2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[5]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/table/tbody/tr[2]/td[8]/div/div[2]/div/form/div/div[1]/div[2]/button[1]')
button2.click()



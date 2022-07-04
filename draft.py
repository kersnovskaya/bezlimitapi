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

# def test_sex():
#     message = ['Выводит список всех номеров в аккаунте. Корректный запрос с полем "query".']
#     expected_message = ['Выводит список всех номеров в аккаунте. Корректный запрос с полем "query".']
#
#     token = 'iP0vKgl5ODvOIDkRDINyKDw6DL4SVurnZoBW1wu-PPS84W3X_0MZennm9G7Vea6_'
#     lktest_url = "https://lktest.bezlimit.ru/v1"
#
#     queries_fields = ['phone', 'name', 'is_disable_delete', 'is_adding_confirmed']
#
#     for field in queries_fields:
#         request_url = f'{lktest_url}/account/phone'
#         headers = {'accept': 'application/json',
#                    'Authorization': f'Bearer {token}'}
#         params = {'fields': field}
#         response = requests.get(request_url, headers=headers, params=params)
#         try:
#             assert response.status_code == 200
#         except AssertionError:
#             message.append(f"Код ответа {response.status_code}, а не 200.")
#
#         for i in response.json():
#             for v in i:
#                 short_fields = queries_fields[:]
#                 short_fields.remove(field)
#                 try:
#                     assert v not in short_fields
#                 except AssertionError:
#                     message.append(f'В параметрах ответа присутствуют типы данных кроме "{v}".')
#                     break

#
# keys = [
#     'id',
#     'title',
#     'short_description',
#     'description',
#     'type',
#     'payment_period',
#     'connection_cost',
#     'subscription_fee',
#     'can_be_deferred',
#     'cannot_be_disabled',
#     'is_cannot_disconnect_in_lk',
#     'is_hit',
#     'is_confirmed_passport_required'
# ]
#
# sex_dick_asshole = list({
#     "id": 243749,
#     "title": "Продли скорость 5 Гб",
#     "short_description": "<p><strong>Докупите 5 Гб скоростной мобильный интернет до конца расчетного периода!</strong></p>",
#     "description": "<p><strong>Докупите 5Гб  скоростной мобильный интернет до конца расчетного периода!</strong></p><p><strong>Услуга подключается раз в два дня и не имеет абонентской платы.<br></strong><strong>Стоимость подключения услуги - <span style=\"color: rgb(192, 80, 77);\">290</span> руб.</strong></p>",
#     "type": {
#       "id": 5,
#       "name": 5,
#       "tmp_name": "Интернет"
#     },
#     "payment_period": "раз в месяц",
#     "connection_cost": "290.00",
#     "subscription_fee": "0.00",
#     "can_be_deferred": False,
#     "cannot_be_disabled": False,
#     "is_cannot_disconnect_in_lk": False,
#     "is_hit": True,
#     "packet_value": 5
#   }.keys())
#
# print(set(keys).difference(sex_dick_asshole))
# print(set(sex_dick_asshole).difference(keys))

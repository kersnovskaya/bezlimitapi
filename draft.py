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

ass = {
    "items": [
        {
            "id": 146050,
            "user_id": 362799,
            "login": "410704",
            "name": "tst",
            "phone": 9951345486,
            "level": 1,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 5,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 145828,
            "user_id": 362272,
            "login": "409594",
            "name": "ТЕСТ ТЕСТ ТЕСТ",
            "phone": 9052770442,
            "level": 2,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 9,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 145609,
            "user_id": 361405,
            "login": "408499",
            "name": "татвовььв --",
            "phone": 9999999999,
            "level": 1,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 5,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 145088,
            "user_id": 359202,
            "login": "405894",
            "name": "тест тест",
            "phone": 9657111786,
            "level": 1,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 5,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 145083,
            "user_id": 359185,
            "login": "405869",
            "name": "тест тест тест",
            "phone": 9602370769,
            "level": 1,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 5,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 145082,
            "user_id": 359184,
            "login": "405864",
            "name": "тест тест тест",
            "phone": 9602403367,
            "level": 1,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 5,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 145066,
            "user_id": 359125,
            "login": "405784",
            "name": "Test Test Test",
            "phone": 9052259448,
            "level": 2,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 9,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 145055,
            "user_id": 359085,
            "login": "405729",
            "name": "ТЕСТ ТЕСТ ТЕСТ",
            "phone": 9052811020,
            "level": 2,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 9,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 145053,
            "user_id": 359080,
            "login": "405719",
            "name": "Тест Тестов Тестович",
            "phone": 9052257817,
            "level": 1,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 5,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 145049,
            "user_id": 359070,
            "login": "405699",
            "name": "ТЕСТ ТЕСТ ТЕСТ",
            "phone": 9052259542,
            "level": 2,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 9,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 144972,
            "user_id": 358818,
            "login": "405314",
            "name": "Член Общества",
            "phone": 9915763263,
            "level": 1,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 5,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 144964,
            "user_id": 358791,
            "login": "405274",
            "name": "ТЕСТ ТЕСТ ТЕСТ",
            "phone": 9003379595,
            "level": 2,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 9,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 144949,
            "user_id": 358752,
            "login": "405199",
            "name": "ТЕСТ ТЕСТ ТЕСТ",
            "phone": 9619992783,
            "level": 1,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 5,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 144454,
            "user_id": 356145,
            "login": "402444",
            "name": "Тест очереди",
            "phone": 9642226804,
            "level": 1,
            "activation": {
                "total_cnt": 1,
                "total_personal_cnt": 1,
                "total_level_cnt": 0,
                "current_month_cnt": 1,
                "current_month_personal_cnt": 1,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 1,
                "last_month_personal_cnt": 1,
                "last_month_level_cnt": 0,
                "last_date": "2022-08-05"
            },
            "loyalty": {
                "id": 5,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 144009,
            "user_id": 353607,
            "login": "400223",
            "name": "Зимоглядова Ирина",
            "phone": 9619187863,
            "level": 2,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 9,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 144006,
            "user_id": 353600,
            "login": "400208",
            "name": "Зимоглядов Сергей",
            "phone": 9198598492,
            "level": 1,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 5,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 143503,
            "user_id": 351451,
            "login": "397693",
            "name": "рв вапв вап",
            "phone": 9064447536,
            "level": 2,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 9,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 143504,
            "user_id": 351452,
            "login": "397703",
            "name": "рв вапв вап",
            "phone": 9064447536,
            "level": 2,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 9,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 143505,
            "user_id": 351453,
            "login": "397713",
            "name": "рв вапв вап",
            "phone": 9064447536,
            "level": 2,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 9,
                "code": "bronze",
                "name": "Бронза"
            }
        },
        {
            "id": 143506,
            "user_id": 351454,
            "login": "397718",
            "name": "рв вапв вап",
            "phone": 9064447536,
            "level": 2,
            "activation": {
                "total_cnt": 0,
                "total_personal_cnt": 0,
                "total_level_cnt": 0,
                "current_month_cnt": 0,
                "current_month_personal_cnt": 0,
                "current_month_level_cnt": 0,
                "previous_month_cnt": 0,
                "previous_month_personal_cnt": 0,
                "previous_month_level_cnt": 0,
                "last_month_cnt": 0,
                "last_month_personal_cnt": 0,
                "last_month_level_cnt": 0,
                "last_date": ""
            },
            "loyalty": {
                "id": 9,
                "code": "bronze",
                "name": "Бронза"
            }
        }
    ],
    "_meta": {
        "totalCount": 48,
        "pageCount": 3,
        "currentPage": 1,
        "perPage": 20
    }
}

for little_shit in ass['items']:
    sex = (list(little_shit.keys()))
    for asshole in sex:
        print(little_shit[asshole])

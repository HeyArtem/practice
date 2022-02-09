import json

# https://youtu.be/rIhygmw9HZM
# json - JavaScript Object Notation
# load считываем фаил json

# # это строка
# str_json = """
# {
#     'responce':{
#         'count': 212121,
#         'item': [{
#             'first_name': 'Лиза',
#             'id': 232323,
#             'last_name': 'Соколова',
#             'can_access': true
#         }, {
#             'first_name': 'Рома',
#             'id': 454545,
#             'last_name': 'Малышев',
#             'can_access': true
# }]
# }
# }"""
# print(type(str_json))
#     # <class 'str'>
#
# #  преобразуем ее в питоновский объект
#
# # loads считываем строку в формате json преобразуем в питон
# # и это не работает
# data = json.loads(str_json)
# print(data)
# print(type(data))



# метод dump создает фаил



#  метод dumps создает строку в виде json


# def get_data_json(url, headers):
#     # r = requests.get(url=url, headers=headers)
#
#     # # сохраняю json минуя промежуточную переменную
#     # with open('data_json_main.json', 'w') as file:
#     #     json.dump(r.json(), file, indent=4, ensure_ascii=False)
#
#     # читаю json  в фаил. Помещаю результат в [], что бы это стал список
#     with open('data_json_main.json') as file:
#         list_json = [json.load(file)]


#  load когда считываем фаил json
#  loads когда считываем строку в формате json

# dump создает фаил
# dumps создает строку в виде json
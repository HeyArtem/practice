import random

'''
Задача сделать код, который рандомно выберет 
двух разных  победителей из списка
'''

# Вар 1. Код выбирает двух, но может выбрать два раза одного и того же учстника
my_list = [
    {'U1': 'Oleg'},
    {'U2': 'Zina'},
    {'U3': 'Sveta'},
    {'U4': 'Vera'}
]

for user in range(2):
    random_user = random.choice(my_list)
    # print(random_user)

    # {'U4': 'Vera'}
    # {'U4': 'Vera'}
    
# Вар 2. Код выбирает двух,  и они не повторяются
my_list_2 = [
    {'U1': 'Oleg'},
    {'U2': 'Zina'},
    {'U3': 'Sveta'},
    {'U4': 'Vera'}
]

# print('Вар 2.')
# print(random.sample(my_list_2, 2))

# Вар 3. 
#  метод  popitem() удаляет и возвращает СЛУЧАЙНУЮ пару

my_list_3_d = [
    {'U1': 'Oleg'},
    {'U2': 'Zina'},           # Это список словарей!!!!!!!!!!!! 
    {'U3': 'Sveta'},
    {'U4': 'Vera'}
]

my_list_3 = {
    'U1': 'Oleg',
    'U2': 'Zina',
    'U3': 'Sveta',                # А это? 
    'U4': 'Vera'   
}

print('Вар 3')
print(my_list_3.popitem())
print(my_list_3.popitem())


print(type(my_list_3_d))
print(type(my_list_3))

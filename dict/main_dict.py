#  По видео от Макса

# 'name': 'Victor'
# 'age': 30

my_dict1 = {}
my_dict2 = dict()

# print(type(my_dict1))   #<class 'dict'>
# print(type(my_dict2))   #<class 'dict'>

my_dict = {
    'user': 'Tomas Anderson',
    'nickname': 'Neo',
    'team': ['Morphius', 'Trinity'],
    1: 'Matrix',
    'has': 'you',
    (1, 2, 3): 'Hello' # кортеж тоже может быть ключем (это редкость), а список нет, потому что он изменяемый
}

# print(my_dict)
# {'user': 'Tomas Anderson', 'nickname': 'Neo', 'team': ['Morphius', 'Trinity'], 1: 'Matrix', 'has': 'you', (1, 2, 3): 'Hello'}


# если нужно получить значение, обращаемся к ключу
# print(my_dict['user'])  #Tomas Anderson
# print(my_dict[1])   #Matrix
# print(my_dict[(1, 2, 3)])   #Hello

month = {
    1: 'January',
    2: 'February'
}

# print(month[2])     #February

# можно всегда добавлять пары
person = {
    'Имя': 'Виктор',
    'Возраст': 27,
    'Рост': 180
}
# print(person)   #{'Имя': 'Виктор', 'Возраст': 27, 'Рост': 180}

# добавляем
person['Вес'] = 93
person['Любимое блюдо'] = 'Карбонара'
# print(person)   #{'Имя': 'Виктор', 'Возраст': 27, 'Рост': 180, 'Вес': 93, 'Любимое блюдо': 'Карбонара'}


# можно измкнить значение у любого ключа 
person['Вес'] = 666
# print(person)   #{'Имя': 'Виктор', 'Возраст': 27, 'Рост': 180, 'Вес': 666, 'Любимое блюдо': 'Карбонара'}


# можно удвлить пару
del person['Любимое блюдо']
# print(person)   #{'Имя': 'Виктор', 'Возраст': 27, 'Рост': 180, 'Вес': 666}


person['Машина'] = 'Porsche'

# перебираем все пары в словаре. Метод items() возвращает список пар  ключ:значение
# for k, v in person.items():
#     print(f'{k} >>> {v}')
    
                            # Имя >>> Виктор
                            # Возраст >>> 27
                            # Рост >>> 180
                            # Вес >>> 666
                            # Машина >>> Porsche



# первый метод получения ключей.   ПРоходя в цикле, не указывая метод, мы получаем все ключи
# for key in person:
#     print(key)
    
        #     Имя
        # Возраст
        # Рост
        # Вес 
        # Машина

# второй метод получения словарей. Используем метод  keys()
# for key in person.keys():
#     print(key)
    
        #     Имя
        # Возраст
        # Рост 
        # Вес
        # Машина


# проверка, на наличие определенного ключа в словаре.  Метод  .keys() можно не использовать!
# if 'Сипл Димпл' in person.keys():
#     print('Ключ уже используется')
# else:
#     print('Такого ключа нет, можете использовать его для создания пары')
    #Такого ключа нет, можете использовать его для создания пары


# ЕСли нужно перебрать только значения из словаря   values()
# for v in person.values():
#     print(v)
    
        #     Виктор
        # 27
        # 180
        # 666
        # Porsche
        

# добавим пару у которой в значениях будет список (Любимое блюдо) и пробежимся в цикле по значениям этого ключа                                 
person_eat = {
    'Имя': 'Виктор',
    'Возраст': 27,
    'Рост': 180,
    'Любимое блюдо': ['Карбонара', 'Пельмешки', 'Картошка с грибами'],
    'Машина': 'Porshe'
}

# for v in person_eat['Любимое блюдо']:
#     print(v)
    
        #     Карбонара
        # Пельмешки
        # Картошка с грибами
        

# работа с конструкцией словарь в словаре
person_dict_in_dict = {
    'Виктор':{
        'Возраст': 27,
        'Рост': 180,
        'Вес': 100,
        'Любимое блюдо': ['Карбонара', 'Пельмешки', 'Картошка с грибами'],
        'Машина': 'Porshe'
    },
    'Robi':{
        'Возраст': 234,
        'Рост': 150,
        'Вес': 400,
        'Любимое блюдо': ['Porich', 'Tomatto', 'Redish'],
        'Машина': 'Reno'
    },   
}
# Виктор и Robi это КЛЮЧИ, а  информация о них (словари) это их ЗНАЧЕНИЯ                                             
# Выведем некоторую информацию
# for username, userinfo in person_dict_in_dict.items():
#     print(f'Имя пользователя: {username}')
#     age = userinfo['Возраст']
#     car = userinfo['Машина']
    
#     print(f'Возраст пользователя {username}: {age} лет')
#     print(f'Авто пользователя {username}: {car}\n')
    
        #     Имя пользователя: Виктор
        # Возраст пользователя Виктор: 27 лет
        # Авто пользователя Виктор: Porshe

        # Имя пользователя: Robi
        # Возраст пользователя Robi: 234 лет
        # Авто пользователя Robi: Reno
        
        
        
# так же при работе со словарями поможет метод get() (возвращает значения по указанному ключу). 
# В случае отсутствия в словаре запрашиваемого ключа, он выдаст нам   # None   или может вывести, что мы пожелаем 
# print(person_eat.get('Должность'))
        # None
        
# здесь я запрограммировал вывод фразу в случае отсутствия ключа 
print(person_eat.get('Должность', 'Чиво Чиво тебе надо?'))
        
        # Чиво Чиво тебе надо?


# метод setdefault() возвращает ключ, а если такого нет, создает пару со значением
# print(person_eat.setdefault('Кока-Кола'))  
        #None
        
# контр-я распечатка, что бы увидеть новую пару в славре  'Кока-Кола': None
# print(person_eat)
        #{'Имя': 'Виктор', 'Возраст': 27, 'Рост': 180, 'Любимое блюдо': ['Карбонара', 'Пельмешки', 'Картошка с грибами'], 'Машина': 'Porshe', 'Кока-Кола': None} 


# Метод copy() возвращает копию словаря
copy_person_eat = person_eat.copy()
# print(copy_person_eat)
        #{'Имя': 'Виктор', 'Возраст': 27, 'Рост': 180, 'Любимое блюдо': ['Карбонара', 'Пельмешки', 'Картошка с грибами'], 'Машина': 'Porshe'}


# Метод update() добавляет новые пары в словарь
person_eat.update({'Профессия': 'Doctor'})
# print(person_eat)

        #{'Имя': 'Виктор', 'Возраст': 27, 'Рост': 180, 'Любимое блюдо': ['Карбонара', 'Пельмешки', 'Картошка с грибами'], 'Машина': 'Porshe', 'Профессия': 'Doctor'}

    # а если добавляемый ключ существует, его значение будет перезаписано
person_eat.update({'Профессия': 'Runner'})
# print(person_eat)

        #{'Имя': 'Виктор', 'Возраст': 27, 'Рост': 180, 'Любимое блюдо': ['Карбонара', 'Пельмешки', 'Картошка с грибами'], 'Машина': 'Porshe', 'Профессия': 'Runner'}


# метод pop() удаляет ключ и возвращает значение
# print('Словарь до применения метода pop:', person_eat)
        #{'Имя': 'Виктор', 'Возраст': 27, 'Рост': 180, 'Любимое блюдо': ['Карбонара', 'Пельмешки', 'Картошка с грибами'], 'Машина': 'Porshe', 'Профессия': 'Runner'}
        
# print(person_eat.pop('Имя'))
# print('Словарь ПОСЛЕ применения метода pop:',  person_eat)
        #{'Возраст': 27, 'Рост': 180, 'Любимое блюдо': ['Карбонара', 'Пельмешки', 'Картошка с грибами'], 'Машина': 'Porshe', 'Профессия': 'Runner'}
        
        # вар., если такого ключа нет
# print(person_eat.pop('Цвет панамы'))

        #KeyError: 'Цвет панамы'
        
        # вар., если такого ключа нет, но мы указали, что выводить в таком случае
# print(person_eat.pop('Цвет панамы', 'Нееет такого!'))

        #Нееет такого!
        
        
#  метод  popitem() удаляет и возвращает СЛУЧАЙНУЮ пару
# print(person_eat.popitem())
        #('Профессия', 'Runner')
        
# print(person_eat.popitem())
# print(person_eat.popitem())
# print(person_eat.popitem())
# print(person_eat.popitem())

        # ('Профессия', 'Runner')
        # ('Машина', 'Porshe')
        # ('Любимое блюдо', ['Карбонара', 'Пельмешки', 'Картошка с грибами'])
        # ('Рост', 180)
        # ('Возраст', 27)

# метод   очищает словарь
# person_dict_in_dict.clear()
# print(person_dict_in_dict)
        #{}

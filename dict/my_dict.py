# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])

# alien_0 = {'color': 'green'}
# print(alien_0['color'])

# # Создание пустого словаря
# alien_0 = {}
# print(alien_0)

# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)


# # Изменение значений в словаре
# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")

# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")


# '''
# Рассмотрим более интересный пример: отслеживание позиции пришельца, который
# может двигаться с разной скоростью. Мы сохраним значение, представляющее
# текущую скорость пришельца, и используем его для определения величины гори-
# зонтального смещения:
# '''
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")

# # Пришелец перемещается вправо.
# # Вычисляем величину смещения на основании текущей скорости.
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # Пришелец двигается быстро.
#     x_increment = 3

# # Новая позиция равна сумме старой позиции и приращения.
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print(f"New position: {alien_0['x_position']}")
# print(alien_0)

# # Например, чтобы превратить пришельца со средней скоростью в быстрого,добавьте следующую строку:
# alien_0['speed'] = fast
# # При следующем выполнении кода блок if - elif - else присвоит x_increment большеезначение.


# # Удаление пар «ключ-значение»
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)



# # Словарь с однотипными объектами
# ''' 
#  За последней парой также рекомендуется поставить запятую, 
#  чтобы при необходимости вы смогли легко 
#  добавитьновую пару «ключ-значение» в следующей строке.
# '''
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")



# # Обращение к значениям методом get()
# # если запрашиваемый ключ не существует, то вы получите сообщение об ошибке.
# alien_0 = {'color': 'green', 'speed': 'slow'}
# # print(alien_0['points'])

# '''
# В первом аргументе метода get() передается ключ. Во втором необязательном ар-
# гументе можно передать значение, которое должно возвращаться при отсутствии
# ключа:
# '''
# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0.get('points', 'No point value assigned.')

# print(point_value)
# '''
# Если есть вероятность того, что запрашиваемый ключ не существует, 
# возможно,стоит использовать метод get() вместо синтаксиса с квадратными скобками.

# Если второй аргумент при вызове get() опущен, а ключ не существу-
# ет, то Python вернет специальное значение None — признак того, что значение не существует.
# '''



# Перебор всех пар «ключ-значение»
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

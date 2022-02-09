# переборсписка в цикле
a = [52, 85, 41, 'sum', 'str', 3 + 5j, 6.8]

# i=0
# while i < len(a):
#     print(a[i])
#     i += 1

    # 52
    # 85
    # 41
    # sum
    # str
    # (3 + 5j)
    # 6.8


# перебор с использованием индекса
# for i in range(len(a)):
#     print(a[i])

    # 52
    # 85
    # 41
    # sum
    # str
    # (3 + 5j)
    # 6.8


# # прямой доступ
# for x in a:
#     print(x)

    # 52
    # 85
    # 41
    # sum
    # str
    # (3 + 5j)
    # 6.8


# Enumerate
for i,x in enumerate(a):
    print('Элeмент:', i, 'is:', x)

    # Элeмент: 0 is: 52
    # Элeмент: 1 is: 85
    # Элeмент: 2 is: 41
    # Элeмент: 3 is: sum
    # Элeмент: 4 is: str
    # Элeмент: 5 is: (3 + 5j)
    # Элeмент: 6 is: 6.8
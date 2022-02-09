'''
проверим наличие нестандартных дополнений перед тем, как готовить
пиццу. В следующем примере определяются два списка. Первый список содержит
перечень доступных топпингов, а второй — список топпингов, заказанных клиен-
том. На этот раз каждый элемент из requested_toppings проверяется по списку
доступных топпингов перед добавлением в пиццу:

Если топпинг доступен, он добавляется в пиццу. Если
заказанный топпинг не входит в список, выполняется блок else
'''

# Стоит заметить, что если в пиццерии используется постоянный ассортимент топпингов, этот список можно реализовать в виде кортежа.
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']

# список топпингов,заказанных клиентом
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

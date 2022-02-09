# на уроке с Максом

x = [1, 5, "123", {"1": "xxx"}]
from pprint import pprint

# y = [
#     "name": "surname"
# ]

y = {
    "name": "imya",
    "name2": "imysdjkfhksjf",
    1: [2, 3, 4, "oleg"],
    "user2": {
        "Morphius": {
            "family": [
                {"1": "Olga"},
                {"1": "Victor"},
                {"1": "Sveta"}
            ]
        }
    }
}
# print(y)
# pprint(y)


name = y["name"]
print(name)
print(y["user2"])
print(y["user2"]["Morphius"])
a = y["user2"]["Morphius"]["family"]
print(a)
print(type(a))

for item in a:
    print(item["1"])
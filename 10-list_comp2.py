# con lista random
import random

list_1 = []
list_2 = []
list_com = []  # lista de elementos comunes

for val in range(1,51):  # metemos valores aleatorios en dos listas
    x = random.randint(1,50)
    list_1.append(x)
    x = random.randint(1,50)
    list_2.append(x)

for element in list_1:
    if element in list_2 and element not in list_com:
        list_com.append(element)

print(f"List 1: {list_1}\n")
print(f"List 2: {list_2}\n")
print(f"Common list: {list_com}")
# coger elementos menores que 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
mylist = []

for element in a:
    if element < 5:
        mylist.append(element)

print(mylist)

# para la misma lista, devolver elementos menores a un input

menor = int(input("Print values from the list less than: "))
for element in a:
    if element < menor:
        mylist.append(element)

print(mylist)
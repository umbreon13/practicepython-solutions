def encuentra(lista, Nbus):
    for elem in lista:
        if Nbus == elem:
            return True
    return False


a = [12, 34, 56, 3, 10, 8, 96, 11, 2, 32]

a = set(a)
# N = int(input("Check if the number is in the list: "))
# if N in a:
#     print("It's in the list")
# else:
#     print("It's not in the list")

print(encuentra(a,96))
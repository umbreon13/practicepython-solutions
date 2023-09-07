a = [5, 10, 15, 20, 25]

def last_elem(lista):
    l = len(lista)
    b = [a[0], a[l-1]]
    return b

b = last_elem(a)
print(b)
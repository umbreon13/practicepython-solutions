# teststring = "  this      has a lot    of   spaces and    tabs"
# result = teststring.split()

# listofstrings = ['a', 'b', 'c']
# result = "**".join(listofstrings)

def fun_reverse(userin):
    spl_user = userin.split()
    return " ".join(spl_user[::-1])  # de esta forma lo devuelve al revés

def reverse_v4(x):
  y = x.split()
  y.reverse()
  return " ".join(y)

user = input("Introduce a sentence: ")
lista_rev = fun_reverse(user)
print(lista_rev)

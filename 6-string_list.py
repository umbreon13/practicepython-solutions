#   >>> a = [5, 10, 15, 20, 25, 30, 35, 40]
#   >>> a[1:4]
#   [10, 15, 20]
#   >>> a[6:]
#   [35, 40]
#   >>> a[:-1]
#   [5, 10, 15, 20, 25, 30, 35]
#   >>> a[1:5:2]
#   [10, 20]
#   >>> a[3:0:-1]
#   [15, 10]


# a las string le podemos hacer lo mismo que a las listas
#   string = "example"
#   for c in string: 
#     print "one letter: " + c

user_in = input("Enter the phrase to analyse: ")
l = len(user_in)
reverse_in = user_in[::-1]  # le manda empezar desde el final de la frase o palabra hacia atrás


if reverse_in == user_in:
    print("This is a palindrome \n")
else:
    print("This is not a palindrome \n")

print(reverse_in) 

          



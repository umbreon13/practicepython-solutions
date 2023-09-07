# buscar divisores de un número

print("This program tells you the divisors of a number")
number = int(input("Enter your number: "))

my_list = range(1, number)
div_list = []   #divisors will be stored here

for element in my_list:
    # div = number / element
    if number % element == 0:  # evalúa el resto de la división
        div_list.append(element)  # añade los divisores

print(f"The divisors of {number} are \n{div_list}")

# tiene en cuenta primos:
# if len(div_list) == 1:
#     print(f"{number} is a prime number (only divisible by 1 and itself)")
# else:
#     print(f"The divisors of {number} are \n{div_list}")
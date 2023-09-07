# odd or even number
print("This program tells you if a number is odd or even")
number_in = int(input("Enter a number: "))

if number_in % 4 == 0:  # evalúa si el input es entero y divisible por 4
    print(f"The number {number_in} is even and multiple of 4")
elif number_in % 2 == 0:
    print(f"The number {number_in} is even, but not multiple of 4")
else: 
    print(f"The number {number_in} is odd")

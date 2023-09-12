def max3(x, y, z):
    Nmax = 0
    if x > y and x > z:
        Nmax = x
    elif y > x and y > z:
        Nmax = y
    else:
        Nmax = z
    return Nmax

if __name__ == '__main__':
    print("Please, enter 3 different numbers. The output will be the maximum")
    userin1 = int(input("First number: "))
    userin2 = int(input("Second number: "))
    userin3 = int(input("Third number: "))

    output = max3(userin1, userin2, userin3)
    print(f"The higher numer of those three is: {output}")


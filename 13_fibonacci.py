def fibo(num):
    list_fibo = []
    counter = num

    list_fibo = [1]
    counter = counter - 1

    if counter != 0:
        list_fibo = [1,1]
        counter = counter - 1

    while counter != 0:
        # l = len(list_fibo)
        new_n = list_fibo[-1] + list_fibo[-2]
        list_fibo.append(new_n)
        counter = counter - 1

    return list_fibo

userin = int(input("Enter how many Fibonacci numbers should the program generate: "))
outlist = fibo(userin)
print(outlist)
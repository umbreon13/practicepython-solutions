with open('prime_numbers.txt','r') as read_primes:
    primes = read_primes.read()
with open('happy_numbers.txt','r') as read_happy:
    happy = read_happy.read()

primes_list = primes.split('\n')
happy_list = happy.split('\n')

both = []

for elem in primes_list:
    if elem in happy_list:
        both.append(elem)

print(both)

# otra forma
# def return_prime():
#     with open('primenumbers.txt', 'r') as open_prime:
#         opened = list(open_prime.read().split("\n"))
#     return opened

# def return_happy():
#     with open('happynumbers.txt', 'r') as open_happy:
#         opened = list(open_happy.read().split("\n"))
#     return opened

# one_list = [x for x in return_prime() if x in return_happy()]
# print(one_list)
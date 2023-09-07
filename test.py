userin = 1234
# N_adiv = ["4","4","5","6"]
N_adiv = [4,7,4,6]
userlist = []
# compare_bulls = ["1","2","3","4"]
compare_bulls = [1,2,4,3]
bulls = 0
cows = 0

for element in compare_bulls:
    if element in compare_bulls and element in N_adiv:
        bulls = bulls + 1
        compare_bulls.remove(element)
    bulls = 4 - len(compare_bulls)
        

for i in range(0,3):
    if userlist[i] == N_adiv[i]:
        cows += 1

print(N_adiv[1])
for seq in range(4):
    print(seq)


print(compare_bulls)
print(bulls)
print(cows)
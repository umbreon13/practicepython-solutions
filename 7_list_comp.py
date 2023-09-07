a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# en varias líneas
# evens  = []
# for elem in a:
#     if elem % 2 == 0:
#         evens.append(elem)

# en una línea
evens = [elem for elem in a if elem % 2 == 0]

print(evens)
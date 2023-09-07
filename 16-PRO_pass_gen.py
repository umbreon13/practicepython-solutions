import random

letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
caps = letters.upper()
nums = "0 1 2 3 4 5 6 7 8 9"  # de 0 a 9 incluidos
sp_ch_list = "! @ # $ % & /"

def return_list(user_str):
    spl_list =[]
    spl_str = user_str.split()
    spl_list = [elem for elem in spl_str]
    return spl_list

low_case = return_list(letters)
upp_case = return_list(caps)
numbers = return_list(nums)
sp_ch = return_list(sp_ch_list)

def rand_char(one_list):
    count = 0
    output = []
    while count < 4:
        indice = random.randint(0, len(one_list) - 1)
        if one_list[indice] not in output:
            output.append(one_list[indice])
            count = count + 1
    return output

list1 = rand_char(low_case)
list2 = rand_char(upp_case)
list3 = rand_char(numbers)
list4 = rand_char(sp_ch)
union = list1 + list2 + list3 + list4

lista_rand = random.shuffle(union)
# print(union)

password = "".join(union)
print(password)

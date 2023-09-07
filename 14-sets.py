def rem_dup(user_list):
    user_list = set(user_list)  # elimina elementos repetidos
    user_list = list(user_list)
    return user_list

a = [1, 1, 2, 3, 5, 8, 13, 21, 21, 34, 55, 55, 89, 89]
new_list = rem_dup(a)
print(new_list)
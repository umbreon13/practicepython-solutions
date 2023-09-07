with open('names.txt','r') as read_file:
    names = read_file.read()
# ahora tengo en 'names' todos los nombres guardados en un string enorme

names_list = names.split('\n')  # hago cada nombre, un elemento de la lista
n_names = set(names_list)  # cuántos hay diferentes

names_dic = {}  # aquí meteré key (el nombre) con su valor (su cantidad)
for element in n_names:
    names_dic.update({element:""})  # sin valor asociado ("")

for element in names_list:
    names_dic[element] =  names_list.count(element)

for pair in names_dic.items():
    print(pair)

# en la segunda parte aparece el método readline que ya va por líneas
cat_dic = {}

with open('sun_pics.txt') as read_file:
    img_name = read_file.readline()  # lee línea por línea mientras haya líneas que leer

    while img_name:  # mientras lee las líneas (mietras exista una línea que leer)
        img_name = img_name[3:-26]  # me quedo con la parte del nombre de la imagen que me interesa
        if img_name in cat_dic:  # si ya está en el diccionario, sumo uno a la cuenta
            cat_dic[img_name] += 1
        else:
            cat_dic[img_name] = 1 # si no está, crea automáticamente la key y le da valor 1
        img_name = read_file.readline()

for pair in cat_dic.items():
    print(pair)

# print(cat_dic)
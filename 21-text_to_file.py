import requests
from bs4 import BeautifulSoup

# 1a forma
# with open('file_to_save.txt', 'w') as open_file:  
#     open_file.write('A string to write')

#2a forma 
# open_file = open('file_to_save.txt', 'w')
# open_file.write('A string to write')
# open_file.close()

# primero cogemos el texto de la web
base_url = 'https://cults3d.com/en/contests'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features="html.parser")

filename = input("Save the file as: ")

with open(filename, 'w') as open_file: # si el archivo no existe, Python lo crea / w: write only, r: read only 
    for story_heading in soup.find_all(class_="tbox-title"): #la clase hay que buscarla inspeccionando la página web
        if story_heading.a: 
            open_file.write(story_heading.a.text.replace("\n", " ").strip())
        else: 
            open_file.write(story_heading.contents[0].replace("\n", " ").strip())

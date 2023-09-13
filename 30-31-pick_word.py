import random

with open('norvig_dictionary.txt','r') as read_file:
    lines = read_file.readlines()  # lines is a list with all the words, note that here I used readlineS

i = random.randint(0,len(lines))
print(f"Random word: {lines[i]}")

def f_check(wordtoguess, guessed):
    output = ""
    for elem in wordtoguess:
        if elem in guessed:
            output = output + "".join(elem)
        else:
            output = output + "".join("_")

    return output
    

game_stat = True
word = lines[i].strip()
word_check = []  # letters that have been said
guessed_letters = []
to_show = f_check(word, "")
print(f"{to_show}  |  {len(word)} letters.")
userin = input("Enter a letter: ")

while game_stat == True:
    print(word_check)
    if userin == "quit":
        game_stat= False

    while userin.upper() in word_check:
        userin = input("That letter was already entered! Try a didfferent one: ")

    if userin.upper() in word:
        word_check.append(userin.upper())
        guessed_letters.append(userin.upper())
        to_show = f_check(word, guessed_letters)
        print(f"{to_show}  |  {len(word)} letters.")
        if word == to_show:
            break
        userin = input("Good guess! introduduce the next letter: ")
        
    else:
        word_check.append(userin.upper())
        print(f"{to_show}  |  {len(word)} letters.")
        userin = input("WRONG! That letter is not in the word. Try a different one: ")

if userin == "quit":
    print("Program stopped by the user")
else:
    print("CONGRATULATIONS! You guessed it :)")

                



        


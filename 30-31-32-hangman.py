import random

with open('norvig_dictionary.txt','r') as read_file:
    lines = read_file.readlines()  # lines is a list with all the words, note that here I used readlineS

i = random.randint(0,len(lines))
# print(f"Random word: {lines[i]}")  #for testing purposes

def f_paint(n):
    if n < 1:
        draw = ""
    elif n == 1:
        draw = "        \n\
                  /"
    elif n == 2:
        draw = "        \n\
                 / \\"
    elif n == 3:
        draw = "        \n\
                    \n\
                  | \n\
                 / \\"
    elif n == 4:
        draw = "        \n\
                      \n\
                /  | \n\
                  / \\"
    elif n == 5:
       draw = "        \n\
                       \n\
               /  |  \\\n\
                 / \\" 
    else:
       draw = "        \n\
                _____  \n\
               |X   X| \n\
               |__O__| \n\
               /  |  \\\n\
                 / \\    GAME OVER..."  
    return draw  

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
fails = 0
to_show = f_check(word, "")
print(f"{to_show}  |  {len(word)} letters.")
userin = input("Enter a letter: ")


while game_stat == True:
    print(f"Said letters: {word_check}") 
    
    while userin.upper() in word_check:  # repeated letter
        userin = input("That letter was already entered! Try a didfferent one: ")

    if userin.upper() in word:  # good guess
        word_check.append(userin.upper())
        guessed_letters.append(userin.upper())
        to_show = f_check(word, guessed_letters)
        print(f_paint(fails))
        print(f"{to_show}  |  {len(word)} letters.")
        if word == to_show:  # end of game (WIN)
            restart = input("CONGRATULATIONS! You guessed it. Play again? ('yes'/'no')")
            if restart.lower() == "yes":
                i = random.randint(0,len(lines))
                # print(f"Random word: {lines[i]}")  # for testing purposes
                word = lines[i].strip()
                word_check = []  # letters that have been said
                guessed_letters = []
                fails = 0
                to_show = f_check(word, "")
                print("NEW GAME")
                print(f"{to_show}  |  {len(word)} letters.")
                userin = input("Enter a letter: ")
            elif restart.lower() == "no":
                game_stat= False

        else:
            userin = input(f"Good guess! introduduce the next letter ({6-fails} wrong guesses left): ")
        
    else:  # wrong guess
        word_check.append(userin.upper())
        fails += 1
        if userin.lower() == "quit" or fails >= 6:  # end of game (LOSE or quit)
            restart = input(f"{f_paint(fails)} \nPlay again? ('yes'/'no'): ")
            if restart.lower() == "yes":
                i = random.randint(0,len(lines))
                word = lines[i].strip()
                word_check = []  # letters that have been said
                guessed_letters = []
                fails = 0
                to_show = f_check(word, "")
                print(f_paint(fails))
                print(f"{to_show}  |  {len(word)} letters.")
                userin = input("Enter a letter: ")
            elif restart.lower() == "no":
                game_stat= False
        else:
            print(f"{to_show}  |  {len(word)} letters.   {f_paint(fails)}")
            userin = input(f"WRONG! That letter is not in the word. ({6-fails} wrong guesses left).\nTry a different one: ")


import random
game_stat = True
print("Think a number between 0 and 100, the computer will try to guess it")
number = random.randint(0,100)

while game_stat == True:
    guess = 50
    user = input(f"Is it {guess}? Answer 'higher', 'lower' or 'yes' ")
    if user == "yes":
        game_stat = False
    elif user == "lower":
        guess = 25
        user = input(f"Is it {guess}? Answer 'higher', 'lower' or 'yes' ")
        if user == "yes":
            game_stat = False
        elif user == "lower":
            vector_025 = range(0,25)
            for elem in vector_025:
                guess = elem
                user = input(f"Is it {guess}? Answer 'higher', 'lower' or 'yes' ")
                if user == "yes":
                    game_stat = False
                    break 
        elif user == "higher":
            vector_2550 = range(26,50)
            for elem in vector_2550:
                guess = elem
                user = input(f"Is it {guess}? Answer 'higher', 'lower' or 'yes' ")
                if user == "yes":
                    game_stat = False
                    break
    elif user == "higher":
        guess = 75
        user = input(f"Is it {guess}? Answer 'higher', 'lower' or 'yes' ")
        if user == "yes":
            game_stat = False
        elif user == "lower":
            vector_5175 = range(51,75)
            for elem in vector_5175:
                guess = elem
                user = input(f"Is it {guess}? Answer 'higher', 'lower' or 'yes' ")
                if user == "yes":
                    game_stat = False 
                    break
        elif user == "higher":
            vector_76100 = range(76,101)
            for elem in vector_76100:
                guess = elem
                user = input(f"Is it {guess}? Answer 'higher', 'lower' or 'yes' ")
                if user == "yes":
                    game_stat = False
                    break

print(f"Your number was guessed!! It's {guess}")

            
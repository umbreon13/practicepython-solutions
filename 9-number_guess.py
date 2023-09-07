import random

game_stat = True
rand_n = random.randint(1,9)
counter = 0

while game_stat == True:
    user_in = input("Guess the number from 1 to 9 (or type 'quit' to end the game): ")
    if user_in == 'quit':
        print("GAME OVER")
        game_stat = False
    else:
        user_in = int(user_in)
        if user_in < 1 or user_in > 9:
            print("Number out of range! \nPlease, introduce a number between 1 and 9 or 'quit' to end the game\n")
        elif user_in < rand_n:
            print("Too LOW! Try again: ")
            counter = counter + 1
        elif user_in > rand_n:
            print("Too HIGH! Try again: ")
            counter = counter + 1
        elif user_in == rand_n:
            counter = counter + 1
            print("You NAILED it!! WINNER!!")
            print(f"It took you {counter} guesses to get the correct number")
            game_stat = False

        

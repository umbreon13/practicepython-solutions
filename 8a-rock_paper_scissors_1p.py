import random

game_list = ["rock", "paper", "scissors"]
game_stat = True

user = input("Chosee between\n 'rock',\n 'paper',\n 'scissors': \n")

val = random.randint(0,2)
cpu =game_list[val]    

while game_stat == True:

    while user == cpu:
        user = input("SAME GUESS! Try again: \n")
        val = random.randint(0,2)
        cpu = game_list[val]

    if user == "rock" and cpu == "scissors":
        print(f"Player chose {user} and beats CPU {cpu}")
        print("You're the WINNER!")
    if user == "rock" and cpu == "paper":
        print(f"CPU chose {cpu} and beats Player {user}")
        print("You LOSE!")
    if user == "paper" and cpu == "rock":
        print(f"Player chose {user} and beats CPU {cpu}")
        print("You're the WINNER!")
    if user == "paper" and cpu == "scissors":
        print(f"CPU chose {cpu} and beats Player {user}")
        print("You LOSE!")
    if user == "scissors" and cpu == "paper":
        print(f"Player chose {user} and beats CPU {cpu}")
        print("You're the WINNER!")
    if user == "scissors" and cpu == "rock":
        print(f"CPU chose {cpu} and beats Player {user}")
        print("You LOSE!")
    
    user_game = input("Play again? (Type 'yes' or 'no')")
    if user_game == "no":
        game_stat = False
    else:
        user = input("Chosee between\n 'rock',\n 'paper',\n 'scissors': \n")
        val = random.randint(0,2)
        cpu =game_list[val] 

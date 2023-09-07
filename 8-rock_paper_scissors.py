print("ROCK-PAPER-SCISSORS GAME \n")

user1 = input("First player: ")
user2 = input("Second player: ")


game_stat = True

while game_stat == True:

    while user1 == user2:
        print("SAME GUESS! Try again \n")
        user1 = input("First player: ")
        user2 = input("Second player: ")

    if user1 == "rock" and user2 == "scissors":
        print(f"Player 1 chose {user1} and beats Player 2 {user2}")
        print("Player 1 is the WINNER!")
    if user1 == "rock" and user2 == "paper":
        print(f"Player 2 chose {user2} and beats Player 1 {user1}")
        print("Player 2 is the WINNER!")
    if user1 == "paper" and user2 == "rock":
        print(f"Player 1 chose {user1} and beats Player 2 {user2}")
        print("Player 1 is the WINNER!")
    if user1 == "paper" and user2 == "scissors":
        print(f"Player 2 chose {user2} and beats Player 1 {user1}")
        print("Player 2 is the WINNER!")
    if user1 == "scissors" and user2 == "paper":
        print(f"Player 1 chose {user1} and beats Player 2 {user2}")
        print("Player 1 is the WINNER!")
    if user1 == "scissors" and user2 == "rock":
        print(f"Player 2 chose {user2} and beats Player 1 {user1}")
        print("Player 2 is the WINNER!")
    
    user_game = input("Play again? (Type 'yes' or 'no')")
    if user_game == "no":
        game_stat = False
    else:
        user1 = input("First player: ")
        user2 = input("Second player: ")


        




    

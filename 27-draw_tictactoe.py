h_inputs = []
game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

game_stat = True
counter = 1
player = 1

# 1st user input
print("Type '999' to stop")
in_user = input(f"Player {player}, enter the coordinates; row,col (for example: 1,2 means 1st row, 2nd column)")

while game_stat == True:

    if in_user == 999:  # stop the program
        game_stat = False

    in_user = in_user.strip()
    while in_user in h_inputs:
        in_user = input(f"Turn {counter}. Player {player}, that's position was already covered; choose another (remember: 1,2 means 1st row, 2nd column) ")
        in_user = in_user.strip()
    h_inputs.append(in_user)
    user_list = in_user.split(',')  
    user_row = int(user_list[0]) - 1  # comp 0 is the Nrow and comp 1 is Ncol
    user_col = int(user_list[1]) - 1
    
    if counter % 2 == 0:  #player 1 has X
        game[user_row][user_col] = "O"
        player += 1
        counter += 1
        print(game)
        in_user = input(f"Turn {counter}. Player {player}, enter the coordinates; row,col (for example: 1,2 means 1st row, 2nd column) ")
    else:
        game[user_row][user_col] = "X"
        player -= 1
        counter += 1
        print(game)
        in_user = input(f"Turn {counter}. Player {player}, enter the coordinates; row,col (for example: 1,2 means 1st row, 2nd column) ")
    
    if counter == 9:
        game_stat = False
        print("GAME OVER")
    
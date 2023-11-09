# Full tic tac toe game
#
def f_board(game):
    
    options = {2:" O ",
               1:" X ",
               0: "   "}
    line = " --- --- --- "
    board = ""

    for row in range(0, 3):
        new_row = []
        for col in range(0,3):
            new_row.append(options[game[row][col]])
        board = board + "|" + "|".join(new_row) + "|\n" + line + "\n"

    return line + "\n" + board


# function to check results
def f_check(game):

    # firt, create lists with the elements of the columns and diagonals
    column1 = []
    column2 = []
    column3 = []
    diag_1 = []
    diag_2 = []

    i = 0  # counter for the first diagonal
    j = -1  # counter for the second diagonal

    winner = 0

    for elem in game:

        # create two lists with the elements of the diagonals
        diag_1.append(elem[i])  # list with the elements of the first diagonal
        diag_2.append(elem[j])  # list with the elements of the second diagonal
        i += 1
        j -= 1
        # create lists with the elements of the columns
        column1.append(elem[0])
        column2.append(elem[1])
        column3.append(elem[2])

    # append them to a new list to be checked, including the rows of the game
    game_check = []
    for elem in game:
        game_check.append(elem)
    game_check.extend([diag_1,diag_2,column1,column2,column3])

    for elem in game_check:
        if elem[0] != 0 and elem[0] == elem[1] and elem[1] == elem[2]:  # checks if a row has every element equal
            winner = elem[0]
    print(game_check)
    return winner

def f_player(counter):
    if counter %2 == 0:
        player = 1
    else:
        player = 2
    return player
    
# MAIN function
if __name__ == '__main__':

    h_inputs = []  # history of coordinates in the game
    game = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0]]

    game_stat = True
    counter = 1
    player = 1

    # 1st user input
    print("Type 'quit' to stop")
    in_user = input(f"Player {player}, enter the coordinates; row,col (for example: 1,2 means 1st row, 2nd column): ")

    while game_stat == True and counter < 9:

        if in_user == "quit":  # stop the program
            print("Program stopped by user")
            game_stat = False
            break

        in_user = in_user.strip()
        while in_user in h_inputs:  # ensure there is no repetion in coordinates
            in_user = input(f"Turn {counter}. Player {player}, that's position was already covered; choose another (remember: 1,2 means 1st row, 2nd column): ")
            in_user = in_user.strip()

        h_inputs.append(in_user)
        user_list = in_user.split(',') # make a list, 1st and 2nd coordinate 
        user_row = int(user_list[0]) - 1  # comp 0 is the Nrow and comp 1 is Ncol
        user_col = int(user_list[1]) - 1
        
        game[user_row][user_col] = player   # add the player to the game matrice
        print(game)
        print(f_board(game))  #draws the board
        winner = f_check(game)


        if winner != 0:
            print(f_board(game))
            print(f"Player {winner} is the WINNER")
            game_stat = False
            break
        else:
            player = f_player(counter)
            counter += 1
            print(f_board(game))
            print(winner)
            in_user = input(f"Turn {counter}. Player {player}, enter the coordinates; row,col (for example: 1,2 means 1st row, 2nd column) ")
        

    print(f_board(game))
    print("GAME OVER")
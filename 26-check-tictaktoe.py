game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

game_stat = True
# firt, create lists with the elements of the columns and diagonals
column1 = []
column2 = []
column3 = []
diag_1 = []
diag_2 = []

i = 0  # counter for the first diagonal
j = -1  # counter for the second diagonal


for elem in game:

    # create two lists with the elements of the diagonals
    diag_1.append(elem[i])  # list with the elements of the firs diagonal
    diag_2.append(elem[j])  # list with the elements of the second diagonal
    i += 1
    j -= 1
    # create lists with the elements of the columns
    column1.append(elem[0])
    column2.append(elem[1])
    column3.append(elem[2])

# append them to a new list to be checked, including the rows of the game
game_check = game
game_check.extend([diag_1,diag_2,column1,column2,column3])

for elem in game_check:
    if len(set(elem)) <= 1:  # checks if a row has every element equal
        winner = elem[0]
        print(f"The winner is Player {winner}")
        game_stat = False
        break

if game_stat == True:
    print("No winner")
    game_stat = False


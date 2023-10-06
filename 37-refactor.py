# this code builds a game board length x width introduced by the user

def fun_board(length, width):
    count_l = 0
    count_w = 0
    lines = " "
    bars = "|   "
    board = ""
    while count_w < width:
        while count_l < length:
            lines = lines + "--- "
            bars = bars + "|   "
            count_l = count_l + 1
        board = board + f"{lines} \n{bars}\n"
        count_w = count_w + 1
    board = board + lines
    return board

print("Draw a game board:")
l = int(input("Length: "))
w = int(input("Width: "))
board = fun_board(l,w)

print(board)
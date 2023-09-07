# this code builds a game board length x width introduced by the user
print("Draw a game board:")
length = int(input("Length: "))
width = int(input("Width: "))


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

print(board + lines)
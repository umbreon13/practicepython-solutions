import random

def adivinar():  # genera un número aletorio de 4 cifras que hay que adivinar
    N = []
    while len(N) < 4:
        N.append(random.randint(0,9))
    return N

def comparador(userin):

    userlist = []
    cowbulls = [0, 0]  # [0] cows and [1] bulls
    compare_bulls = []  # se añaden bulls cuando coincide algún número

    for elem in userin:
        elem = int(elem)
        userlist.append(elem)  # pone el string del input como lista, número a número

    for element in userlist:
        compare_bulls.append(element)
        if element in compare_bulls and element in N_adiv:
            compare_bulls.remove(element)
    cowbulls[1] = 4 - len(compare_bulls)  # esto en realidad es cows+bulls sin diferenciarlos

    for i in range(4):
        if userlist[i] == N_adiv[i]:
            cowbulls[0] += 1
    cowbulls[1] = cowbulls[1] - cowbulls[0]

    return cowbulls

# if __name__=="__main__":
game_stat = True
N_adiv = adivinar()
userin = input("Make your guess - enter a 4-digit number \n(COW: good guess in the correct place \n BULL: guess in the incorrect place): ")
attempts = 0

while game_stat == True:

    attempts += 1
    listcb = comparador(userin)
    if listcb[0] == 4:
        list_number = []
        for n in N_adiv:
            list_number.append(str(n))
        print(f"YOU WIN!! You guessed the whole number after {attempts} attempts!! \n{list_number[0]+list_number[1]+list_number[2]+list_number[3]}")
        game_stat = False
    elif userin == "quit":
        game_stat = False
    else:
        print(f"You have {listcb[0]} cows and {listcb[1]} bulls \n Number of attempts: {attempts} \n")
        userin = input("Guess again (or type 'quit' to exit): ")
        if userin == "quit":
            game_stat = False
        # listcb = comparador(userin)
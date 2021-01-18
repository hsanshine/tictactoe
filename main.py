#tic tac toe game
import random
from replit import clear


def print_board(n):
    clear()
    for x in n:
        for i in range(len(x)):
            print(x[i], end='     ')
        print('\n\n')


def IsWon(n):
    fire = '🔥'
    ice = '🧊'
    if (n[0][0] == n[0][1] == [0][2] == fire):
        print('\n***fire wins***\n')
        return True
    elif (n[0][0] == n[0][1] == n[0][2] == ice):
        print('\n**ice wins***\n')
        return True
    elif (n[1][0] == n[1][1] == n[1][2] == fire):
        print('\n***fire wins\n')
        return True
    elif (n[1][0] == n[1][1] == n[1][2] == ice):
        print('\n***ice wins***\n')
        return True
    elif (n[2][0] == n[2][1] == n[2][2] == fire):
        print('\n***fire wins***\n')
        return True
    elif (n[2][0] == n[2][1] == n[2][2] == ice):
        print('\n***ice wins***\n')
        return True
    elif (n[0][0] == n[1][1] == n[2][2] == fire):
        print('\n***fire wins***\n')
        return True
    elif (n[0][0] == n[1][1] == n[2][2] == ice):
        print('\n***ice wins***\n')
        return True
    elif (n[0][2] == n[1][1] == n[2][0] == fire):
        print('\n***fire wins***\n')
        return True
    elif (n[0][2] == n[1][1] == n[2][0] == ice):
        print('\n***ice wins***\n')
        return True
    elif (n[0][0] == n[1][0] == n[2][0] == fire):
        print('\n***fire wins***\n')
    elif (n[0][0] == n[1][0] == n[2][0] == ice):
        print('\n***ice wins***\n')
        return True
    elif (n[0][1] == n[1][1] == n[2][1] == fire):
        print('\n***fire wins***\n')
        return True
    elif (n[0][1] == n[1][1] == n[2][1] == ice):
        print('\n***ice wins***\n')
        return True
    elif (n[0][2] == n[1][2] == n[2][2] == fire):
        print('\n***fire wins***\n')
        return True
    elif (n[0][2] == n[1][2] == n[2][2] == ice):
        print('\n***ice wins***\n')
        return True
    else:
        return False


def mark(position, moji, n):
    if (position == '1'):
        n[0][0] = moji
    elif (position == '2'):
        n[0][1] = moji
    elif (position == '3'):
        n[0][2] = moji
    elif (position == '4'):
        n[1][0] = moji
    elif (position == '5'):
        n[1][1] = moji
    elif (position == '6'):
        n[1][2] = moji
    elif (position == '7'):
        n[2][0] = moji
    elif (position == '8'):
        n[2][1] = moji
    elif (position == '9'):
        n[2][2] = moji


played_spots = set()


def comp_play(board):
    rand = random.randint(1, 9)
    while (str(rand) in played_spots):
        rand = random.randint(1, 9)
    played_spots.add(str(rand))
    #print(played_spots)
    print('comp choose to play : ' + str(rand) + '\n')
    return rand


def IsDraw(n):
    if (str(n[0][0]).isdigit() or str(n[0][1]).isdigit()
            or str(n[0][2]).isdigit() or str(n[1][0]).isdigit()
            or str(n[1][1]).isdigit() or str(n[1][2]).isdigit()
            or str(n[2][0]).isdigit() or str(n[2][1]).isdigit()
            or str(n[2][2]).isdigit()):
        return False
    else:
        print("\n***it is a draw***")
        return True


a = '🎅'
fire = '🔥'
ice = '🧊'

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#board =[[fire,ice,fire],[ice,fire,fire],[ice,fire,ice]]
print_board(board)


def payer_turn(board):
    position = input('\nchoose a position to play : ')
    while (position in played_spots):
        position = input('\nchoose another position to play : ')
    played_spots.add(position)
    mark(position, player, board)
    print_board(board)


def comp_turn(board):
    position = comp_play(board)
    mark(str(position), comp, board)
    print_board(board)


first = random.randint(0, 1)
if (first == 0):
    print('\ndo you want to play as "fire" or as "ice"?')
    choice = input('"fire" or "ice " ? : ')
    if (choice == 'fire'):
        player = fire
        comp = ice
    else:
        player = ice
        comp = fire
else:
    print("comp will play first as 'fire'\n ")
    player = ice
    comp = fire
    comp_turn(board)

while (True):
    if (IsWon(board)):
        break
    elif (IsDraw(board)):
        break
    else:
        payer_turn(board)

    if (IsWon(board)):
        break
    elif (IsDraw(board)):
        break
    else:
        comp_turn(board)

print('thank you playing')
print('Hamza')

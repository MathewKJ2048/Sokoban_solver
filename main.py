from game import *

sol = ['a', 'a', 'w', 'w', 'd', 'd', 'w', 'w', 's', 's', 'a', 'w', 'a', 's', 's', 's', 'd', 'd', 'w', 'w', 'w', 's', 's', 's', 'd', 'd', 'w', 'a', 's', 'a', 'w', 's', 'a', 'a', 'w', 'w', 'w', 'd', 'd', 's', 'w', 'd', 's', 'w', 'a', 's', 'a', 'w', 'a', 's', 's', 's', 'd', 'd', 'w', 'w', 's', 's', 'd', 'd', 'w', 'a', 'w', 'w', 'a', 's', 'a', 'w', 'w', 's', 's', 'a', 's', 's', 'd', 'd', 'w', 'w', 's', 's', 'a', 'a', 'w', 'w', 'w', 'd', 'd', 's', 's', 's']


match = {
    "a":"left",
    "s":"down",
    "w":"up",
    "d":"right"
}

board = init_board

print_board(board)

for i in sol:
    board = process(i,board)
    print_board(board)
    k = input("")

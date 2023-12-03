import copy

n = 8

SPACE = 0
WALL = 1
BOX = 2
CHAR = 3

def set_state(S,W):
    # W for walls, invariant in play
    board = []
    for i in range(n):
        board.append([SPACE]*n)
    for x in range(int(len(W)/2)):
        i = W[2*x]
        j = W[2*x+1]
        board[i][j] = WALL
    for x in range(int(len(S)/2)):
        i = S[2*x]
        j = S[2*x+1]
        board[i][j] = BOX
    pi = S[0]
    pj = S[1]
    board[pi][pj] = CHAR
    return board
        


def print_row(i,board):
    ro = ""
    for j in range(n):
        if board[i][j] == CHAR:
            ro = ro+" O"
        elif board[i][j] == SPACE:
            ro = ro+" ."
        elif board[i][j] == WALL:
            ro = ro+" X"
        elif board[i][j] == BOX:
            ro = ro+" #"
    print(ro)

def print_board(board):
    for i in range(n):
        print_row(i, board)

def next(i,j,inp):
    if inp == "w":
        return (i-1,j)
    elif inp == "s":
        return (i+1,j)
    elif inp == "a":
        return (i,j-1)
    elif inp == "d":
        return (i,j+1)

def process(inp,board):
    pi=None
    pj = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == CHAR:
                pi=i
                pj=j
    i_n,j_n = next(pi, pj, inp)
    if board[i_n][j_n] == SPACE:
        board[pi][pj] = SPACE
        board[i_n][j_n] = CHAR
    elif board[i_n][j_n] == BOX:
        i_s,j_s = next(i_n,j_n,inp)
        if board[i_s][j_s] == SPACE:
            board[pi][pj]=SPACE
            board[i_s][j_s]=BOX
            board[i_n][j_n] = CHAR
    return board

state_mem = []

move_int = {"w":"up","s":"down","a":"left","d":"right"}

def explore(board,fin):
    if board == fin:
        return []
    global state_mem
    h = copy.deepcopy(board)
    for x in state_mem:
        if x == board:
            return ["f"]
    state_mem.append(h)
    for move in ["w","s","a","d"]:
        board = copy.deepcopy(h)
        res = explore(process(move,board),fin)
        if res != ["f"]:
            return [move]+res
    print(len(state_mem))
    return ["f"]
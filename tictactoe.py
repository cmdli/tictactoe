import random

EMPTY = 0
X = 1
TIE = 2
O = 3

def other(player):
    if player == X:
        return O
    else:
        return X

def successors(board, player):
    succ = []
    for i,cell in enumerate(board):
        if cell == EMPTY:
            new_board = list(board)
            new_board[i] = player
            succ.append((i,new_board))
    return succ

def start():
    return [EMPTY for i in range(9)]

def goal(board, player):
    for x in range(3):
        m = True
        for y in range(3):
            m = m and board[x+y*3] == player
        if m:
            return True
    for y in range(3):
        m = True
        for x in range(3):
            m = m and board[x+y*3] == player
        if m:
            return True
    m = True
    for i in range(3):
        m = m and board[i+i*3] == player
    if m:
        return True
    m = True
    for i in range(3):
        m = m and board[i+(2-i)*3] == player
    if m:
        return True
    return False

def minimax(board, player):
    """print player
    print_board(board)
    print goal(board,player)"""
    if goal(board,player):
        return player
    if goal(board,other(player)):
        return other(player)
    if full(board):
        return TIE
        
    ss = successors(board,player)
    tie = False
    for a,succ in ss:
        best = minimax(succ, other(player))
        if best == TIE:
            tie = True
        if best == player:
            return player
    if tie:
        return TIE
    else:
        return other(player)

def print_board(board):
    for y in range(3):
        for x in range(3):
            if board[x+y*3] == X:
                print "X",
            elif board[x+y*3] == O:
                print "O",
            else:
                print ".",
            if not x == 2:
                print "|",
        print ""

def best_action(board, player):
    tie = -1
    ss = successors(board, player)
    if len(ss) == 0:
        return -1
    for action, succ in ss:
        best = minimax(succ, other(player))
        if tie == -1 and best == TIE:
            tie = action
        if best == player:
            return action
    if not tie == -1:
        return tie
    else:
        return random.choice(ss)[0]

def full(board):
    for i in board:
        if i == EMPTY:
            return False
    return True

def play():
    board = start()
    print "X or O?"
    print "> ",
    choice = raw_input().strip()
    while not (choice == "X" or choice == "O"):
        print "Invalid input ('X' or 'O' please!)"
        choice = raw_input().strip()        
    if choice == "X":
        player = X
    else:
        player = O
    turn = X
    while not goal(board, other(turn)) and not full(board):
        print_board(board)
        print ""
        if turn == player:
            print "Please enter your move ('X Y'): ",
            move_text = raw_input().strip().split(" ")
            while True:
                try:
                    move = map(int,move_text)
                    if move[0] in [0,1,2] and move[1] in [0,1,2]:
                        break
                except ValueError:
                    print "Please format the input like 'X Y'!"
            board[move[0] + move[1]*3] = player
        else:
            print "Computer move..."
            move = best_action(board, other(player))
            x = move%3
            y = move-x
            print "Placing on (%d,%d)..." % (x,y)
            board[move] = other(player)
        turn = other(turn)
    if goal(board,player):
        print "You won!"
    else:
        print "The computer is unfair! You lose."

if __name__ == "__main__":
    play()
        



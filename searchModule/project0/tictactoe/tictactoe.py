"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    symbol_count = 0

    for row in board:
        for element in row:
            if element != EMPTY:
                symbol_count += 1

    return X if symbol_count % 2 == 0 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for i,row in enumerate(board):
        for j,cell in enumerate(row):
            if cell == EMPTY:
                possible_moves.add((i,j))
    
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    if board[i][j] != EMPTY:
        raise Exception('Invalid action')
    current_turn = player(board)
    copy_board = copy.deepcopy(board)
    copy_board[i][j] = current_turn

    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    possible_wins = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)]
        ]
        
    for element in possible_wins:
        a,b,c = element
        if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] != EMPTY:
            return board[a[0]][a[1]]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != EMPTY:
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    value = winner(board)
    if value == EMPTY:
        return 0
    return 1 if value == X else -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)

    best_move = None
    
    if current_player == 'X':
        best_val = -math.inf
        for action in actions(board):
            move_val = min_value(result(board, action))
            if move_val > best_val:
                best_val = move_val
                best_move = action
    else:
        best_val = math.inf
        for action in actions(board):
            move_val = max_value(result(board, action))
            if move_val < best_val:
                best_val = move_val
                best_move = action
    
    return best_move
    

def max_value(board):
    if terminal(board):
        return utility(board)
    v = - math.inf
    for action in actions(board):
        v = max(v,min_value(result(board,action)))
    return v
    

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v,max_value(result(board,action)))
    return v

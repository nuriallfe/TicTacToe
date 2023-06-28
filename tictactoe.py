"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_count = 0
    o_count = 0
    for row in board:
        for column in row: 
            if column == X:
                x_count += 1
            elif column == O:
                o_count += 1
    if x_count > o_count : 
        return O
    else: 
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] is not EMPTY:
        raise Exception("Invalid action. Cell already occupied.")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #rows
    for row in board: 
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
        
    #columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]
        
    #diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    #mirar que quedin cells buides per continuar jugant
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        value, move = max_value(board)
    else:
        value, move = min_value(board)

    return move

def max_value(board):
    """
    Helper function for the minimax algorithm that returns the maximum utility value and corresponding move for X.
    """
    if terminal(board):
        return utility(board), None

    max_utility = float("-inf")
    best_move = None

    for action in actions(board):
        new_board = result(board, action)
        value, _ = min_value(new_board)
        if value > max_utility:
            max_utility = value
            best_move = action

    return max_utility, best_move


def min_value(board):
    """
    Helper function for the minimax algorithm that returns the minimum utility value and corresponding move for O.
    """
    if terminal(board):
        return utility(board), None

    min_utility = float("inf")
    best_move = None

    for action in actions(board):
        new_board = result(board, action)
        value, _ = max_value(new_board)
        if value < min_utility:
            min_utility = value
            best_move = action

    return min_utility, best_move

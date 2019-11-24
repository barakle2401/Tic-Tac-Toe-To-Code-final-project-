from __future__ import print_function
from human_player import HumanPlayer
from ai_player import AIPlayer
from game import Game


board = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]

game = Game(HumanPlayer('X'), AIPlayer('O'))


def _is_all_the_same(board, i1, i2, i3, val):
    if (board[i1[0]][i1[1]] == board[i2[0]][i2[1]] and
            board[i1[0]][i1[1]] == board[i3[0]][i3[1]] and
            board[i1[0]][i1[1]] == val
            ):
        return True
    else:
        return False


def get_winner(board):
    for player in ['X', 'O']:
        # rows
        if _is_all_the_same(board, (0, 0), (0, 1), (0, 2), player):
            return player
        if _is_all_the_same(board, (1, 0), (1, 1), (1, 2), player):
            return player
        if _is_all_the_same(board, (2, 0), (2, 1), (2, 2), player):
            return player

        # columns
        if _is_all_the_same(board, (0, 0), (1, 0), (2, 0), player):
            return player
        if _is_all_the_same(board, (0, 1), (1, 1), (2, 1), player):
            return player
        if _is_all_the_same(board, (0, 2), (1, 2), (2, 2), player):
            return player

        # diagonals
        if _is_all_the_same(board, (0, 0), (1, 1), (2, 2), player):
            return player
        if _is_all_the_same(board, (0, 2), (1, 1), (2, 0), player):
            return player


def game_over(board):
    if get_winner(board) is not None:
        return True

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.':
                return False

    return True


def is_valid(board, next_move):
    row, column = next_move
    try:
        return board[row][column] == '.'
    except IndexError:
        return False


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print("{:^3}".format(board[i][j]), end='')
        print("")


def play(board, next_move, game):
    row, column = next_move
    player_value = game.current_player_icon()
    board[row][column] = player_value

    game.next_turn()

    print_board(board)

#################
#
# 1. AI player
# 2. GUI
# 3. Score


if __name__ == '__main__':
    while not game_over(board):
        next_move = game.current_player().get_move()
        if is_valid(board, next_move):
            play(board, next_move, game)

    winner = get_winner(board)

    if winner == "X":
        print("Yay! X won")
    elif winner == "O":
        print("Yay! O won")
    else:
        print("game over...")

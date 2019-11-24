from pc_player import PcPlayer
from game import Game
from human_player import HumanPlayer
game_board = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]

game = Game(HumanPlayer('X'), PcPlayer('O'))




def game_over(game_board):
    if get_winner(game_board) is not None:
        return True
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == '.':
                return False
    return True


def all_equal(game_board, i1, i2, i3, val):
    if (game_board[i1[0]][i1[1]] == game_board[i2[0]][i2[1]] and
        game_board[i1[0]][i1[1]] == game_board[i3[0]][i3[1]] and
        game_board[i1[0]][i1[1]] == val
        ):
        return True
    else:
        return False


def get_winner(game_board):
    for player in ['X', 'O']:
         # rows
        if all_equal(game_board, (0, 0), (0, 1), (0, 2), player):
            return player
        if all_equal(game_board, (1, 0), (1, 1), (1, 2), player):
            return player
        if all_equal(game_board, (2, 0), (2, 1), (2, 2), player):
            return player

        # columns
        if all_equal(game_board, (0, 0), (1, 0), (2, 0), player):
            return player
        if all_equal(game_board, (0, 1), (1, 1), (2, 1), player):
            return player
        if all_equal(game_board, (0, 2), (1, 2), (2, 2), player):
            return player

        # diagonals
        if all_equal(game_board, (0, 0), (1, 1), (2, 2), player):
            return player
        if all_equal(game_board, (0, 2), (1, 1), (2, 0), player):
            return player


def print_board(game_board):

    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            print("{:^4}".format(game_board[i][j]), end='')
        print("")
    print('*'*20)


def get_next_player(current_player):
    if current_player == 'X':
        return 'O'
    else:
        return 'X'


def play(game_board, player_move, game):
    row, column = player_move

    game_board[row][column] = game.current_player_icon()
    game.next_turn()
    print_board(game_board)


def is_valid(board, player_move):
    row, column = player_move
    try:
        return game_board[row][column] == '.'
    except IndexError:
        return False


if __name__ == "__main__":

    while not game_over(game_board):

        player_move = game.current_player().get_move()
        if is_valid(game_board, player_move):
            play(game_board, player_move, game)

    winner = get_winner(game_board)
    if winner == 'X':
        print("X has won")
    elif winner == 'O':
        print("O has won")
    else:
        print("Game Over")

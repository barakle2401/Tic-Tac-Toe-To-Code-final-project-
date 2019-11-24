
class HumanPlayer:

    def __init__(self, value):
        self.value = value

    def get_move(self):
        print("Hello {}, please type your move (row, col)".format(self.value))
        text = input()

        row, column = text.split(', ')

        return (int(row), int(column))

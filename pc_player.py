import random


class PcPlayer:

    def __init__(self, value):
        self.value = value

    def get_move(self):

        c = random.randint(0, 2)
        r = random.randint(0, 2)
        return(r, c)

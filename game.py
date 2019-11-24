class Game:
    def __init__(self, p1, p2):
        self._players = [p1, p2]
        self._current_player = 0

    def next_turn(self):
        self._current_player = (self._current_player + 1) % 2

    def current_player(self):
        return self._players[self._current_player]

    def current_player_icon(self):
        return self.current_player().value

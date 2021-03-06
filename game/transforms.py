import copy


class Board:
    def __init__(self, data):
        self.data = copy.deepcopy(data)

    def get_rows(self):
        return [
            Line(self, [0, 1, 2]),
            Line(self, [3, 4, 5]),
            Line(self, [6, 7, 8]),
        ]

    def get_columns(self):
        return [
            Line(self, [0, 3, 6]),
            Line(self, [1, 4, 7]),
            Line(self, [2, 5, 8]),
        ]

    def get_diagonals(self):
        return [
            Line(self, [0, 4, 8]),
            Line(self, [2, 4, 6]),
        ]

    def get_lines(self):
        return [] + self.get_rows() + self.get_columns() + self.get_diagonals()

    def played_moves_count(self):
        return 9 - self.data.count(' ')

    def get_winning_side(self):
        for line in self.get_lines():
            if line.get_winner() is not None:
                return line.get_winner()
        return None

    def is_game_over(self):
        if self.get_winning_side() is not None:
            return True
        if all(r.is_filled() for r in self.get_rows()):
            return True
        return False


class Line:
    def __init__(self, game, positions):
        self.positions = copy.deepcopy(positions)
        self.data = []
        for position in positions:
            self.data.append(game.data[position])

    def get_data(self):
        return self.data

    def get_positions(self):
        return self.positions

    def get_winner(self):
        if all(d == 'x' for d in self.data):
            return 'x'
        elif all(d == 'o' for d in self.data):
            return 'o'
        else:
            return None

    def is_filled(self):
        return all(d != ' ' for d in self.data)

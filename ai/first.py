import random

from ai.ai import Ai
from game.transients import Board


class First(Ai):
    def get_name(self):
        return '1st Ai'

    def play(self, board: Board, side):
        for row in board.get_rows():
            for i in range(3):
                if row.data[i] == ' ':
                    return row.positions[i]
        return None

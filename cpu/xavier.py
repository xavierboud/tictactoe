from cpu.cpu import Cpu
from game.transforms import Board
from .services import find_winning_position


class Xavier(Cpu):
    def name(self):
        return 'Xavier''s AI 1.0'

    def play(self, board: Board, player_side, opposing_side):

        winning_position = find_winning_position(board, player_side)
        if winning_position is not None:
            return winning_position

        losing_position = find_winning_position(board, opposing_side)
        if losing_position is not None:
            return losing_position

        # board is empty
        if board.played_moves_count() == 0:
            return 0

        if board.played_moves_count() == 2:
            if board.data[8] == ' ':
                return 8
            else:
                return 6

        if board.played_moves_count() == 4:
            if board.data[0] == player_side and board.data[6] == player_side :
                return 2
            else:
                raise RuntimeError("Not reacheable")

        if board.played_moves_count() == 1:
            if board.data[4] == opposing_side:
                return 8
            else:
                return 4
        if board.played_moves_count() == 3:
            return 5

        return 5

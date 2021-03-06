from game.transforms import Board
from abc import ABCMeta, abstractmethod


class Cpu:
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def name(self): raise NotImplementedError

    @abstractmethod
    def play(self, board: Board, player_side, opposing_side): raise NotImplementedError

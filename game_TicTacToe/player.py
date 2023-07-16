
from abc import abstractmethod
from board import Board


class Player:
    """
    The Player class has properties:
        avatar --- type of str
        board --- type of Board class
    
    """
    def __init__(self, avarta:str, board: Board) -> None:
        self.avatar = avarta
        self.board = board

    @abstractmethod
    def next_move(self):
        pass





if __name__ == "__main__":
    board = Board()


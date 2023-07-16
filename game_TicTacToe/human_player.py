# from abc import abstractmethod
from board import Board

from player import Player


class HumanPlayer(Player):

    """
    HumanPlayer class is a child from Player class.
    Has self properties:
        avatar: type of str
        board: type of Board class
    and a method:
        next_move
    """

    def next_move(self):
        """
        Provides the correct choice of Human player's next-move, 
        updates the status of board and print new status.

        Args:
            self: self properties of HumanPlayer class
        
        """

        while True:

            move = input("Enter your move ---")

            if move in ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]:

                i = ord(move[0]) - 97
                j = int(move[1]) - 1

                if (i, j) not in self.board.get_free_moves():
                    print("This move has alrady daone.\n")
                    continue
                else:
                    move = (i, j)
                    self.board.set_board(self.avatar, move)
                    break
            else:
                print("Your choice is incorrect!!!\n")
                continue


if __name__ == "__main__":
    board = Board()
    human = HumanPlayer("X", board)
    human.next_move()
    human.next_move()

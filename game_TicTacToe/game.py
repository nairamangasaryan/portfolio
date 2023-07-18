
import random
from board import Board
from player import Player
from human_player import HumanPlayer
from computer_player import ComputerPlayer


class Game:

    """
    This Game class has the properties:
        board: type of Board class
        human: type of HumanPlayer class with self properties avatar = "X" and board
        computer: type of ComputerPlayer class with self properties avatar = "O" and board
    and methods:
        win_or_not: as an argument takes self properties and char("X" or "O"), 
            this methode check, if anyone of players win or not
        game: as an argument takes self properties
            this methode ensures the correct flow of the game
    """
    def __init__(self) -> None:
        self.board = Board()
        self.human = HumanPlayer("X", self.board)
        self.computer = ComputerPlayer("O", self.board)

    def win_or_not(self, char:str) -> bool:

        """
        Check, if anyone of players win or not

        Args:
            self: self properties of Gamea class
            char: str type, is equal to player's avatar: "X" or "O"
        Returns:
            bool: True if there are three "X" or "O" in row, column or dioganal and False otherwise
        """

        def result(l: list)-> bool:
            """
            Check the presence of three "X" or "O" in a row, column or diagonal

            Args:
                l (list): this list is a row, column or diagonal of the board

            Returns:
                bool: True if there are three "X" or "O" in l and False otherwise
            """

            if l.count(char) == 3:
                print(f"The '{char}' player WINS!!!")
                return True
            else:
                return False

        my_board = self.board.board

        diag1 = [my_board[0][0], my_board[1][1], my_board[2][2]]
        diag2 = [my_board[2][0], my_board[1][1], my_board[0][2]]

        for lst in [diag1, diag2]:

            if result(lst):
                return True

        for i in range(3):
            if result(my_board[i]):
                return True
            if result([my_board[0][i], my_board[1][i], my_board[2][i]]):
                return True

        return False

    def game(self):

        """
        Ensures the correct flow of the game.
        Args:
            self: self properties of Game class
        Returns:
            print name of winner or "Draw" if anyone of players dosen't win
            
        """
        self.board.print_board()

        while True:
            self.human.next_move()
            if Game.win_or_not(self, char=self.human.avatar):
                break

            self.computer.next_move()
            if Game.win_or_not(self, char=self.computer.avatar):
                break

            if len(self.board.get_free_moves()) == 0:
                print("Draw!!!")
                break

        print("Geme over!!!")


if __name__ == "__main__":
    tic_tac_toe = Game()
    tic_tac_toe.game()

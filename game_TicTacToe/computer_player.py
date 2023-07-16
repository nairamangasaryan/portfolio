
import random

from board import Board

from player import Player


class ComputerPlayer(Player):

    """
    ComputerPlayer class is a child from Player class.
    Has self properties:
        avatar: type of str
        board: type of Board class
    and a method:
        next_move
    """

    def next_move(self):
        """
        Provides the correct choice of Computer player's next-move, 
        updates the status of board and print new status.

        """

        def logic_for_list(l: list, char):

            """
            Cheack if there are two "X" or "O" in the list
            Args:
                l: list
                char: "X" or "O"
            Returns:
                int: the index of "-" in the list if it is exist
                     and None, if doesn't exist
            """

            if l.count(f"{char}") == 2:
                if "-" in l:
                    return l.index("-")
            return None


        moves_for_win = []
        moves_for_notlose = []
        my_board = self.board.board

        diag1 = [my_board[0][0], my_board[1][1], my_board[2][2]]
        diag2 = [my_board[2][0], my_board[1][1], my_board[0][2]]

        ### --- Check the existance of 2 "X" or "O" in the diaganals
        for char in ["X", "O"]:

            index1 = logic_for_list(diag1, char)
            if index1 != None:

                if char == "O":
                    moves_for_win.append((index1, index1))
                else:
                    moves_for_notlose.append((index1, index1))

        
            index2 = logic_for_list(diag2, char)
            if index2 != None:

                if char == "O":
                    moves_for_win.append((2-index2, index2))
                else:
                    moves_for_notlose.append((2-index2, index2))

        ### --- Check the existance of 2 "X" or "O" in the rows and columns
        for i in range(3):

            for char in ["X", "O"]:
                index3 = logic_for_list(my_board[i], char)
                if index3 != None:

                    if char == "O":
                        moves_for_win.append((i, index3))
                    else:
                        moves_for_notlose.append((i, index3))

                index4 = logic_for_list([my_board[0][i], my_board[1][i], my_board[2][i]], char)
                if index4 != None:

                    if char == "O":
                        moves_for_win.append((index4, i))
                    else:
                        moves_for_notlose.append((index4, i))

        ### --- Choose the wining move from moves_for_win if it isn't empty,
        ### --- otherwise choose the move from moves_for_notlose if it isn't empty,
        ### --- otherwise choose random move from available moves
        if moves_for_win != []:
            o_move = moves_for_win[0]
        elif moves_for_notlose != []:
            o_move = moves_for_notlose[0]
        else:
            o_move = random.choice(self.board.get_free_moves())

        self.board.set_board(self.avatar, o_move)


if __name__ == "__main__":
    board = Board()

    comp = ComputerPlayer("O", board)
    comp.next_move()
    comp.next_move()
    comp.next_move()

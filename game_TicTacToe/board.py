

class Board:

    """
    Board class has property board
    and methods: print_board, set_board, get_free_moves
    """

    def __init__(self) -> None:
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def print_board(self):
        """
        Print the corrent statuse of board.

        Args:
            self: self properties of Board class
        """
        print()
        print("\t1\t2\t3")
        k = 0
        for i in ['a', 'b', 'c']:
            print(f"\n{i}", end='\t')
            for j in range(3):
                print(self.board[k][j], end='\t')
            print()
            k += 1
        print()
        print()

    def set_board(self, player: str, move: tuple):
        """
        Update the new status of board after next move of player

        Args:
            player (str): "X" for human player, and "O" for computer player
            move (tuple): next move of player
        """
        i, j = move
        self.board[i][j] = player
        Board.print_board(self)

    def get_free_moves(self):
        """
        Check and return the list of available moves

        Returns:
            list: list of available moves
        """

        free_moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "-":
                    free_moves.append((i, j))

        return free_moves


if __name__ == "__main__":
    b = Board()
    b.print_board()
    b.set_board("x", (1, 1))
    print(b.get_free_moves())

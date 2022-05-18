class Board:
    """Represents one board to a Tic-Tac-Toe game."""

    def __init__(self):
        """Initializes a new board.
        A board is a 2-D array where each sub-array represents a row"""
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def __str__(self):
        """Prints the board."""
        bottom_border = f"-{'-+' * 3}\n"
        row_1 = f"|{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}|\n"
        row_2 = f"|{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}|\n"
        row_3 = f"|{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}|\n"
        return f"{row_1}{bottom_border}{row_2}{bottom_border}{row_3}{bottom_border}"

    def is_full(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def _is_valid_move(self, row, column):
        return self.board[row][column] == " "

    def change_board(self, row, column, current_player):
        """Receive a position and if the player is 'X' or 'O'.
        Checks if the position is valid, modifies the board and returns the modified board.
        Returns None if the move is not valid."""
        if self._is_valid_move(row, column):
            self.board[row][column] = current_player
            return self.board
        return None

    def is_winner(self, player):
        """Returns True if the player won and False otherwise."""
        # check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
        # check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False


class Player:
    """Represents one player."""

    def __init__(self, piece):
        """Initializes a player with type 'X' or 'O'."""
        self.piece = piece

    def __str__(self):
        return f"Player {self.piece}"


class Game:
    """Represents a Tic-Tac-Toe game.
    The game defines player 1 always playing with 'X'."""

    def __init__(self):
        """Initialize 2 Players and one Board."""
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.board = Board()

    def print_board(self):
        """Prints the board."""
        print(self.board)

    def change_turn(self, player):
        """Changes the player's turn.
        Takes in a player and returns the other."""
        return self.player2 if player == self.player1 else self.player1

    def won_game(self, player):
        """Returns True if the player won the game, False otherwise."""
        return self.board.is_winner(player)

    def _invalid_move(self):
        print("Position not valid. Please, try again: ")
        return False

    def modify_board(self, row, column, current_player):
        """Receives position and player type ('X' or 'O').
        Returns modified board if position was valid.
        Asks to player try a different position otherwise."""
        if not row.isnumeric() and column.isnumeric():
            return self._invalid_move()
        row_num = int(row)
        col_num = int(column)
        if row_num < 0 or row_num > 2 or col_num < 0 or col_num > 2:
            return self._invalid_move()
        if self.board.change_board(row_num, col_num, current_player):
            return self.board.change_board(row_num, col_num, current_player)
        else:
            return self._invalid_move()


def play():
    game = Game()
    player = game.player1
    while not game.board.is_full():
        game.print_board()
        row = input(f"{player}, what row would you like to put your piece on? ")
        column = input(f"{player}, what column would you like to put your piece on? ")

        valid_move = game.modify_board(row, column, player.piece)
        if game.won_game(player.piece):
            print(f"{player} is the Winner!")
            game.print_board()
            break
        elif valid_move is not False:
            player = game.change_turn(player)
    else:
        print("Game over! It's a tie!")


if __name__ == "__main__":
    play()

from random import choice

class TicTacToe:

    def __init__(self):
        self.board = []
        self.possible_squares = [square for square in range(9)]
        self.available_squares = [square for square in range(9)]

    def create_board(self):
        """This Function will Create The Board."""
        square = 0
        col = 3
        for row in range(3):
            row = []
            for squares in range(3):
                while square < col:
                    row.append(square)
                    square += 1
            col += 3
            self.board.append(row)

    def print_board(self):
        """This Function will print the board."""

        for row in self.board:
            for squares in row:
                print('|',squares, '|',end='')
            print()

    def get_human_move(self):
        """This function will Get Player square Number."""
        while True:
            try: square = int(input("Enter Square Number: "))
            except ValueError: print("Invalid Input!")
            else:
                if square not in self.possible_squares: 
                    print("Invalid Square number! Try again.")
                else:
                    if square in self.available_squares: 
                        self.available_squares.remove(square) 
                        break
                    else: print("That Slot is already Occupied!")
        return square

    def get_computer_move(self):
        """This function will get Computer square number."""
        square = choice(self.available_squares)
        self.available_squares.remove(square)
        return square

    def fix_spot(self, move, symbol):
        """Fix spots on board."""
        square = move % 3
        if move < 3: self.board[0][square] = symbol
        elif move < 6: self.board[1][square] = symbol
        elif move < 9: self.board[2][square] = symbol

    def is_winner(self, symbol):
        """This will Decide the winner."""
        n = len(self.board)
        win = None
        # Check rows.
        for row in range(n):
            win = True
            for square in range(n):
                if self.board[row][square] != symbol:
                    win = False
            if win:
                return win
        # Check columns.
        for row in range(n):
            win = True
            for square in range(n):
                if self.board[square][row] != symbol:
                    win = False
            if win:
                return win
        # Check Diagnoals
        win = True
        for diagnol1 in range(n):
            if self.board[diagnol1][diagnol1] != symbol:
                win = False
        if win:
            return win

        win = True
        for diagnol2 in range(n):
            if self.board[diagnol2][n - 1 - diagnol2] != symbol:
                win = False
        if win:
            return win


def play_game():
    """Start the Game."""
    game = TicTacToe()
    game.create_board()
    symbol = 'X'

    while len(game.available_squares) != 0:
        if symbol == 'X':
            square = game.get_human_move()
        else:
            square = game.get_computer_move()

        game.fix_spot(square, symbol)
        print("\n{0} makes a move to square {1}".format(symbol, square))
        game.print_board()
        print()
        if game.is_winner(symbol):
            print("{0} Won !!".format(symbol))
            break
        
        if symbol == 'X': 
            symbol = 'O'
        else: symbol = 'X'
    
play_game()

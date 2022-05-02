from random import randint

class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):

        """Create a board of 3 by 3 (3x3)"""
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def player_cords(self):
        """Get Player's coordinates."""
        while True:
            row = int(input("Enter Row Number: "))
            if row >= 1 and row <= 3:
                break
            else:
                print("Invalid Input!\nSelect from 1 to 3.\n")
        
        while True:
            col = int(input("Enter Column Number: "))
            if col >= 1 and col <= 3:
                break
            else:
                print("Invalid Input!\nSelect from 1 to 3.\n")

        coords = (row, col)
        return list(coords)

    def computer_cords(self):
        """Generate computers Random coordinates."""
        row , col = randint(1, 3), randint(1, 3)
        coords = (row, col)
        return list(coords)

    def random_turn(self):
        num = randint(1,2)
        return num

    def is_taken(self, row, col):
        """Check if the slot in board is taken or not."""
        if self.board[row][col] == '-':
            return False
        return True

    def print_board(self):
        """This function will print the board."""
        for row in self.board:
            for col in row:
                print(col, end=" ")
            print()

    def start_game(self):
        """Let the Game Begins."""
        self.create_board()
        p_symbol = 'X' if self.random_turn() == 1 else 'O'
        c_symbol = 'X' if self.random_turn() == 0 else 'O'
        used_cords = []
        while True:
            while True:
                player = self.player_cords()
                if self.is_taken(player[0] - 1, player[1] - 1):
                    print("That slot is already occupied, Select another slot.")
                else:
                    self.board[player[0] - 1][player[1] - 1] = p_symbol
                    break

            while True:
                computer = self.computer_cords()
                if self.is_taken(computer[0] - 1, computer[1] - 1) == False:
                    self.board[computer[0] - 1][computer[1] - 1] = c_symbol
                    break
            self.print_board()


b = TicTacToe()
# b.create_board()
# b.print_board()
b.start_game()
input()

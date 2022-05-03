from random import randint, choice

class TicTacToe:

    def __init__(self):
        self.board = [
                      ['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-'],
                    ]

    def print_board(self):
        """This function will print the board."""
        for row in self.board:
            for col in row:
                print(f"{col}", end="  ")
            print()

    def player_cords(self):
        """Get Player's coordinates."""
        while True:
            row = int(input("Enter Row Number: "))
            if row >= 1 and row <= 3: break
            else: print("Invalid Input!\nSelect from 1 to 3.\n")
        
        while True:
            col = int(input("Enter Column Number: "))
            if col >= 1 and col <= 3: break
            else: print("Invalid Input!\nSelect from 1 to 3.\n")

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

    def is_board_full(self, b):
        for row in b:
            for item in row:
                if item == '-':
                    return False
        return True

    def start_game(self):
        """Let the game Begin's."""
        possible_cords = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
        p_symbol = 'X' if self.random_turn() == 1 else 'O'
        c_symbol = 'O' if p_symbol == 'X' else 'X'
        board = self.board

        while self.is_board_full(board) == False:
            print()
            self.print_board()
            print()
            player = self.player_cords()
            if self.is_taken(player[0] - 1, player[1] - 1):
                print("That slot is already occupied, Try again!")
            else:
                possible_cords.remove(player)
                board[player[0] - 1][player[1] - 1] = p_symbol
                computer = choice(possible_cords)
                possible_cords.remove(computer)
                board[computer[0] - 1][computer[1] - 1] = c_symbol


b = TicTacToe()
b.start_game()

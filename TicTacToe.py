from random import randint


class TicTacToe:

    def __init__(self):
        self.board = [
                      ['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-'],
                    ]
        self.valid_inputs = [1, 2, 3]
        self.possible_cords = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]


    def print_board(self):
        """This Function will Print the board."""
        for row in self.board:
            for slot in row:
                print(slot, end="  ")
            print()


    def player_cords(self):
        """
        Get Player's Coordinates in the form of row and column.
        """
        coords = []
        while True:
            try: row = int(input("Enter Row Number: "))
            except ValueError: print("Invalid Input!")
            else: 
                if row not in self.valid_inputs: print("Select from 1 to 3.")
                else: 
                    coords.append(row)
                    break
        while True:
            try: col = int(input("Enter Column Number: "))
            except ValueError: print("Invalid Input!")
            else: 
                if col not in self.valid_inputs: print("Select from 1 to 3.")
                else: 
                    coords.append(col)
                    break
        return coords


    def random_number(self):
        """
        This Function will generate random number,
        from 1 to 2, to use for symbol.
        """
        number = randint(1, 2)
        return number


    def swap_player_turn(self, symbol):
        """This function will Swap the Player's Turn."""
        if symbol == 'X':
            symbol = 'O'
        elif symbol == 'O':
            symbol = 'X'
        return symbol


    def is_winner(self, player):
        """This Functio will Decide the winner of TicTacToe."""
        n = len(self.board)
        win = None
        # Check Rows.
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
            if win:
                return win
        # Check Columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
            if win:
                return win
        # Check Diagnals
        win = True
        for i in range (n):
            if self.board != player:
                win = False
        if win:
            return win
        
        for i in range(n):
            if self.board[n - 1 - i] != player:
                win = False
        if win:
            return win
        return False
        

    def start_game(self):
        """Let the game begin's."""
        self.print_board()
        print()
        symbol = 'X' if self.random_number == 1 else 'O'

        while True:
            # If board's Full then it's a Draw(exit loop)
            if len(self.possible_cords) == 0:
                print("It's a Draw.")
                break
            print("Player '{0}' Turn.".format(symbol))
            player = self.player_cords()
            # If Slot is Occupied.
            if player not in self.possible_cords:
                print("That Slot is already Occupied, Select Another Slot.\n")
            else:
                # If slot is not Occupied remove it from possible coords.
                self.possible_cords.remove(player)
                # Draw symbol on board.
                self.board[player[0] - 1][player[1] - 1] = symbol
                # Print board.
                print()
                self.print_board()
                print()
                # If Player 'O' or 'X' wins
                # Print Message and exit loop.
                if self.is_winner(symbol):
                    print('Player {0} won!'.format(symbol))
                    break
                # Swap Player's Turn.
                symbol = self.swap_player_turn(symbol)
            

game = TicTacToe()
game.start_game()

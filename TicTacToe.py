from random import randint, choice

class TicTacToe:

    def __init__(self):
        self.board = [
                      ['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-'],
                    ]
        self.possible_cords = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]


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
        """
        Function to randomly choose symbol for player and computer.
        """
        num = randint(1,2)
        return num


    def is_winner(self, player):
        """Decide the winner."""
        n = len(self.board)
        win = False
        # Check Rows
        for row in range(n):
            win = True
            for col in range(n):
                if self.board[row][col] != player:
                    win = False
                    break
            if win:
                return win
        
        # Check Columns     
        for row in range(n):
            win = True      
            for col in range(n):
                if self.board[col][row] != player:
                    win = False
                    break
            if win:
                return win

        # Check Diagnals    
        win = True           
        for i in range(n):  
            if self.board[i][i] != player:
                win = False
        if win:
            return win 

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
        if win:
            return win
        return False


    def start_game(self):
        """Let the game Begin's."""
        p_symbol = 'X' if self.random_turn() == 1 else 'O'
        c_symbol = 'O' if p_symbol == 'X' else 'X'

        while True:
            # Get Player's coordinates
            player = self.player_cords()
            if player not in self.possible_cords:
                print("That slot is already occupied, Try again!\n")
            else:
                self.possible_cords.remove(player)
                # Update Player's coordinates on board.
                self.board[player[0] - 1][player[1] - 1] = p_symbol
                # Get Computer's coordinates.
                computer = choice(self.possible_cords)
                self.possible_cords.remove(computer)
                # Update Computer's coordinates on board.
                self.board[computer[0] - 1][computer[1] - 1] = c_symbol
                print()
                # Print board after Player's and Computer's Turn.
                self.print_board()
                print()
                # If board is Full End the game.
                if len(self.possible_cords) == 0:
                    print("It's a Draw!")
                    break

            # Check Winner
            if self.is_winner(c_symbol):
                print("Computer won! Better luck next time.")
                break
            elif self.is_winner(p_symbol):
                print("You outsmarted computer, You won!")
                break

game = TicTacToe()
game.start_game()

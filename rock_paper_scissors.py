from random import choice


def game_rules():
    """Show game rules."""
    strng = "Welcome to Rock, Paper or Scissors!\n"
    strng += "Game Rules:\n"
    strng += "--> Rock wins against Scisscors\n"
    strng += "--> Paper wins against Rock\n"
    strng += "--> Scissors wins Paper\n\n"
    strng += "Who ever wins first 3 rounds, wins this game!\nGood luck."
    return strng


def player_choice():
    """Get a valid player's choice."""
    choices = ['R', 'P', 'S']

    while True:
        player_choice = input('\n"R" for Rock, "P" for Paper, "S" for Scissors. ')
        if player_choice.upper() in choices:
            break
        elif player_choice.upper() not in choices:  # ask user again if choice is other than
            print("Invalid choice! Try again.")     # 'R', 'P' or 'S'
    return player_choice.upper()


def computer_choice():
    """Get computer's random choice."""
    choices = ['R', 'P', 'S']
    comp_choice = choice(choices)
    return comp_choice


def is_win(player, computer):
    """Decide the winner of each round."""
    if player == 'P' and computer == 'R':
        return True
    elif player == 'R' and computer == 'S':
        return True
    elif player == 'S' and computer == 'P':
        return True
    return False

def play_game():
    """Start the game."""
    player_score = 0
    rou = 5

    # R > S, P > R, S > P 
    while rou != 0:
        player = player_choice()
        computer = computer_choice()
        print(computer)
        
        if player == computer:
            print("It's a Tie!")        # If it's a Tie, then round doesn't count.
        elif is_win(player, computer):
            rou -= 1
            player_score += 1
            print("You won this round!")
        else:
            rou -= 1
            print("Computer won this round!")

    return player_score


def declare_winner():
    """Declare the winner of the game."""
    score = play_game()
    if score >= 3:
        print("\nCongrats, You won {0} out of 5 rounds.\nYou win".format(score))
    else:
        print("\nComputer won {0} out of 5 rounds.\nBetter luck next time.".format(5 - score))


print(game_rules())
declare_winner()
input("\n\nPress Enter to quit.")

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


def play_game():
    """Start the game."""
    player_score = 0
    computer_score = 0
    rou = 5

    # R > S, P > R, S > P 
    while rou != 0:
        player = player_choice()
        computer = computer_choice()
        if player == computer:
            print("It's a Tie!")        # If it's a Tie, then round doesn't count.
        elif (player == 'R' and computer == 'S') or (player == 'P' and computer == 'R') \
            or (player == 'S' or computer == 'P'):
            print("You won this Round!\n")
            player_score += 1
            rou -= 1
        else:
            print("Computer won this Round!")
            computer_score += 1
            rou -= 1

    return player_score


print(game_rules())
print(play_game())
input()
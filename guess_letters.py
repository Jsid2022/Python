from random import choice
import string


words = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie']

def about_game():
    """Tell user about game."""
    strng = "Welcome to game: Guess Letter.\n"
    strng += "A random word will be generated when you enter the game.\n"
    strng += "For example the word is: 'CRICKET'.\n"
    strng += "--> Guess a letter, If that letter is in word,\n"
    strng += "    Then that letter will be displayed like this _R__KE_.\n"
    strng += "--> You have total 7 attempts to guess the letters of word correctly.\n\n"
    strng += "Good Luck!"
    print(strng)


def guess_letter():
    """Start the game."""
    word = choice(words).upper()  # Get a random word.
    letter_list = list(word)      # Make a list of words.(Original word)
    word_letters = set(word)      # Make a list of words.(That doesn't repeat)
    word_list = ['_' for letter in word]    # Make a list of words('_') equal to lenght of word.
    used_letters = set()          # Initialized empty list to store user input.(repeated input will not be stored.)
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        index = 0

        print("\nCurrent word: {0}".format(''.join(word_list)))
        guess = input("Guess a letter: ").upper()

        if guess not in string.ascii_uppercase:
            # If user's input is not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            print("Invalid Input!")
        elif guess in used_letters:
            # If user's input is in used_letters.
            print("You have already guessed that letter, Guess another letter.")
        elif guess not in used_letters:
            # if user's input is not in user_letters.
            used_letters.add(guess)
            if guess in word_letters:
                # If user's input is in word_letters
                word_letters.remove(guess)
            else: # else print.
                print("Your letter {0} is not in the word.".format(guess))
                lives -= 1

        # If user's input is in word_letter's then
        # Loop through each item in word_list
        # And replace it with user's input.
        while index < len(word_list):
            if letter_list[index] == guess:
                word_list[index] = guess
            index += 1

    if lives == 0:
        print("You died, sorry. The word was, {0}.".format(word))
    else:
        print('Congrats you guessed the correct word "{0}".'.format(word))


about_game()
guess_letter()
input('\n\nPress Enter to quit.')

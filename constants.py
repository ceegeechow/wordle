import argparse
import enum

# enum used to track the display color of characters
class guessState(enum.Enum):
    green = 1
    yellow = 2
    red = 3

# used to format output in color
class printColors:
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    endc = '\033[0m'

def check_range(arg):
    try:
        value = int(arg)
    except ValueError as err:
       raise argparse.ArgumentTypeError(str(err))

    if value < 3 or value > 10:
        raise argparse.ArgumentTypeError("must be between 3 and 10, inclusive")

    return value

def check_min(arg):
    try:
        value = int(arg)
    except ValueError as err:
       raise argparse.ArgumentTypeError(str(err))

    if value < 1:
        raise argparse.ArgumentTypeError("must be greater than 0")

    return value

def parseArguements():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rules", help="display rules", action="store_true")
    parser.add_argument("-l", "--length", type=check_range, default=5, help="number of letters in wordle, must be between 3 and 10 inclusive", required=False)
    parser.add_argument( "-mg", "--maxGuesses",type=check_min, default=6, help="maximum number of guesses, must be a positive integer", required=False)
    parser.add_argument("-hm", "--hardMode", help="any revealed hints must be used in subsequent guesses", action="store_true")
    return parser.parse_args()
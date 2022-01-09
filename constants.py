import enum

class guessState(enum.Enum):
    green = 1
    yellow = 2
    red = 3

class printColors:
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    endc = '\033[0m'
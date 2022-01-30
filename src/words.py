import utils
from datetime import datetime, timedelta
import enchant
from random_word import RandomWords
import re 

# used by guessProcessor to print color-coded alphabet to help user with guesses
class alphabet:
    def __init__(self):
        self.letters = "abcdefghijklmnopqrstuvwxyz"
        self.letterMap = {c: None for c in self.letters}

    def updateMap(self, c, state):
        self.letterMap[c] = state

    def get(self, c):
        return self.letterMap[c]

    def printOutput(self):
        outputString = ""
        for c in self.letters:
            if self.letterMap[c] == utils.guessState.green:
                outputString += utils.printColors.green + c + utils.printColors.endc
            elif self.letterMap[c] == utils.guessState.yellow:
                outputString += utils.printColors.yellow + c + utils.printColors.endc
            elif self.letterMap[c] == utils.guessState.red:
                outputString += utils.printColors.red + c + utils.printColors.endc
            else:
                outputString += c
        print(outputString)

class wordValidator:
    def __init__(self, language="en_US"):
        self.d = enchant.Dict(language)

    def validateWord(self, s, n):
        if s == None:
            return False
        if len(s) != n:
            return False
        if not re.fullmatch('[a-z]+', s):
            return False
        return self.d.check(s)

class wordGenerator:
    def __init__(self, n, t=30):
        self.wordLength = n
        self.randomWords = RandomWords()
        self.timeoutDuration = t
        self.validator = wordValidator()
    
    def generateWord(self):
        timeout = datetime.now() + timedelta(seconds=self.timeoutDuration)
        while datetime.now() < timeout:
            s = self.randomWords.get_random_word(hasDictionaryDef=True, minLength=self.wordLength, maxLength=self.wordLength)
            if self.validator.validateWord(s, self.wordLength):
                return s
        raise(utils.generatorTimeout)
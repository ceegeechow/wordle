import constants
import words

class guessProcessor:
    def __init__(self, wordle, hardMode):
        self.alpha = words.alphabet()
        self.wordle = wordle
        self.results = []
        self.hardMode = hardMode # TODO: implement hard mode

    def processGuess(self, guess):
        if len(self.wordle) != len(guess):
            sys.exit("len(word) != len(guess)")

        r = [None]*len(self.wordle)

        availableLetters = self.wordle
        
        for i in range(len(self.wordle)):
            if self.wordle[i] == guess[i]:
                r[i] = constants.guessState.green
                availableLetters = availableLetters.replace(self.wordle[i], "", 1)
                self.alpha.updateMap(self.wordle[i], constants.guessState.green)
        for i, val in enumerate(r):
            if val == None:
                if guess[i] in availableLetters:
                    r[i] = constants.guessState.yellow
                    availableLetters = availableLetters.replace(guess[i], "", 1)
                    if self.alpha.get(guess[i]) != constants.guessState.green:
                        self.alpha.updateMap(guess[i], constants.guessState.yellow)
                else:
                    r[i] = constants.guessState.red
                    if self.alpha.get(guess[i]) != constants.guessState.green and self.alpha.get(guess[i]) != constants.guessState.yellow:
                        self.alpha.updateMap(guess[i], constants.guessState.red)
        self.results.append(r)
        return r

    def outputResult(self, res, s):
        if len(res) != len(s):
            sys.exit("len(res) != len(s)")
        outputString = ""
        for i in range(len(s)):
            if res[i] == constants.guessState.green:
                outputString += constants.printColors.green
            elif res[i] == constants.guessState.yellow:
                outputString += constants.printColors.yellow
            else:
                outputString += constants.printColors.red
            outputString += s[i] + constants.printColors.endc
        print(outputString)

    def shareResults(self):
        #TODO
        print(self.results)
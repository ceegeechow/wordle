import utils
import words

class mismatchedLength(Exception):
    pass

class invalidHardMode(Exception):
    pass

class guessProcessor:
    def __init__(self, wordle, hardMode):
        self.alpha = words.alphabet()
        self.wordle = wordle
        self.results = []
        self.lastGuess = ""
        self.hardMode = hardMode

    # takes guess word and compares it to the wordle (target word)
    def processGuess(self, guess):
        if len(self.wordle) != len(guess):
            raise mismatchedLength()

        if self.hardMode and not self.checkPriorGuesses(guess):
            raise invalidHardMode()

        r = [None]*len(self.wordle)

        availableLetters = self.wordle
        
        for i in range(len(self.wordle)):
            if self.wordle[i] == guess[i]:
                r[i] = utils.guessState.green
                availableLetters = availableLetters.replace(self.wordle[i], "", 1)
                self.alpha.updateMap(self.wordle[i], utils.guessState.green)
        for i, val in enumerate(r):
            if val == None:
                if guess[i] in availableLetters:
                    r[i] = utils.guessState.yellow
                    availableLetters = availableLetters.replace(guess[i], "", 1)
                    if self.alpha.get(guess[i]) != utils.guessState.green:
                        self.alpha.updateMap(guess[i], utils.guessState.yellow)
                else:
                    r[i] = utils.guessState.red
                    if self.alpha.get(guess[i]) != utils.guessState.green and self.alpha.get(guess[i]) != utils.guessState.yellow:
                        self.alpha.updateMap(guess[i], utils.guessState.red)
        self.lastGuess = guess
        self.results.append(r)
        return r

    # in hard mode, the guess should include revealed letters
    def checkPriorGuesses(self, guess):
        if len(self.results) == 0 or self.lastGuess == "":
            return True
        lastResult = self.results[-1]
        if len(lastResult) != len(guess) or len(lastResult) != len(self.lastGuess):
            raise mismatchedLength()
        for i, c in enumerate(guess):
            if lastResult[i] == utils.guessState.green and guess[i] != self.lastGuess[i]:
                return False
            elif lastResult[i] == utils.guessState.yellow and self.lastGuess[i] not in guess:
                return False
        return True

    def outputResult(self, res, s):
        if len(res) != len(s):
            raise mismatchedLength()

        outputString = ""
        for i in range(len(s)):
            if res[i] == utils.guessState.green:
                outputString += utils.printColors.green
            elif res[i] == utils.guessState.yellow:
                outputString += utils.printColors.yellow
            else:
                outputString += utils.printColors.red
            outputString += s[i] + utils.printColors.endc
        print(outputString)

    def shareResults(self, guessNum, maxGuesses):
        print("Camille's Wordle " + str(guessNum) + "/" + str(maxGuesses))
        for r in self.results:
            self.outputResult(r, "ooooo")
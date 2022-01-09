import guesses
import words

class Wordle:
    def __init__(self, maxGuesses, length, hardMode):
        self.guessMap = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth", 6: "Sixth"}
        self.guessNum = 0
        self.maxGuesses = maxGuesses
        self.length = length
        self.validator = words.wordValidator()
        w = words.wordGenerator(self.length)
        self.wordle = w.generateWord()
        self.processor = guesses.guessProcessor(self.wordle, hardMode)

    def play(self):
        while self.guessNum < self.maxGuesses:
            self.guessNum += 1
            guess = input(self.guessMap[self.guessNum] + " guess: ")
            if not self.validator.validateWord(guess, self.length):
                print(guess + " is not a valid guess, try again")
                self.guessNum -= 1
                continue
            guessRes = self.processor.processGuess(guess)
            self.processor.outputResult(guessRes, guess)

            if guess == self.wordle:
                print("Congratulations! You got the wordle in", self.guessNum, "guesses!")
                share = input("Would you like to share your result (y/n)?")
                if share.lower() == "y":
                    self.processor.shareResults()
                return
            
            self.processor.alpha.printOutput()

        print("The wordle was " + self.wordle + ". Better luck next time!")

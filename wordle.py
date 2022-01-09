import guesses
import words

class Wordle:
    def __init__(self, maxGuesses, length, hardMode):
        # to format input statement
        self.guessMap = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth", 6: "Sixth"}
        self.guessNum = 0 # guess that the player is on
        self.maxGuesses = maxGuesses
        self.length = length # length of the wordle
        self.validator = words.wordValidator()
        w = words.wordGenerator(self.length)
        self.wordle = w.generateWord() # word player is trying to guess
        self.processor = guesses.guessProcessor(self.wordle, hardMode) # processes player guesses

    def play(self):
        while self.guessNum < self.maxGuesses:
            self.guessNum += 1
            # get guess from input
            guess = input(self.guessMap[self.guessNum] + " guess: ")
            # validate guess, if guess is invalid, decrement guess number and try again
            if not self.validator.validateWord(guess, self.length):
                print(guess + " is not a valid guess, try again")
                self.guessNum -= 1
                continue

            # process guess and output result
            try:
                guessRes = self.processor.processGuess(guess)
            except guesses.mismatchedLength:
                sys.exit("error processing guess: length of guess does not match length of wordle")
            
            try:
                self.processor.outputResult(guessRes, guess)
            except guesses.mismatchedLength:
                sys.exit("error printing output: length of guess does not match length of result")

            # if the player guesses the word, end the game
            if guess == self.wordle:
                print("Congratulations! You got the wordle in", self.guessNum, "guesses!")
                share = input("Would you like to share your result (y/n)?")
                if share.lower() == "y":
                    self.processor.shareResults()
                return
            
            # print color-coded alphabet to help player
            self.processor.alpha.printOutput()

        # out of guesses
        print("The wordle was " + self.wordle + ". Better luck next time!")

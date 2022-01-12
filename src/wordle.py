import guesses
import words
import sys

class Wordle:
    def __init__(self, maxGuesses, length, hardMode):
        self.guessNum = 0 # guess that the player is on
        self.maxGuesses = maxGuesses
        self.length = length # length of the wordle
        self.validator = words.wordValidator()
        w = words.wordGenerator(self.length)
        self.wordle = w.generateWord() # word player is trying to guess
        self.hardMode = hardMode
        self.processor = guesses.guessProcessor(self.wordle, self.hardMode) # processes player guesses

    def play(self):
        found = False
        while self.guessNum < self.maxGuesses:
            self.guessNum += 1
            # get guess from input
            guess = input("Guess #" + str(self.guessNum) + ": ")
            guess = guess.lower()
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
            except guesses.invalidHardMode:
                print("this guess does not use all of the previous hints (hard mode)")
                self.guessNum -= 1
                continue
            
            try:
                self.processor.outputResult(guessRes, guess)
            except guesses.mismatchedLength:
                sys.exit("error printing output: length of guess does not match length of result")

            # if the player guesses the word, end the game
            if guess == self.wordle:
                found = True
                print("Congratulations! You got the wordle in", self.guessNum, "guesses!")
                share = input("Would you like to share your result (y/n)?")
                if share.lower() == "y":
                    self.processor.shareResults(self.guessNum, self.maxGuesses)
                break
            # print color-coded alphabet to help player
            self.processor.alpha.printOutput()

        # out of guesses
        if not found:
            print("-"*(39+len(self.wordle)))
            print("The wordle was " + self.wordle + ". Better luck next time!")

        # play again?
        again = input("Play again (y/n)?")
        if again.lower() == "y":
            self.__init__(self.maxGuesses, self.length, self.hardMode)
            self.play()
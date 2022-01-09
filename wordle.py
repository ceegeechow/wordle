import argparse
import constants
import sys
import words

GUESS_MAP = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth", 6: "Sixth"}

def compareLetters(word, guess, a):
    if len(word) != len(guess):
        sys.exit("len(word) != len(guess)")
    letters = word
    r = [None]*len(word)
    
    for i in range(len(word)):
        if word[i] == guess[i]:
            r[i] = constants.guessState.green
            letters = letters.replace(word[i], "", 1)
            a.updateMap(word[i], constants.guessState.green)
    for i, val in enumerate(r):
        if val == None:
            if guess[i] in letters:
                r[i] = constants.guessState.yellow
                letters = letters.replace(guess[i], "", 1)
                if a.get(guess[i]) != constants.guessState.green:
                    a.updateMap(guess[i], constants.guessState.yellow)
            else:
                r[i] = constants.guessState.red
                if a.get(guess[i]) != constants.guessState.green and a.get(guess[i]) != constants.guessState.yellow:
                    a.updateMap(guess[i], constants.guessState.red)
    return r, a

def outputResult(res, s):
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
    return outputString

if __name__ == "__main__":
    #TODO: add hardmode
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, default=5, help="number of letters in wordle", required=False)
    parser.add_argument("--maxGuesses", type=int, default=6, help="maximum number of guesses", required=False)
    args = parser.parse_args()

    a = words.alphabet()
    w = words.wordGenerator(args.length)
    v = words.wordValidator()

    word = w.generateWord()
    if word == "":
        sys.exit("error generating valid word")

    guessNum = 0
    sharableResults = []
    while guessNum < args.maxGuesses:
        guessNum += 1
        guess = input(GUESS_MAP[guessNum] + " guess: ")
        if not v.validateWord(guess, args.length):
            print(guess + " is not a valid guess, try again")
            guessNum -= 1
            continue
        guessRes, a = compareLetters(word, guess, a)
        sharableResults.append(guessRes)
        print(outputResult(guessRes, guess))

        if guess == word:
            print("Congratulations! You got the wordle in", guessNum, "guesses!")
            share = input("Would you like to share your result (y/n)?")
            if share.lower() == "y":
                print(sharableResults) #TODO: output emojis?
            sys.exit()
        
        a.printOutput()

    print("The wordle was " + word + ". Better luck next time!")

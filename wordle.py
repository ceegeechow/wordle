from random_word import RandomWords
import re
import enum

guessMap = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth", 6: "Sixth"}

class GuessState(enum.Enum):
    green = 1
    yellow = 2
    gray = 3

class printColors:
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    endc = '\033[0m'

def generateWord(n):
    r = RandomWords()
    word = r.get_random_word(hasDictionaryDef=True, minCorpusCount=20, minDictionaryCount=10, minLength=n, maxLength=n)
    return word

def getValidWord(n):
    for _ in range(5):
        s = generateWord(n)
        if re.fullmatch('[a-z]{5}', s):
            return s

def validateGuess(s): #TODO
    if len(s) != 5:
        return False
    return True

def compareLetters(word, guess):
    letters = word
    r = [None]*len(word)
    for i in range(len(word)):
        if word[i] == guess[i]:
            r[i] = GuessState.green
            letters = letters.replace(word[i], "", 1)
    for i, val in enumerate(r):
        if val == None:
            if guess[i] in letters:
                r[i] = GuessState.yellow
                letters = letters.replace(guess[i], "", 1)
            else:
                r[i] = GuessState.gray
    return r

def outputResult(res, guess):
    outputString = ""
    for i in range(len(guess)):
        if res[i] == GuessState.green:
            outputString += printColors.green
        elif res[i] == GuessState.yellow:
            outputString += printColors.yellow
        else:
            outputString += printColors.red
        outputString += guess[i] + printColors.endc
    return outputString

if __name__ == "__main__":
    word = getValidWord(5)
    # print(word)
    guessNum = 0
    sharableResults = []
    while guessNum < 6:
        guessNum += 1
        guess = input(guessMap[guessNum] + " guess: ")
        if not validateGuess(guess):
            print(guess + " is not a valid guess, try again")
            guessNum -= 1
            continue
        res = compareLetters(word, guess)
        sharableResults.append(res)
        print(outputResult(res, guess))
        # TODO: print color coded alphabet
        if guess == word:
            print("Congratulations! You got the wordle in", guessNum, "guesses!")
            share = input("Would you like to share your result (y/n)?")
            if share.lower() == "y":
                print(sharableResults) #TODO: output emojis?
            exit(0)

    print("The wordle was " + word + ". Better luck next time!")

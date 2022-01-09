import argparse
from datetime import datetime, timedelta
import enchant
import enum
from random_word import RandomWords
import re
import sys

guessMap = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth", 6: "Sixth"}

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
            if self.letterMap[c] == guessState.green:
                outputString += printColors.green + c + printColors.endc
            elif self.letterMap[c] == guessState.yellow:
                outputString += printColors.yellow + c + printColors.endc
            elif self.letterMap[c] == guessState.red:
                outputString += printColors.red + c + printColors.endc
            else:
                outputString += c
        print(outputString)

def validateWord(s, n):
    if s == None:
        return False
    if len(s) != n:
        return False
    if not re.fullmatch('[a-z]+', s):
        return False
    d = enchant.Dict("en_US")
    return d.check(s)

class wordGenerator:
    def __init__(self, n, t=30):
        self.l = n
        self.r = RandomWords()
        self.t = t
    
    def generateWord(self):
        timeout = datetime.now() + timedelta(seconds=self.t)
        while datetime.now() < timeout:
            s = self.r.get_random_word(hasDictionaryDef=True, minLength=self.l, maxLength=self.l)
            if validateWord(s, self.l):
                return s

class guessState(enum.Enum):
    green = 1
    yellow = 2
    red = 3

class printColors:
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    endc = '\033[0m'

def compareLetters(word, guess, a):
    if len(word) != len(guess):
        sys.exit("len(word) != len(guess)")
    letters = word
    r = [None]*len(word)
    
    for i in range(len(word)):
        if word[i] == guess[i]:
            r[i] = guessState.green
            letters = letters.replace(word[i], "", 1)
            a.updateMap(word[i], guessState.green)
    for i, val in enumerate(r):
        if val == None:
            if guess[i] in letters:
                r[i] = guessState.yellow
                letters = letters.replace(guess[i], "", 1)
                if a.get(guess[i]) != guessState.green:
                    a.updateMap(guess[i], guessState.yellow)
            else:
                r[i] = guessState.red
                if a.get(guess[i]) != guessState.green and a.get(guess[i]) != guessState.yellow:
                    a.updateMap(guess[i], guessState.red)
    return r, a

def outputResult(res, s):
    if len(res) != len(s):
        sys.exit("len(res) != len(s)")
    outputString = ""
    for i in range(len(s)):
        if res[i] == guessState.green:
            outputString += printColors.green
        elif res[i] == guessState.yellow:
            outputString += printColors.yellow
        else:
            outputString += printColors.red
        outputString += s[i] + printColors.endc
    return outputString

if __name__ == "__main__":
    #TODO: add hardmode
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, default=5, help="number of letters in wordle", required=False)
    parser.add_argument("--maxGuesses", type=int, default=6, help="maximum number of guesses", required=False)
    args = parser.parse_args()

    a = alphabet()
    w = wordGenerator(args.length)

    word = w.generateWord()
    if word == "":
        sys.exit("error generating valid word")

    guessNum = 0
    sharableResults = []
    while guessNum < args.maxGuesses:
        guessNum += 1
        guess = input(guessMap[guessNum] + " guess: ")
        if not validateWord(guess, args.length):
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

from platform import java_ver
from flask import Flask, render_template, request
import guesses
import wordle
import words
import sys


app = Flask(__name__)

@app.route("/")
def root():
    global w
    try:
        w = wordle.Wordle(6, 5, False)
    except words.generatorTimeout:
        return "<p>Failed to generate word! Refresh the page.</p>"
    w.guessNum = 1
    return render_template("main.html", guessMap=w.processor.results, guessNum=str(w.guessNum))

@app.route('/calculate', methods = ["POST"])
def calculate():
    # get guess from input
    data = request.form
    guess = str(data["guess"]).lower()
    
    # validate guess, if guess is invalid, decrement guess number and try again
    if not w.validator.validateWord(guess, w.length):
        w.guessNum -= 1
        return "<p>invalid guess.</p>"

    # process guess
    try:
        w.guessNum += 1
        w.processor.processGuess(guess)
    except guesses.mismatchedLength:
        return "<p>error processing guess: length of guess does not match length of wordle.</p>"
    except guesses.invalidHardMode:
        w.guessNum -= 1
        return "<p>error processing guess: length of guess does not match length of wordle.</p>"

    # win logic
    if guess == w.wordle:
        return "<p>Congrats! You got the wordle :)</p>"
    # lose logic
    elif w.guessNum > w.maxGuesses:
        return "<p>Out of guesses :(</p>"

    return render_template("main.html", guessMap=w.processor.results, guessNum=str(w.guessNum))

if __name__ == "__main__":
    app.run()
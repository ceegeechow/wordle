from platform import java_ver
from flask import Flask, render_template, request
import guesses
import utils
import wordle
import words

app = Flask(__name__)

@app.context_processor
def injectContext():
    return dict(guessState=utils.guessState)

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
        #w.guessNum -= 1
        return "<p>invalid guess.</p>"

    # process guess
    try:
        w.guessNum += 1
        w.processor.processGuess(guess)
    except guesses.mismatchedLength:
        return "<p>error processing guess: length of guess does not match length of wordle.</p>"
    except guesses.invalidHardMode:
        #w.guessNum -= 1
        return "<p>error processing guess: length of guess does not match length of wordle.</p>"

    # win logic
    if guess == w.wordle:
        return render_template("won.html")
    # lose logic
    elif w.guessNum > w.maxGuesses:
        return render_template("lost.html", word=w.wordle)

    return render_template("main.html", guessMap=w.processor.results, guessNum=str(w.guessNum))

if __name__ == "__main__":
    app.run()
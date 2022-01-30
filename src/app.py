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

@app.route('/', methods = ["POST"])
def calculate():
    # get guess from input
    data = request.form
    guess = str(data["guess"]).lower()
    
    # validate guess, if guess is invalid, decrement guess number and try again
    if not w.validator.validateWord(guess, w.length):
        return render_template("main.html", guessMap=w.processor.results, guessNum=str(w.guessNum),
            invalidGuess=True, errorMessage="invalid word, try again")

    # process guess
    try:
        w.processor.processGuess(guess)
    except guesses.mismatchedLength:
        return render_template("main.html", guessMap=w.processor.results, guessNum=str(w.guessNum),
            invalidGuess=True, errorMessage="incorrect word length, try again")
    except guesses.invalidHardMode:
        return render_template("main.html", guessMap=w.processor.results, guessNum=str(w.guessNum),
            invalidGuess=True, errorMessage="invalid guess (hard mode), try again")

    w.guessNum += 1
    # win logic
    if guess == w.wordle:
        return render_template("won.html")
    # lose logic
    elif w.guessNum > w.maxGuesses:
        return render_template("lost.html", word=w.wordle)

    return render_template("main.html", guessMap=w.processor.results, guessNum=str(w.guessNum))

if __name__ == "__main__":
    app.run()
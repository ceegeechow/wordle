from platform import java_ver
from flask import Flask, render_template, request
import guesses
import wordle
import words
import sys


app = Flask(__name__)

@app.route("/")
# def example():
#     return render_template('example.html', name='Camille')
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
    data = request.form
    guess = data["guess"]
    # process guess and output result
    try:
        w.processor.processGuess(guess)
    except guesses.mismatchedLength:
        return "<p>error processing guess: length of guess does not match length of wordle.</p>"
    except guesses.invalidHardMode:
        w.guessNum -= 1
        return "<p>error processing guess: length of guess does not match length of wordle.</p>"

    return render_template("main.html", guessMap=w.processor.results, guessNum=str(w.guessNum))

if __name__ == "__main__":
    app.run()
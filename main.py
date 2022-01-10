import constants
import sys
import wordle

if __name__ == "__main__":
    args = constants.parseArguements()

    if args.rules:

        print("""
            After each guess, the color of the tiles will change to show how close your guess was to the word.
            Green means the letter is in the word and in the correct spot.
            Yellow means the letter is in the word, but in the wrong spot.
            Red means the letter is not in the word.
        """)
        sys.exit()

    try:
        w = wordle.Wordle(args.maxGuesses, args.length, args.hardMode)
    except words.generatorTimeout:
        sys.exit("error generating wordle")
    w.play()

import argparse
import sys
import wordle
import words

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rules", help="display rules", action="store_true")
    parser.add_argument("-l", "--length", type=int, default=5, help="number of letters in wordle", required=False)
    parser.add_argument( "-mg", "--maxGuesses",type=int, default=6, help="maximum number of guesses", required=False)
    parser.add_argument("-hm", "--hardMode", help="any revealed hints must be used in subsequent guesses", action="store_true")
    args = parser.parse_args()

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

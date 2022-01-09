import argparse
import sys
import wordle
import words

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, default=5, help="number of letters in wordle", required=False)
    parser.add_argument("--maxGuesses", type=int, default=6, help="maximum number of guesses", required=False)
    parser.add_argument("--hardMode", type=bool, default=False, help="any revealed hints must be used in subsequent guesses", required=False)
    args = parser.parse_args()

    try:
        w = wordle.Wordle(args.maxGuesses, args.length, args.hardMode)
    except words.generatorTimeout:
        sys.exit("error generating wordle")
    w.play()

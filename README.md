## Running instructions

### Dependencies
- python3
- enchant: https://pypi.org/project/pyenchant/
- random_word: https://pypi.org/project/Random-Word/

### Run Steps

- `git clone https://github.com/ceegeechow/wordle.git`

- `cd wordle`

- `python3 main.py`

### Flags/Usage: 

```
usage: main.py [-h] [--length LENGTH] [--maxGuesses MAXGUESSES] [--hardMode HARDMODE]

optional arguments:
  -h, --help            show this help message and exit
  --length LENGTH       number of letters in wordle
  --maxGuesses MAXGUESSES
                        maximum number of guesses
  --hardMode HARDMODE   any revealed hints must be used in subsequent guessesmain.py [-h] [--length LENGTH] [--maxGuesses MAXGUESSES] [--hardMode HARDMODE]
  ```

## ToDos
- better filtering of obscure words
- expand to web app
- unit tests
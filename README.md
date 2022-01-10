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
usage: main.py [-h] [-r] [-l LENGTH] [-mg MAXGUESSES] [-hm]

optional arguments:
  -h, --help            show this help message and exit
  -r, --rules           display rules
  -l LENGTH, --length LENGTH
                        number of letters in wordle
  -mg MAXGUESSES, --maxGuesses MAXGUESSES
                        maximum number of guesses
  -hm, --hardMode       any revealed hints must be used in subsequent guesses
  ```

## ToDos
- better filtering of obscure words/more efficient word generation
- use virtual environment
- expand to web app
- unit tests
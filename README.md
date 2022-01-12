## Running instructions

### Dependencies
- Python **3.9 or greater**
- This project uses python binding to **Enchant** for spell checking. For the python bindings to 
work it must be able to find the Enchant C library. **You must install this yourself**.
Instructions for your system can be found [here](http://pyenchant.github.io/pyenchant/install.html#installing-the-enchant-c-library).
- [Poetry](https://python-poetry.org) is used for dependency and virtual environment management. If you would
prefer not to use Poetry, you can install dependencies listed in `pyproject.toml` manually.
No guaranty can be made that this will work.

### Run Steps

Clone this repository and navigate inside it.
```shell
git clone https://github.com/ceegeechow/wordle.git
cd wordle
```

Install dependencies with Poetry
```shell
poetry install
```

Run inside virtual environment
```shell
poetry run python main.py
```

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
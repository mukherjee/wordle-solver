# wordle solver
Script to solve Wordle puzzle in 6 guesses or fewer
## https://www.powerlanguage.co.uk/wordle/

# How to use the Wordle solver script

The Python script is a console-based script where users enter their guesses and the color of the boxes to determine the next best move. Based on my testing, all puzzles are solved within six guesses

## TOC
- Install Python from python.org. No external libraries are needed
- Run the script from the command line/terminal with the appropriate arguments
- After running the script, you will be told what the next best guess is. A backup guess is given if the recommended guess is not accepted. Build the input string and re-run until only one best guess is given.

## Install Python

- Install Python from Python.org
- Check your installation by running "python --version". It should not error out

## Download the `wordle.py` script and the associated five-letter word wordslist.
- The script is `wordle.py`
- The word list filename is `5-letter-words.txt`. Save it to the same directory where `wordle.py` is located.

## Using the script.

The general format of running the script is to type python3 and a single multi-string argument (enclosed in a single set of quotes). The multistring argument should have the strings in pairs. The first string is the guess that was provided, and the second string should be the resulting colors. A single character is used to represent the name of the color. Because, Green and Gray both start with "G", I am using "B" as Gray, is it's close to Gray.
- ### ![#f1c40f](https://via.placeholder.com/15/f1c40f/000000?text=+) "Y" = Yellow. Correct letter, but in the wrong place
- ### ![#2ecc71](https://via.placeholder.com/15/2ecc71/000000?text=+) "G" = Green. Letter is in the correct place
- ### ![#2c3e50](https://via.placeholder.com/15/2c3e50/000000?text=+) "B" = Black/Gray. The letter does not appear in the solution.
 
### An example of coding the color results in the string argument. 
Suppose the guess is "table", and the puzzle solution is actually "store".
The puzzle will return colors: ![#000000](https://via.placeholder.com/15/f1c40f/000000?text=+)![#2c3e50](https://via.placeholder.com/15/2c3e50/000000?text=+)![#2c3e50](https://via.placeholder.com/15/2c3e50/000000?text=+)![#2c3e50](https://via.placeholder.com/15/2c3e50/000000?text=+)![#2ecc71](https://via.placeholder.com/15/2ecc71/000000?text=+)


The correct format to run this through the script from the command line is:
```diff
- Note that the guess word must all be lowercase
- The letters representing the colors must be CAPS 
```
```
$ python3 wordle.py "table YBBBG"
```
After executing the command you will see the recommended next guess. A backup suggestion is provided in case the primary suggestion is rejected. The output will look as follows:
```
$ python3 wordle.py "table YBBBG"

Recommended next word: suite
Backup word: ['store']
$
```
The next step is to enter the recommended guess and rerun the program with the next color results. You will need to include the first guess and its results for the second iteration. In other words, you build the argument with each guess. You can hit the "up" arrow to populate the command line with the previous command. Note the single set of quotes wrapped around the argument:
```
$ python3 wordle.py "table YBBBG suite GBBYG"

Recommended next word: stoke
Backup word: ['stone']

$ 
```
Below are several examples:
## Example #1
One example, let's say, the puzzle solution is ```decoy```. I have found success with using ```about``` as a good initial guess for any puzzle. 

```
$python3 wordle.py "about BBYBB"

Recommended next word: doers
Backup word: ['loser']

$ python3 wordle.py "about BBYBB doers GYYBB"

Recommended next word: decoy
Backup word: ['demon']

$ python3 wordle.py "about BBYBB doers GYYBB decoy GGGGG"

Recommended next word: decoy
```

## Example #2
In this example we'll have a puzzle that has duplicate letters: ```loose```. I'll go with my usual initial guess ```about```. 

```
$ python3 wordle.py "about BBGBB"

Recommended next word: snore
Backup word: ['prose']


$ python3 wordle.py "about BBGBB snore YBGBG"

Recommended next word: chose
Backup word: ['close']

$ python3 wordle.py "about BBGBB snore YBGBG chose BBGGG"

Recommended next word: goose
Backup word: ['loose']

$ python3 wordle.py "about BBGBB snore YBGBG chose BBGGG goose BGGGG"

Recommended next word: loose
Backup word: ['moose']

$ python3 wordle.py "about BBGBB snore YBGBG chose BBGGG goose BGGGG loose GGGGG"

Recommended next word: loose
$ 
```

## Troubleshooting
-If the program crashes, try to use the backup suggestion. This may occur if the solution has duplicate letters.
Update: This bug has been fixed.
## License

MIT


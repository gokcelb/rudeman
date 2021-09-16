# Rudeman
This hangman game is just as fun as any other hangman game, but with a rude twist! Don't worry, it's just that the game prints out a rather rude message if you hang the man, nothing too saucy.

## Quick Start

Use the commands below to play __Rudeman__.

```bash
$ git clone https://github.com/gokcelb/rudeman
$ cd rudeman
$ python hangman.py # for Windows
$ python3 hangman.py # for Linux and Darwin
```

Here is how the game works:

There are categories of words - only "vehicle" and "technology" at the moment but its design allows adding new categories quite easily.

The game asks the user to choose one of these categories and assigns a random word from the chosen category. 

The words have difficulty levels for scoring. The score is updated with each word the user guesses correctly.

The random word is presented to the user in the form of underscores and as the user guesses the letters, either letters appear one by one on the screen or the hangman is gradually hung depending on whether they guessed right or wrong.

Pretty simple, right?

Here is how a sample game play of __Rudeman__ looks:

```bash
# Which category do you choose? Technology or vehicle?
> technology

________

# Type in a letter:
> m
__M_____

# Type in a letter:
> o
_OM_____

...
...
...

# Type in a letter:
> r
COMPUTER

Your current score: 5

NEW WORD
_____

# Type in a letter:
```

And here is what happens when you hang the man.

```bash
# Which category do you choose? Technology or vehicle?
> vehicle   

___

# Type in a letter:
> c

C not in word.    





/ \
___

...
...
...

# Type in a letter:
> c

C not in word.
 ________
 |       |
 |       O
 |
 |
/ \
___

...
...
...

# Type in a letter:
> c

C not in word.
 ________
 |       |
 |       O
 |     /( )\
 |     _| |_
/ \
___

Congragulations! You hanged the man you worthless piece of garbage.
```
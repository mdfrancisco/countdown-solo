# Countdown Solo

A console single-player version of **Countdown Letters Game** in Python. The game allows players to select vowels and consonants, generates a letter set, finds the longest valid English words, scores them, and keeps track of the total points across 4 rounds.


## Features
- **User letter selection**: Choose vowels or consonants for a 9-letter set.
    - Vowel and consonant stacks use frequency-weighted distributions.
- **Longest word calculation**: Automatically identifies the longest valid words from the letters.
- **Scoring system**:  
  - 9-letter words: 18 points  
  - Otherwise: length of the longest word
- **Four rounds**: Keeps track of total points.

## Sources
- Word List The English word list used in this project is taken from [words_alpha](https://github.com/dwyl/english-words) by DWYL.  
- Letter frequency data sourced from  https://en.wikipedia.org/wiki/Letter_frequency.



## Requirements

- Python 3.10+  
- `pytest` for running tests (optional)


## Installation

Clone the repository:

```bash
git clone https://github.com/mdfrancisco/countdown-solo.git

cd countdown-solo

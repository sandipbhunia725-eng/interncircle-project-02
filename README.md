# Project 02 — Number Guessing Game & Word Counter

**Language:** Python 3.10+  
**Type:** Beginner-friendly command-line application

## Features

### Number guessing game
- Random secret number from 1 to 100 using `random.randint()`
- Seven valid attempts per round
- Helpful “Too high”, “Too low”, and “Correct” feedback
- Whole-number and range validation
- Replay option and best-score tracking

### Word counter
- Reads a UTF-8 text file with a `with` block
- Handles missing or unreadable files
- Converts text to lowercase and removes punctuation
- Counts words with `collections.Counter`
- Displays total words, unique words, and the top 10 most common words

## Scoring rule
The player starts with **100 points**. Each incorrect valid guess deducts **10 points**. The score cannot go below zero. Invalid inputs and guesses outside 1–100 do not consume an attempt or reduce the score. Each round allows seven valid guesses.

## Files
- `main.py` — application source code
- `sample.txt` — sample text for testing the word counter
- `README.md` — documentation
- `submission_description.txt` — suggested submission notes

## How to run
Open a terminal in this folder and run:

```bash
python main.py
```

On some Windows installations, use `py main.py`.

Choose 1 to play, 2 to count words (press Enter to use `sample.txt`), or 3 to quit.

## Test checklist
- Enter letters or a decimal as a guess; the program should ask again.
- Enter 0 or 101; the program should reject it without using an attempt.
- Try guesses that are too high and too low.
- Confirm each incorrect valid guess deducts 10 points.
- Use all seven attempts and confirm the answer and score are displayed.
- Replay and check that the best score is retained during the session.
- Count words in `sample.txt`.
- Try a missing file and an empty text file.
- Confirm uppercase and lowercase versions count as the same word and punctuation is ignored.

## GitHub upload
Create a public repository named `interncircle-project-02`. Upload `main.py`, `sample.txt`, and `README.md`. You may also upload `submission_description.txt`. Copy the repository URL and submit it in InternCircle Project 02.

## Submission description
I created Project 02 – Number Guessing Game & Word Counter using Python. The guessing game selects a random number from 1 to 100, gives the player seven valid attempts, provides higher/lower hints, and tracks a score and best score. The scoring rule starts at 100 points and deducts 10 points for each incorrect valid guess. The word counter reads a UTF-8 text file, ignores case and punctuation, and uses `collections.Counter` to display total words, unique words, and the ten most common words.

## Before submitting
Run the program and test both menu options, including invalid guesses, a missing file, and an empty file. Make sure you can explain the functions and scoring rule. The learner guide asks you to write your own solution; use this project to understand, test, and adapt the code before submission.

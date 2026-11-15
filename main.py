"""
Project 02: Number Guessing Game & Word Counter
Scoring: start at 100 points; lose 10 points for each incorrect valid guess.
Invalid or out-of-range input does not use an attempt or reduce the score.
"""
import random
import string
from collections import Counter

LOWER_BOUND = 1
UPPER_BOUND = 100
MAX_ATTEMPTS = 7
STARTING_SCORE = 100
POINTS_PER_WRONG_GUESS = 10


def read_whole_number(prompt):
    """Keep asking until the user enters a whole number."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a whole number, such as 25.")


def play_one_round():
    """Run one round of the guessing game and return the score."""
    secret = random.randint(LOWER_BOUND, UPPER_BOUND)
    attempts = 0
    score = STARTING_SCORE
    print(f"Guess the secret number between {LOWER_BOUND} and {UPPER_BOUND}.")
    print(f"You have {MAX_ATTEMPTS} valid attempts.")

    while attempts < MAX_ATTEMPTS:
        guess = read_whole_number(f"Guess {attempts + 1}/{MAX_ATTEMPTS}: ")
        if not LOWER_BOUND <= guess <= UPPER_BOUND:
            print("Please enter a number from 1 to 100. This does not use an attempt.")
            continue

        attempts += 1
        if guess == secret:
            print(f"Correct! You found it in {attempts} attempt(s).")
            print(f"Score: {score}/{STARTING_SCORE}")
            return score

        score = max(0, score - POINTS_PER_WRONG_GUESS)
        print("Too high!" if guess > secret else "Too low!")
        print(f"Attempts remaining: {MAX_ATTEMPTS - attempts}")

    print(f"Game over. The secret number was {secret}.")
    print("Score: 0/100")
    return 0


def guessing_game():
    """Allow replay and keep the best score for this session."""
    best_score = 0
    while True:
        best_score = max(best_score, play_one_round())
        print(f"Best score: {best_score}/100")
        while True:
            replay = input("Play again? (y/n): ").strip().lower()
            if replay in ("y", "yes"):
                break
            if replay in ("n", "no"):
                print("Thanks for playing!")
                return
            print("Please enter y or n.")


def count_words(path):
    """Read a UTF-8 file and return its word-frequency Counter."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            text = file.read().lower()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except OSError as error:
        print(f"Could not read file: {error}")
        return None

    text = text.translate(str.maketrans("", "", string.punctuation))
    return Counter(text.split())


def word_counter():
    """Read a text file and print word statistics and the top ten words."""
    path = input("Text file path (Enter for sample.txt): ").strip() or "sample.txt"
    counts = count_words(path)
    if counts is None:
        return

    print("\nWORD COUNT REPORT")
    print("-" * 25)
    print("Total words :", sum(counts.values()))
    print("Unique words:", len(counts))
    if not counts:
        print("The file is empty or contains no words.")
        return

    print("\nTop 10 most common words")
    print(f"{'Word':<15}{'Count':>7}")
    print("-" * 22)
    for word, frequency in counts.most_common(10):
        print(f"{word:<15}{frequency:>7}")


def main():
    """Show the main menu until the user chooses to quit."""
    while True:
        print("\n" + "=" * 42)
        print("       NUMBER GUESSING & WORD COUNTER")
        print("=" * 42)
        print("1. Play the number guessing game")
        print("2. Count words in a text file")
        print("3. Quit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            guessing_game()
        elif choice == "2":
            word_counter()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

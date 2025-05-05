import random
import time

# Constants
WORDS_FILE = "./words.txt"
SCORES_FILE = "./scores.txt"

# Global variables
user_scores = {}

def load_words():
    try:
        with open(WORDS_FILE, 'r') as f:
            words = [line.strip() for line in f if line.strip()]
        return words
    except FileNotFoundError:
        print("Words file not found. Using default words.")
        return ["apple", "banana", "cherry", "date", "fig", "grape"]

def save_scores():
    with open(SCORES_FILE, 'w') as f:
        for user, score in user_scores.items():
            f.write(f"{user}:{score}\n")

def load_scores():
    try:
        with open(SCORES_FILE, 'r') as f:
            for line in f:
                if ':' in line:
                    name, score = line.strip().split(':')
                    user_scores[name] = int(score)
    except FileNotFoundError:
        pass

def scramble_word(word):
    word_letters = list(word)
    random.shuffle(word_letters)
    return ''.join(word_letters)

def play_round(word):
    scrambled = scramble_word(word)
    print(f"\nScrambled word: {scrambled}")
    guess = input("Your guess: ").strip().lower()

    if guess == word:
        print("Correct!")
        return True
    else:
        print(f"Wrong. The word was '{word}'")
        return False

def get_top_scores():
    print("\nTop Scores:")
    sorted_scores = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
    for name, score in sorted_scores[:5]:
        print(f"{name}: {score}")

def main():
    print("=== Welcome to the Word Scramble Game ===")
    username = input("Enter your name: ").strip()
    if username not in user_scores:
        user_scores[username] = 0

    words = load_words()
    random.shuffle(words)
    rounds = min(5, len(words))

    print(f"\nYou'll play {rounds} rounds. Good luck, {username}!\n")
    time.sleep(1)

    for i in range(rounds):
        print(f"\n--- Round {i + 1} ---")
        success = play_round(words[i])
        if success:
            user_scores[username] += 1

    print(f"\nGame is over! You scored {user_scores[username]} points.")
    save_scores()
    get_top_scores()

# Load previous scores before starting
load_scores()

# Start the game
if __name__ == "__main__":
    import ipdb; ipdb.set_trace()
    main()


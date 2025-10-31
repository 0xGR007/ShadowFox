#2. Hangman: Implement the wordguessing game with visual progress and hints.
import random
# Hangman visual stages
hangman_stages = [
    """
      +---+
          |
          |
          |
         ===
    """,
    """
      +---+
      O   |
          |
          |
         ===
    """,
    """
      +---+
      O   |
      |   |
          |
         ===
    """,
    """
      +---+
      O   |
     /|   |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
     /    |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
     / \\  |
         ===
    """,
]

def play_hangman():
    words = ["python", "internship", "superman", "laptop", "developer"]
    word_to_guess = random.choice(words)
    hidden_word = ["_"] * len(word_to_guess)
    guessed_letters = []
    lives = 6

    print("Welcome to Hangman Game!")
    print("Word to guess:", " ".join(hidden_word))

    while lives > 0 and "_" in hidden_word:
        print(hangman_stages[6 - lives])
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct guess!")
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    hidden_word[i] = guess
        else:
            lives -= 1
            print(f"Wrong guess! Lives left: {lives}")

        print("Current word:", " ".join(hidden_word))
        print("Guessed so far:", ", ".join(guessed_letters))
        print("-" * 30)

    if "_" not in hidden_word:
        print("Congratulations! You guessed the word:", word_to_guess)
    else:
        print(hangman_stages[6])
        print("Game Over! The word was:", word_to_guess)

while True:
    play_hangman()
    again = input("Do you want to play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! Goodbye!")
        break

#Output:
'''
Welcome to Hangman Game!
Word to guess: _ _ _ _ _ _ _ _ _

      +---+
          |
          |
          |
         ===
    
Guess a letter: l
Correct guess!
Current word: _ _ _ _ l _ _ _ _
Guessed so far: l
------------------------------

      +---+
          |
          |
          |
         ===
    
Guess a letter: a
Wrong guess! Lives left: 5
Current word: _ _ _ _ l _ _ _ _
Guessed so far: l, a
------------------------------

      +---+
      O   |
          |
          |
         ===
    
Guess a letter: d
Correct guess!
Current word: d _ _ _ l _ _ _ _
Guessed so far: l, a, d
------------------------------

      +---+
      O   |
          |
          |
         ===
    
Guess a letter: e
Correct guess!
Current word: d e _ e l _ _ e _
Guessed so far: l, a, d, e
------------------------------

      +---+
      O   |
          |
          |
         ===
    
Guess a letter: v
Correct guess!
Current word: d e v e l _ _ e _
Guessed so far: l, a, d, e, v
------------------------------

      +---+
      O   |
          |
          |
         ===
    
Guess a letter: o
Correct guess!
Current word: d e v e l o _ e _
Guessed so far: l, a, d, e, v, o
------------------------------

      +---+
      O   |
          |
          |
         ===
    
Guess a letter: r
Correct guess!
Current word: d e v e l o _ e r
Guessed so far: l, a, d, e, v, o, r
------------------------------

      +---+
      O   |
          |
          |
         ===
    
Guess a letter: p
Correct guess!
Current word: d e v e l o p e r
Guessed so far: l, a, d, e, v, o, r, p
------------------------------
Congratulations! You guessed the word: developer
Do you want to play again? (y/n): n
Thanks for playing! Goodbye!
'''
'''Task-02 2.Hangman is completed successfully'''

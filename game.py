# This code sets up the Word Guessing Game for use in CPSC217
# By Richard Zhao
# This file should not be edited in any way for the assignment
# Your code should be created in a new, separate file called game_functions.py

import game_functions

# Get the names of the three other files from the file "file_names.txt"
words_file, config_file, score_file = game_functions.get_file_names()

max_length, min_length, start_letters, index_to_choose, max_attempts =  game_functions.read_config(config_file)

words = game_functions.load_words(words_file)

word_to_guess = game_functions.choose_word(words, max_length, min_length, start_letters, index_to_choose)

guessed_letters = set()
incorrect_guesses = 0

print("Welcome to Guessing Words!")

score = game_functions.get_score(score_file)
print(f"The current high score is: {score}.")

print(f"The word has {len(word_to_guess)} letters.")
end = 0

while incorrect_guesses < max_attempts and not end:
    print("\n" + game_functions.display_word(word_to_guess, guessed_letters))
    new_guess = input("Guess a letter: ").lower()

    result = game_functions.guess_letter(new_guess, guessed_letters, word_to_guess)

    if result == 1:
        print("Invalid input. Please enter a single alphabetic character.")
    elif result == 2:
        print("You already guessed that letter.")
    elif result == 3:
        print(f"Yes, '{new_guess}' is in the word.")
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! You have {max_attempts - incorrect_guesses} attempts left.")


    guessed_letters.add(new_guess)

    end = game_functions.end_game(word_to_guess, guessed_letters, incorrect_guesses, max_attempts)
    if end == 1:
        print("\nCongratulations! You guessed the word:", word_to_guess)
    elif end == 2:
        print("\nYou lost! The word was:", word_to_guess)


calculated_score = game_functions.calculate_score(max_attempts, incorrect_guesses)
print("\nYour score is:", calculated_score)
game_functions.save_score(score_file, calculated_score)

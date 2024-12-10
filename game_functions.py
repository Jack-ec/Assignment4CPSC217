# Jack Chidlaw, UCID:30187692, Hangman game, Assignment 4
import random


def get_file_names():
    try:
        with open("file_names.txt", "r") as file:
            content = file.read()
            content = content.split()
            words_file_name = str(content[0].strip())
            config_file_name = str(content[1].strip())
            score_file_name = str(content[2].strip())
        return words_file_name, config_file_name, score_file_name
    except FileNotFoundError:
        print("Error: 'file_names.txt' not found. Please ensure the file exists in the working directory.")
        return "", "", ""

def read_config(config_file_name):
    try:
        with open(config_file_name, "r") as file:
            content = file.readlines()
            max_length, min_length, start_letters, index_to_choose, max_attempts = [], [], [], [], []
            for line in content:
                line = line.strip()
                if "max_length" in line:
                    max_length = int(line.split()[1])
                if "min_length" in line:
                    min_length = int(line.split()[1])
                if "start_letters" in line:
                    start_letters = str(line.split()[1])
                if "index_to_choose" in line:
                    index_to_choose = int(line.split()[1])
                if "max_attempts" in line:
                    max_attempts = int(line.split()[1])
        return max_length, min_length, start_letters, index_to_choose, max_attempts
    except FileNotFoundError:
        print("File not found while executing read_config: Ensure the file exists in the working directory")
        max_length, min_length, start_letters, index_to_choose, max_attempts = 15, 1, "abc", 5, 6
        return max_length, min_length, start_letters, index_to_choose, max_attempts

def load_words(words_file_name):
    try:
        with open(words_file_name, "r") as file:
            words = file.read().split()
        return words
    except FileNotFoundError:
        print("File not found while executing load_words: Ensure file exists in the working directory")
        words = ["adventure","chocolate","diversity","car","according","ear","kind","conserve","friendship","employment","analysis","emotional"]
        return words

def choose_word(words, max_length, min_length, start_letters, index_to_choose):
    try:
        filtered_words = []
        for word in words:
            if min_length <= len(word) <= max_length and word[0] in start_letters:
                filtered_words.append(word)
        random.shuffle(filtered_words)
        if len(filtered_words) >= index_to_choose:
            word_to_guess = str(filtered_words[-1])
        else:
            word_to_guess = str(filtered_words[index_to_choose])
        return word_to_guess
    except Exception as error:
        print("an Error occurred during choose_word:", error)
        word_to_guess = random.choice(words)
        return word_to_guess



def get_score(score_file_name):
    try:
        with open(score_file_name, "r") as file:
            score = file.read().split()
            score = int(score[0])
        return score
    except FileNotFoundError:
        print("File not found while executing get_score: Ensure file exists")
        score = 0
        return score

def display_word(word_to_guess, guessed_letters):
    displayed_word = " ".join(letter if letter in guessed_letters else "_" for letter in word_to_guess)
    return displayed_word

def guess_letter(new_guess, guessed_letters, word_to_guess):
    if not new_guess.isalpha():
        return 1
    if new_guess in guessed_letters:
        return 2
    if new_guess in word_to_guess and new_guess not in guessed_letters:
        return 3

def end_game(word_to_guess, guessed_letters, incorrect_guesses, max_attempts):
    remaining_guesses = max_attempts - incorrect_guesses
    if "_" not in display_word(word_to_guess, guessed_letters):
        return 1
    if remaining_guesses == 0:
        return 2
    else:
        return 0

def calculate_score(max_attempts, incorrect_guesses):
    remaining_guesses = max_attempts - incorrect_guesses
    score = remaining_guesses * 100
    return score

def save_score(score_file_name, calculated_score):
    try:
        with open(score_file_name, "r") as file:
            score = int(file.read().strip())
        if calculated_score > score:
            with open(score_file_name, "w") as file:
                file.write(str(calculated_score))
    except FileNotFoundError:
        print("File not found while executing save_score: Ensure file exists in working directory")

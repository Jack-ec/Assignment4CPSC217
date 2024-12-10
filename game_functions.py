# Jack Chidlaw, UCID:30187692, Hangman game, Assignment 4
import random #used later


def get_file_names():
    try:
        with open("file_names.txt", "r") as file: # open file with name file_names.txt, split contents into a list
            content = file.read()                 # assign the names of files accordingly based on index
            content = content.split()
            words_file_name = str(content[0].strip())
            config_file_name = str(content[1].strip())
            score_file_name = str(content[2].strip())
        return words_file_name, config_file_name, score_file_name
    except FileNotFoundError: # if file is not found print information and return empty strings so the rest of program can run
        print("Error: 'file_names.txt' not found. Please ensure the file exists in the working directory.")
        return "", "", ""

def read_config(config_file_name):
    try:
        with open(config_file_name, "r") as file: # open config file and assign info based on the name in index 0 for each line
            content = file.readlines()            # return values will be in index 1 when split into lists
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
    except FileNotFoundError: # if the file is not  found, deliver information to console and return default  values so the program can still run
        print("File not found while executing read_config: Ensure the file exists in the working directory")
        max_length, min_length, start_letters, index_to_choose, max_attempts = 15, 1, "abc", 5, 6
        return max_length, min_length, start_letters, index_to_choose, max_attempts

def load_words(words_file_name):
    try:
        with open(words_file_name, "r") as file: #open and read words file and split into list of words to be returned
            words = file.read().split()
        return words
    except FileNotFoundError: # if the file is not found deliver info to console and return default list of words so there will still be a primitive game
        print("File not found while executing load_words: Ensure file exists in the working directory")
        words = ["adventure","chocolate","diversity","car","according","ear","kind","conserve","friendship","employment","analysis","emotional"]
        return words

def choose_word(words, max_length, min_length, start_letters, index_to_choose):
    try:
        filtered_words = [] # filter words from list based on specified config criteria
        for word in words:
            if min_length <= len(word) <= max_length and word[0] in start_letters:
                filtered_words.append(word)
        random.shuffle(filtered_words) # shuffle words from filtered list
        if len(filtered_words) >= index_to_choose: #if index is larger than filtered list just choose the last word
            word_to_guess = str(filtered_words[-1])
        else:
            word_to_guess = str(filtered_words[index_to_choose]) # if index to choose is in range, choose word from specified index
        return word_to_guess
    except Exception as error: #if an error occurs, deliver info to console and pick a random unfiltered word 
        print("an Error occurred during choose_word:", error)
        word_to_guess = random.choice(words)
        return word_to_guess

def get_score(score_file_name):
    try:
        with open(score_file_name, "r") as file: #read score file and get the score value
            score = file.read().split()
            score = int(score[0])
        return score
    except FileNotFoundError: # if score file is not found deliver info to console and default the score to 0
        print("File not found while executing get_score: Ensure file exists in the working directory")
        score = 0
        return score

def display_word(word_to_guess, guessed_letters):
    displayed_word = " ".join(letter if letter in guessed_letters else "_" for letter in word_to_guess)
    return displayed_word  # check if letters in word to guess has been guessed, if not display "_" in thier place
                           # no exception handling required 
def guess_letter(new_guess, guessed_letters, word_to_guess):
    if not new_guess.isalpha(): #if the new guess doesn't exist in english alphabet return gamestate 1
        return 1
    if new_guess in guessed_letters: #if the new guess has already been guessed return gamestate 2
        return 2 
    if new_guess in word_to_guess and new_guess not in guessed_letters: #if the new guess has not been guessed return gamestate 3
        return 3

def end_game(word_to_guess, guessed_letters, incorrect_guesses, max_attempts):
    remaining_guesses = max_attempts - incorrect_guesses
    if "_" not in display_word(word_to_guess, guessed_letters): #if no underscores in display word than game has been won, return gamestate 1
        return 1
    if remaining_guesses == 0: #if player has run out of guessses return gamestate 2
        return 2
    else: #player is still playing, return gamestate 0
        return 0

def calculate_score(max_attempts, incorrect_guesses):
    remaining_guesses = max_attempts - incorrect_guesses #calculate score based off of players remaining guesses
    score = remaining_guesses * 100
    return score

def save_score(score_file_name, calculated_score):
    try:
        with open(score_file_name, "r") as file: #read current high score from score file
            score = int(file.read().strip())
        if calculated_score > score: # if new score is higher, overwrite old score
            with open(score_file_name, "w") as file:
                file.write(str(calculated_score))
    except FileNotFoundError: # if score file is not found, deliver info to console and do nothing else
        print("File not found while executing save_score: Ensure file exists in working directory")

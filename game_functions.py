from game import index_to_choose, max_attempts, words


def get_file_names():
    with open("file_names.txt", "r") as file:
        content = file.read()
        content = content.split()
        words_file_name = str(content[1].strip())
        config_file_name = str(content[2].strip())
        score_file_name = str(content[3].strip())
    return words_file_name, config_file_name, score_file_name


def read_config(config_file_name):
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
                start_letters = int(line.split()[1])
            if "index_to_choose" in line:
                index_to_choose = int(line.split()[1])
            if "max_attempts" in line:
                max_attempts = int(line.split()[1])
    return max_length, min_length, start_letters, index_to_choose, max_attempts

def load_words(words_file_name):
    with open(words_file_name, "r") as file:
        words = file.read().split()
    return words

def choose_word(words, max_length, min_length, start_letters, index_to_choose):
    filtered_words = []
    for word in words:
        if len(word) <= max_length and len(word) >= min_length and word[0] in start_letters:
            filtered_words.append(word)
    if len(filtered_words) > index_to_choose:
        return filtered_words[len(filtered_words)]
    else:
        return filtered_words[index_to_choose]

def get_score(score_file_name):
    with open(score_file_name, "r") as file:
        score = file.read().split()
        score = int(score[1])
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

def
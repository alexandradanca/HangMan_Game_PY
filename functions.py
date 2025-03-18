def display(man, word):
    for idx, line in enumerate(man):
        if idx == 1:
            print(line + "  *   " + word)
        else:
            print(line + "  *")

    print("******")

def verify_user_letter(word, letter, guessed_letters):
    if letter in guessed_letters:
        print(f"Letter '{letter}' has already been guessed.")
        return False
    else:
        return letter in word
    
def verify_middle_letters(word, letter):
    for i in range(1, len(word) - 1):  
        if word[i] == letter:
            return True
    return False


    
def verify_word_completed(random_word, my_word):
    return random_word == my_word

def add_letters(random_word, my_word, indexes):
    my_word = list(my_word)

    for i in indexes:
        my_word[i] = random_word[i]

    return ''.join(my_word)

def get_letter_positions(word, letter):
    return [i for i, l in enumerate(word) if l == letter]

def display_word_mode(word, mode, user_input=None, current_word=""):
    new_word = current_word

    match mode:
        case "start_game":
            for x in range(0, len(word)):
                if x == 0 or x == len(word)-1:
                    new_word += word[x]
                else:
                    new_word += "_"

        case "replace_letter":
            idxs = get_letter_positions(word, user_input)
            if len(idxs) > 0:
                new_word = add_letters(word, new_word, idxs)

    return new_word
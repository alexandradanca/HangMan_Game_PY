import random
from functions import display, verify_user_letter,verify_middle_letters, verify_word_completed, display_word_mode
from constants import fruits, draw_man
                        
def main():
    random_word = random.choice(fruits)
    user_word = ""
    err_counter = 0
    mode = "start_game"
    guessed_letters = set()

    while err_counter < 7:
        if mode == "start_game":
            user_word = display_word_mode(random_word, mode, current_word=user_word)
            display(draw_man[err_counter], user_word)
            mode = "replace_letter"
        else:
            user = input("Enter a letter: ")
            print("***********")

            while len(user) != 1:
                print("Too many letters. Please insert just one letter.")
                user = input("Enter a letter: ")
                print("***********")

            if verify_user_letter(random_word, user, guessed_letters):
                if verify_middle_letters(random_word, user):
                   guessed_letters.add(user)
                else:
                    err_counter += 1 
                user_word = display_word_mode(random_word, mode, user_input=user, current_word=user_word)
            else:
                err_counter += 1
            
            display(draw_man[err_counter], user_word)

            if err_counter == 6:
                print("YOU LOSE! The word was:", random_word)
                break
            elif verify_word_completed(random_word, user_word):
                print("YOU WIN! The word was:", random_word)
                break
            else:
                continue    


if __name__=="__main__":
    main()

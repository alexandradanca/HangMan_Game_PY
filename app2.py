import tkinter as ttk
from tkinter import PhotoImage, messagebox
from constants import alphabet, fruits
import random

random_word = "_ _ _ _ _"
hang_img_list = ["hang0.png","hang1.png","hang2.png","hang3.png","hang4.png","hang5.png","hang6.png"]
user_word = ""
err_counter = 0
guessed_letters = set()
mode = "start_game"

def red_flash():
    hang_label.config(bg="red")
    hang_label.after(200, lambda: hang_label.config(bg="#57B4BA"))
    
def warning_message(text):
    ttk.messagebox.showwarning(title = "Warning", message = text)
    
def space_btw_letters(word):
    new_word = ""
    for l in range(len(word)):
        new_word += " " + word[l]
    return new_word

def start_game():
    global random_word, user_word, err_counter, guessed_letters, mode, current_img
    random_word = random.choice(fruits)
    user_word = ""
    err_counter = 0
    guessed_letters = set()
    mode = "play_game"
    
    for x in range(0, len(random_word)):
        if x == 0 or x == len(random_word)-1:
            user_word += random_word[x]
        else:
            user_word += "_"
    
    word_label.config(text=space_btw_letters(user_word))   
    current_img = PhotoImage(file=f"./hang_images/{hang_img_list[0]}")
    hang_label.config(image=current_img) 
    
def click(letter):
    global random_word, user_word, err_counter, guessed_letters, mode, current_img
    
    if mode == "start_game":
        warning_message("Please start the game befor click the buttons")
    else:
        found = False
        if letter not in guessed_letters:
            guessed_letters.add(letter)
            for x in range(1, len(random_word) - 1):
                if random_word[x] == letter:
                    user_word = user_word[:x] + letter + user_word[x + 1:]
                    found = True
            
            if not found:
                err_counter += 1
                red_flash()
        else:
            err_counter += 1
            red_flash()
        
        word_label.config(text=space_btw_letters(user_word))    
        current_img = PhotoImage(file=f"./hang_images/{hang_img_list[err_counter]}")
        hang_label.config(image=current_img)
        
        if err_counter == 6:
            warning_message(f"YOU LOSE! The word was: {random_word}")
        elif user_word == random_word:
            warning_message(f"YOU WIN! The word was: {random_word}")
        else:
            pass

window = ttk.Tk()
window.geometry('700x700')
window.title("Hangman Game")
window.configure(background="#57B4BA")
window.resizable(False,False)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=0)
window.rowconfigure(1, weight=0)
window.rowconfigure(2, weight=0)
window.rowconfigure(3, weight=1)


title_frame = ttk.Frame(window, height=50)
title_frame.grid(row=0, column=0, sticky="nsew")
title_frame.rowconfigure(0, weight=1)
title_frame.columnconfigure(0, weight=1)
title = ttk.Label(title_frame, text="HangMan Game", font = "Fixedsys 20 bold", bg="#57B4BA", foreground="#6D2323")
title.grid(row=0, column=0, sticky="nsew")


game_frame = ttk.Frame(window, bg="#57B4BA", height=325)
game_frame.grid(row=1, column=0, sticky="nsew")
game_frame.rowconfigure(0, weight=1)
game_frame.columnconfigure(0, weight=1)
game_frame.columnconfigure(1, weight=1)

img = PhotoImage(file = "./hang_images/hang0.png")
hang_label = ttk.Label(game_frame, 
          justify="left",
          compound = "left",
          height=325,
          image=img,
          bg="#57B4BA")
hang_label.grid(row=0, column=0)

word_label = ttk.Label(game_frame, bg="#57B4BA", text=random_word, font = "Fixedsys 20", foreground="#015551")
word_label.grid(row=0, column=1, sticky="nsew")


btn_start = ttk.Button(window, text="Start Game", bg="#FE4F2D", font = "Fixedsys 15", foreground="#015551", command = start_game, width=15, height=2)
btn_start.grid(row=2, column=0, padx=50)


alphabet_frame = ttk.Frame(window, bg="#57B4BA", height=100)
alphabet_frame.grid(row=3, column=0)

y = 0
r = 1
for x in range(0,26): 
    if x < 8:
        btn = ttk.Button(alphabet_frame, text=alphabet[x],font = "Fixedsys 15", bg="#E5D0AC",
                         foreground="#015551", width= 5, command=lambda l=alphabet[x]: click(l))
        btn.grid(row = 0, column = x, sticky = "nsew", padx = 10, pady = 10)         
    elif x > 7 and y < 8:
        btn = ttk.Button(alphabet_frame, text=alphabet[x],font = "Fixedsys 15", bg="#E5D0AC",
                         foreground="#015551", width= 5, command=lambda l=alphabet[x]: click(l))
        btn.grid(row = r, column = y, sticky = "nsew", padx = 10, pady = 10)
        y += 1
    else:
        r += 1
        y = 0
        btn = ttk.Button(alphabet_frame,text=alphabet[x],font = "Fixedsys 15", bg="#E5D0AC",
                         foreground="#015551", width= 5, command=lambda l=alphabet[x]: click(l))
        btn.grid(row = r, column = y, sticky = "nsew", padx = 10, pady = 10)
        y += 1
        
    if x > 23:
        btn.grid(row = r, column = y+2, sticky = "nsew", padx = 10, pady = 10)

window.mainloop()

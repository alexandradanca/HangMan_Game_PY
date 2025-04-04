import tkinter 
from tkinter import PhotoImage
from constants import alphabet

######### Create widgets & design ######### 
###---> ROOT <---###
window = tkinter.Tk()
window.geometry('700x700')
window.title("Hangman Game")
window.configure(background="blue")
window.resizable(False,False)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)


##--> TITLE
title_frame = tkinter.Frame(window, bg="red", height=100)
title_frame.grid(row=0, column=0, sticky="ew")
title_frame.grid_propagate(False)

title = tkinter.Label(title_frame,text="HangMan Game", font=("Calibri", 10, "bold"), bg="green")
title.pack(expand=False)
window.after(1000, lambda: print(title.winfo_height()))

# -----> PARTEA DE JOC <-----
hang_game_frame = tkinter.Frame(window)
hang_game_frame.grid(row=1, column=0, sticky="nsew")

# Configurare grilă pentru hang_game_frame (2 coloane)
hang_game_frame.columnconfigure(0, weight=1)
hang_game_frame.columnconfigure(1, weight=1)
hang_game_frame.rowconfigure(0, weight=1)
hang_game_frame.rowconfigure(1, weight=1)

# -----> PRIMA COLOANĂ (VERDE) <-----
hang_frame = tkinter.Frame(hang_game_frame, bg="green", width=200, height=400)
hang_frame.grid(row=0, column=0, sticky="nsew")
hang_frame.grid_propagate(False)  # Previne redimensionarea automată

bgr = PhotoImage(file = "./hang_images/hang0.png")
img = tkinter.Label(hang_frame, image=bgr, bg="#aec1e6")
img.pack(expand=True)

# -----> A DOUA COLOANĂ (PINK + MOV) <-----
word_frame = tkinter.Frame(hang_game_frame, bg="pink", width=500, height=400)
word_frame.grid(row=0, column=1, sticky="nsew")
word_frame.grid_propagate(False)

word = tkinter.Label(word_frame,text="CUVANT", font=("Calibri", 20, "bold"))
word.pack(expand=True)

### ULTIMUL RAND
alpha_frame = tkinter.Frame(window)
alpha_frame.grid(row=2, column=0, sticky="nsew")

letters_frame = tkinter.Frame(alpha_frame, bg="purple",  width=700, height=200)
letters_frame.grid(row=1, column=0, sticky="nsew")
letters_frame.grid_propagate(False)

y = 0
r = 1
for x in range(0,26): 
    if x < 6:
        btn = tkinter.Button(letters_frame,text=alphabet[x],font=("Calibri", 15), width= 5)
        btn.grid(row = 0, column = x, sticky = "nsew", padx = 10, pady = 10)         
    elif x > 5 and y < 6:
        btn = tkinter.Button(letters_frame,text=alphabet[x],font=("Calibri", 15), width= 5)
        btn.grid(row = r, column = y, sticky = "nsew", padx = 10, pady = 10)
        y += 1
    else:
        r += 1
        y = 0
        btn = tkinter.Button(letters_frame,text=alphabet[x],font=("Calibri", 15), width= 5)
        btn.grid(row = r, column = y, sticky = "nsew", padx = 10, pady = 10)
        y += 1        

#### FUNCTIONS


######
#frame_title = tkinter.Frame(window, height=100, bg="red")
#frame_title.pack(side=tkinter.TOP, fill=tkinter.X, expand=True)

#title_label = tkinter.Label(frame_title, text="ALEXANDRA", font=("Calibri", 16, "bold"))
#title_label.grid(row=0, column=0, sticky="ew")
#frame_title.columnconfigure(0, weight=1)

###---> GAME FRAME
#frame_game = tkinter.Frame(window, bg="yellow")
#frame_game.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)

## HANG IMAGE FRAME
#bgr = PhotoImage(file = "./hang_images/hang0.png")
#w = 400
#h = 600
#frame_man = tkinter.Frame(frame_game, width=w, height=h)
#frame_man.pack(side=tkinter.LEFT)
#label = tkinter.Label(frame_man, image=bgr)
#label.place(x = w/3, y = h/3.5)

## WORD & ALPHABET FRAME
#w = 300
#h = 300
#frame_w = tkinter.Frame(frame_game, width=w,  height=h, bg="blue")
#frame_w.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)

#word_label_frame = tkinter.LabelFrame(frame_w)
#px = 20
#py = 10
#word_label_frame.grid(row=0, column=0, padx = px, pady = py)
#title_label = tkinter.Label(word_label_frame, text="ALEXANDRA", font=("Calibri", 16, "bold"))
#title_label.grid(row=0, column=0, sticky="ew")
#word_label_frame.columnconfigure(0, weight=1)
## WORD & ALPHABET FRAME
#w = 300
#h = 300
#frame_w = tkinter.Frame(frame_game, width=w,  height=h, bg="blue")
#frame_w.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

#title_label = tkinter.Label(frame_w, text="ALEXANDRA", font=("Calibri", 16, "bold"))
#title_label.grid(row=0, column=0, sticky="ew")
#frame_w.columnconfigure(0, weight=1)


#title_label = tkinter.Label(frame_game, text="_ _ _", font=("Calibri", 16, "bold"))
#title_label.grid(row=0, column=0, sticky="nsew")

window.mainloop()






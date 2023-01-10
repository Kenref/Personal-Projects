import tkinter as tk
import requests
import time
import random
import schedule


#initialize the window
root = tk.Tk()
root.title("Word of the day")
root.geometry("500x550")

#picking a random word every day
with open("words.txt") as file:
    word_list = file.read()
    word_list = word_list.split("\n")
    WORD = random.choice(word_list[:-1])



#window size
canvas = tk.Canvas()
canvas.pack()

#background image
background_image = tk.PhotoImage(file="bgimage.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

#smaller window within window (border)
display_frame = tk.Frame(root, bg="#18c8ba", bd=5)
display_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.5, anchor="n")

#getting word definition from dictionary api
data = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{WORD}?key=b08a99f6-8ab5-49e4-95f0-9235e9ef2ec5")

#pulling the definitions
jsonn = data.json()
jsonn = jsonn[0]["shortdef"]
result = ""
for indx, definition in enumerate(jsonn):
    result += f"{indx + 1}: {''.join(definition.capitalize())} \n"

#word of the day at the top
word = tk.Label(display_frame, text=WORD.title(), font="arial 30")
word.place(relx=0.5, rely=0.02, relwidth=0.97, relheight=0.3, anchor="n")

#word definition below wotd
definition = tk.Message(display_frame, text = result, font="arial 12", width="450") 
definition.place(relx=0.5, rely=0.35, relwidth=0.97, relheight=0.63, anchor="n")

#second window within window
interactive_frame = tk.Frame(root, bg="#18c8ba")
interactive_frame.place(relx=0.5, rely=0.6, relwidth=0.9, relheight=0.3, anchor="n")

#remove word button functionality
def remove_word():
    with open("words.txt", "r") as file:
        inpt = text_box.get()
        lines=file.readlines()
    with open("words.txt", "w") as file:
        for line in lines:
            if line.strip("\n") != inpt:
                file.write(line)

#remove word button
remove_button = tk.Button(interactive_frame, text="Remove", command=remove_word)
remove_button.place(relx=0.67, rely=0.1, relwidth=0.3, relheight=0.4)

#text box
text_box = tk.Entry(interactive_frame, font="arial 20")
text_box.place(relx=0.03, rely=0.1, relwidth=0.6, relheight=0.8)

#add word functionality
def add_word():
    with open("words.txt", "a") as file:
        inpt = text_box.get()
        if inpt.isalpha():
            file.write(f"{inpt.lower()}\n")

#add word button
add_button = tk.Button(interactive_frame, text="Add", command=add_word)
add_button.place(relx=0.67, rely=0.5, relwidth=0.3, relheight=0.4)






#make textbox clear when a word is added or deleted

#everyday is a random with time
# figure out how to make it send a text message every day


#find a way to check whether word is legit in the api to verify whether to add it in the words list or not


root.mainloop()
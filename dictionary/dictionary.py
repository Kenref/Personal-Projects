import tkinter as tk

HEIGHT = 500
WIDTH = 400
WORD = "word of the day"
TEXT = "pull definition from dictionary"

#initialize the window
root = tk.Tk()

#window size
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#smaller window within window (border)
display_frame = tk.Frame(root, bg="#18c8ba", bd=5)
display_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.5, anchor="n")

word = tk.Label(display_frame, text=WORD, font=50) #fix font
word.place(relx=0.5, rely=0.02, relwidth=0.97, relheight=0.3, anchor="n")

definition = tk.Message(display_frame, text=TEXT, font=50) #fix font
definition.place(relx=0.5, rely=0.35, relwidth=0.97, relheight=0.63, anchor="n")

#second window within window
interactive_frame = tk.Frame(root, bg="#18c8ba")
interactive_frame.place(relx=0.5, rely=0.6, relwidth=0.9, relheight=0.35, anchor="n")

#drop down box top left remove button top right
#textbox bottom left remove bottom right remove buttton

text_box = tk.Entry(interactive_frame, font=40)
text_box.place(relwidth=0.8, relheight=1, anchor="n")





# the text box to be placed in 0.3

# add_button = tk.Button(frame, text = "Add word")
# add_button.pack(side="bottom")

# remove_button = tk.Button(frame, text = "Remove word")
# remove_button.pack(side="bottom")dfdf

# #textbox
# textbox_add = tk.Entry(frame)
# textbox_add.pack(side="bottom")

# #textbox
# textbox_remove = tk.Entry(frame)
# textbox_remove.pack(side="bottom")dfdf










root.mainloop()
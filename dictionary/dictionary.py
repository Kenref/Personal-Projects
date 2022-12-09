import tkinter as tk

HEIGHT = 500
WIDTH = 400

#initialize the window
root = tk.Tk()

#window size
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#smaller window within window (border)
display_frame = tk.Frame(root, bg="#18c8ba")
display_frame.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.4)

word = tk.Label(display_frame, text="WOTD")
word.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.4)



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
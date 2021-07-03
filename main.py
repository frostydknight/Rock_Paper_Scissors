import tkinter as tk

#Builds window
window = tk.Tk()
window.columnconfigure(0, weight=1, minsize=250)
window.rowconfigure(0, weight=1, minsize=100)

#Creates general layout
title = tk.Label(
    master=window,
    text="Rock, Paper, Scissors!",
    font=('Arial', 25),
    padx=5,
    pady=5
).grid(
    column=0, 
    row=0, 
    padx=5, 
    pady=5
)
startGame = tk.Button(
    master=window,
    text="Start Game",
    width=15,
    height=2,
).grid(
    row=1,
    column=0,
    padx=5,
    pady=5
)
exitGame = tk.Button(
    master=window,
    text="Exit Game",
    width=15,
    height=2,
).grid(
    row=2,
    column=0,
    padx=5,
    pady=5
)

#Launches the gui
window.mainloop()

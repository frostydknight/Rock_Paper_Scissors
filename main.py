import tkinter as tk

#Builds window
window = tk.Tk()
#Creates general layout
title = tk.Label(text="Rock, Paper, Scissors!")
title.pack()

startGame = tk.Button(
    text="Start Game",
    width=25,
    height=5,
    bg="grey"
)
startGame.pack()


#Launches the gui
window.mainloop()


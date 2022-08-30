from tkinter import *
from game import game
from pygame import mixer
from levelsmessage import level
from settings import Settings
def crashed():
    win = Tk()
    win.title("crashed")
    win.geometry("1100x730")
    win.config(bg="black")
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
    win.geometry("%dx%d+0+0" % (width, height))
    bg = PhotoImage(file="crashed.gif")
    my_label = Label(win, image=bg)
    my_label.pack()

    mixer.init()
    mixer.music.load("Snake0.wav")
    mixer.music.play(-1)

    def play_again():
        win.destroy()
        game()

    def exit():
        win.destroy()

    def settings():
        win.destroy()
        Settings()

    def levels():
        win.destroy()
        level()

    x = PhotoImage(file="play again.png")
    x1 = PhotoImage(file="exit.png")
    x2 = PhotoImage(file="settings.png")
    x3 = PhotoImage(file="levels.png")

    play_again_but = Button(win, image=x, command=lambda: play_again(), borderwidth=0)
    play_again_but.place(x=600, y=490)

    exit_but = Button(win, image=x1, command=exit, borderwidth=0)
    exit_but.place(x=630, y=410)

    settings_but = Button(win, image=x2, command=settings, borderwidth=0)
    settings_but.place(x=605, y=330)

    levels_but = Button(win, image=x3, command=lambda:levels(), borderwidth=0)
    levels_but.place(x=620, y=250)

    win.mainloop()
from tkinter import *
def Settings():
    from message import crashed
    from playermode import two_player
    settings = Tk()
    settings.title("levels")
    settings.iconbitmap("icon.ico")
    settings.geometry("1100x730")
    settings.config(bg="black")
    width = settings.winfo_screenwidth()
    height = settings.winfo_screenheight()
    settings.geometry("%dx%d+0+0" % (width, height))
    bg = PhotoImage(file="settings1.png")
    my_label1 = Label(settings, image=bg)
    my_label1.pack()

    def playermode():
        settings.destroy()
        two_player()
    def back():
        settings.destroy()
        crashed()

    x = PhotoImage(file="duo.png")

    two_player_but = Button(settings, image=x, command=playermode, borderwidth=0)
    two_player_but.place(x=615, y=480)

    x1 = PhotoImage(file="back.png")

    back_but = Button(settings, image=x1, command=back, borderwidth=0)
    back_but.place(x=1200, y=20)

    settings.mainloop()
from tkinter import *
def level():
    from game import game
    from level2 import Level2
    from level3 import Level3
    from level4 import Level4
    from message import crashed

    level = Tk()
    level.title("levels")
    level.iconbitmap("icon.ico")
    level.geometry("1100x730")
    level.config(bg="black")
    width = level.winfo_screenwidth()
    height = level.winfo_screenheight()
    level.geometry("%dx%d+0+0" % (width, height))
    bg = PhotoImage(file="level.png")
    my_label1 = Label(level, image=bg)
    my_label1.pack()

    def level1():
        level.destroy()
        game()

    def level2():
        level.destroy()
        Level2()

    def level3():
        level.destroy()
        Level3()

    def level4():
        level.destroy()
        Level4()

    def back():
        level.destroy()
        crashed()

    x1 = PhotoImage(file="level1.png")

    level1_but = Button(level, image=x1, command=level1, borderwidth=0)
    level1_but.place(x=270, y=280)

    x2 = PhotoImage(file="level2.png")


    level2_but = Button(level, image=x2, command=level2, borderwidth=0)
    level2_but.place(x=270, y=630)

    x3 = PhotoImage(file="level3.png")


    level3_but = Button(level, image=x3, command=level3, borderwidth=0)
    level3_but.place(x=990, y=280)

    x4 = PhotoImage(file="level4.png")

    level4_but = Button(level, image=x4, command=level4, borderwidth=0)
    level4_but.place(x=990, y=630)

    x5 = PhotoImage(file="back.png")

    back_but = Button(level, image=x5, command=back, borderwidth=0)
    back_but.place(x=620, y=20)

    level.mainloop()
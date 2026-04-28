from tkinter import *

window = Tk()
window.geometry('600x500')
window.title("I am the parent window")

def splashscreen():
    classwindow = Toplevel(window)
    classwindow.geometry('200x100')
    classwindow.title("I am child window aka topleavel")
    classwindow.mainloop()

btn = Button(window, text='Open Splash Screen', command=splashscreen)
btn.pack()

window.mainloop()
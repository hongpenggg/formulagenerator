from tkinter import *
from tkinter.filedialog import askopenfile

window = Tk()

window.title("App")

label = Label(window, text="Hello, World.").pack()

button = Button(window, text="Click Me!").pack()

filename = askopenfile()

print(filename)

window.geometry("300x200+10+20")
window.mainloop()
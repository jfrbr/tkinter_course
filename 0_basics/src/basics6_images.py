import tkinter
from PIL import ImageTk, Image


root = tkinter.Tk()
root.title("Image Basics")
root.geometry("700x700")


my_image = tkinter.PhotoImage(Image.open("shield.png"))
my_label = tkinter.Label(root, image=my_image)
my_label.pack()

root.mainloop()
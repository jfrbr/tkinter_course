import tkinter
import os


root = tkinter.Tk()
root.title('Window Basics!')
""" img = tkinter.PhotoImage(file='/home/juan/dev/python/10-projects-python/0_basics/src/thinking.ico')
root.tk.call('wm', 'iconphoto', root._w, img) """
root.geometry('640x480')
root.resizable(False,False)
root.config(bg='blue')



top = tkinter.Toplevel()
top.title("Second window")
top.config(bg="#123456")
top.geometry("200x200+500+50")



root.mainloop()
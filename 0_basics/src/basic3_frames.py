import tkinter
from tkinter import BOTH

root = tkinter.Tk()
root.title("Frame Basics!")
root.geometry("500x500")
root.resizable(0,0)


""" name_label = tkinter.Label(root,text="Enter your name")
name_label.pack()
name_button = tkinter.Button(root, text="Submit your name")
name_button.grid(row=0, column=1) """

pack_frame = tkinter.Frame(root,bg="red")
grid_frame_1 = tkinter.Frame(root,bg="blue")
grid_frame_2 = tkinter.LabelFrame(root,text="Grid system rules!", borderwidth=5)

pack_frame.pack(fill=BOTH, expand=True)
grid_frame_1.pack(fill='x', expand=True)
grid_frame_2.pack(fill=BOTH, expand=True)


tkinter.Label(pack_frame, text='text').pack()
tkinter.Label(pack_frame, text='text').pack()
tkinter.Label(pack_frame, text='text').pack()

#Grid 1 layout
tkinter.Label(grid_frame_1, text='text').grid(row=0, column=0)
tkinter.Label(grid_frame_1, text='text').grid(row=1, column=1)
tkinter.Label(grid_frame_1, text='text').grid(row=2, column=2)
tkinter.Label(grid_frame_1, text='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').grid(row=3, column=0)


tkinter.Label(grid_frame_2, text='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').grid(row=0, column=0)
root.mainloop()
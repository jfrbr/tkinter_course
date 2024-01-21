import tkinter

root = tkinter.Tk()
root.title("Button basics!")
root.geometry("500x500")
root.resizable(0,0)


name_button = tkinter.Button(root,text="Name")
name_button.grid(row=0, column=0)

time_button=tkinter.Button(root,text="Time",bg="#00ffff")
time_button.grid(row=0,column=1)

place_button = tkinter.Button(root, text="Place", bg="#00ffff",activebackground="#ff0000")
place_button.grid(row=0, column=2, padx=10, pady=10, ipadx=15)

day_button = tkinter.Button(root, text="Day", bg="black", fg="white", borderwidth=5)
day_button.grid(row=1, column=0)

root.mainloop()
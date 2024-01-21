import tkinter

root = tkinter.Tk()
root.title("Label Basics!")
root.geometry("400x400")
root.resizable(0,0)
root.config(bg="blue")


name_label_1 = tkinter.Label(root,text="Hello, my name is Mike.")
name_label_1.pack()

name_label_2 = tkinter.Label(root,text="Hello, my name is John.", font=("Arial", 18,"bold"))
name_label_2.pack()

name_label_3 = tkinter.Label(root)
name_label_3.config(text="Hello, my name is Paul.")
name_label_3.config(font=('Cambria',10))
name_label_3.config(bg='#ff0000')
name_label_3.pack(padx=10, pady=50)

name_label_4 = tkinter.Label(root, text="Hello, my name is Sue", bg="#000000", fg="green")
name_label_4.pack(pady=(0,10), ipadx=50,ipady=10, anchor="w")

name_label_5 = tkinter.Label(root, text="Hello, my name is Pat", bg="#ffffff", fg="#123456")
name_label_5.pack(fill='both',expand=True)

root.mainloop()
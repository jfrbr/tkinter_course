import tkinter
from tkinter import BOTH, StringVar


root = tkinter.Tk()
root.title("Hello GUI World")

root.geometry("400x400")
root.resizable(0,0)

root_color = "#224870"
input_color = "#2a4494"
output_color = "#4ea5d9"

root.config(bg=root_color)

input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)

input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)


name = tkinter.Entry(input_frame, text="Enter your name",width=20)
submit_button = tkinter.Button(input_frame, text="Submit")
name.grid(row=0, column=0, padx=10, pady=10)
submit_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20)


# Create radio buttons for text display
case_style = StringVar()
case_style.set('normal')
normal_button = tkinter.Radiobutton(input_frame, text="Normal Case",variable=case_style, value='normal', bg=input_color)
upper_button = tkinter.Radiobutton(input_frame, text="Upper Case",variable=case_style, value='upper', bg=input_color)
normal_button.grid(row=1, column=0)
upper_button.grid(row=1, column=1)


root.mainloop()
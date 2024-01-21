import tkinter
from tkinter import font, StringVar, IntVar, scrolledtext, END, messagebox, filedialog
from PIL import ImageTk, Image

#Define window
root = tkinter.Tk()
root.title("Notepad")
root.geometry("600x600")
root.resizable(0,0)

#Define fonts and colors
text_color = "#fffacd"
menu_color = "#dbd9db"
root_color = "#6c809a"
root.config(bg=root_color)


#Define functions
def change_font(event):
    """ Change the given font based off dropbox options"""
    if font_options.get() == 'none':
        my_font = (font_family.get(), font_size.get())
    else:
        my_font = (font_family.get(), font_size.get(), font_options.get())

    #Change the font style
    input_text.config(font=my_font)

def new_note():
    """Create a new Note which essentially clears the screen"""
    #Use a messagebox to ask for a new note
    question = messagebox.askyesno("New Note","Are you sure you want to start a new note?")
    if question == 1:
        #ScrolledText widgets starting index is 1.0 not 0.
        input_text.delete("1.0",END)

def close_note():
    """Closes the note which essentially quits the program"""
    #Use a messagebox to ask for a new note
    question = messagebox.askyesno("Close Note","Are you sure you want to close your note?")
    if question == 1:
        root.destroy()

def save_note():
    """Save the given note. First three lines are saved as font family, font size, and font option"""
    #Use filedialog to get location and name where/what to save the file as
    save_name = filedialog.asksaveasfilename(initialdir="./", title="Save note", filetypes=(("Text Files",".txt"), ("All files", "*.*")))
    with open(save_name, 'w') as f:
        #First three lines of save file are font_family, font_size and font_options. Font_size must be a string not int.
        f.write(font_family.get() + "\n")
        f.write(str(font_size.get()) + "\n")
        f.write(font_options.get() + "\n")

        #Write remaining text in field to the file
        f.write(input_text.get("1.0", END))


def open_note():
    """Open a previously saved note. First three lines of note are font_family, font_size and font_option. First set the font, then load the text"""
    #Use file dialog to get location and directory of note file
    open_name = filedialog.askopenfilename(initialdir="./",title="Open note", filetypes=(("Text Files",".txt"), ("All files", "*.*")))
    with open(open_name, "r") as f:
        #Clear the current text 
        input_text.delete("1.0", END)

        #First three lines are font family_, font_size and font_option...You must strip the new line char at the end of each line!
        font_family.set(f.readline().strip())
        font_size.set(int(f.readline().strip()))
        font_options.set(f.readline().strip())


        #Call the change font for these .set() and pass an arbitrary value
        change_font(1)
        
        #Read the rest of the file and insert it into the text field
        text = f.read()
        input_text.insert("1.0", text)
        

#Define layout
#Define frames
menu_frame = tkinter.Frame(root, bg=menu_color)
text_frame = tkinter.Frame(root, bg=text_color)
menu_frame.pack(padx=5, pady=5)
text_frame.pack(padx=5, pady=5)

#Layout for menu frame
#Create the menu: new, open,save, close, font family, font size, font option
new_image = ImageTk.PhotoImage(Image.open('/home/juan/dev/python/10-projects-python/5_notepad/src/new.png'))
new_button = tkinter.Button(menu_frame, image=new_image,command=new_note)
new_button.grid(row=0, column=0, padx=5, pady=5)

open_image = ImageTk.PhotoImage(Image.open('/home/juan/dev/python/10-projects-python/5_notepad/src/open.png'))
open_button = tkinter.Button(menu_frame, image=open_image,command=open_note)
open_button.grid(row=0, column=1, padx=5, pady=5)

save_image = ImageTk.PhotoImage(Image.open('/home/juan/dev/python/10-projects-python/5_notepad/src/save.png'))
save_button = tkinter.Button(menu_frame, image=save_image, command=save_note)
save_button.grid(row=0, column=2, padx=5, pady=5)

close_image = ImageTk.PhotoImage(Image.open('/home/juan/dev/python/10-projects-python/5_notepad/src/close.png'))
close_button = tkinter.Button(menu_frame, image=close_image, command=close_note)
close_button.grid(row=0, column=3, padx=5, pady=5)

#Create a list of fonts to use
families = font.families()
font_family = StringVar()
font_family_drop = tkinter.OptionMenu(menu_frame, font_family, *families, command=change_font)
font_family.set('Tahoma')
#Set the width so it will fit "times new roman" and remain constant
font_family_drop.config(width=16)
font_family_drop.grid(row=0, column=4, padx=5, pady=5)
#for font in fonts:
#    print(font)

sizes = [8,10,12,14,16,20,24,32,48,64,72,96]
font_size = IntVar()
font_size_drop = tkinter.OptionMenu(menu_frame, font_size, *sizes, command=change_font)
font_size.set(12)
#Set width to be constant even if its 8.
font_size_drop.config(width=2)
font_size_drop.grid(row=0, column=5, padx=5, pady=5)

options = ['none', 'bold', 'italic']
font_options = StringVar()
font_options_drop = tkinter.OptionMenu(menu_frame, font_options, *options, command=change_font)
font_options.set('none')
font_options_drop.config(width=5)
font_options_drop.grid(row=0, column=6, padx=5, pady=5)

#Layout for the text frame

my_font = (font_family.get(), font_size.get())

#Create input_text as a scrolltext so you can scroll trough the text field
#Set default width and height to be more than the window size so that on the smallest text size, the text field size is constant
input_text = tkinter.scrolledtext.ScrolledText(text_frame, width=1000, height=1000, bg=text_color, font=my_font)
input_text.pack()

#Run the root window
root.mainloop()

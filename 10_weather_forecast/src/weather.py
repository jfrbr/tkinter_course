#Weather Forecast 

import tkinter
from tkinter import BOTH

#Define window

root = tkinter.Tk()
root.title("Weather Forecast")
root.geometry("400x400")
root.resizable(0,0)


#Define fonts and colors
sky_color = "#76c3ef"
grass_color = "#aad207"
output_color = "#dcf0fb"
input_color = "#ecf2ae"
large_font = ('SimSun',14)
small_font = ('SimSun',10)

#Define functions


#Define layout

#Create frames

sky_frame = tkinter.Frame(root, bg=sky_color, height=250)
grass_frame = tkinter.Frame(root, bg=grass_color)
sky_frame.pack(fill=BOTH, expand=True)
grass_frame.pack(fill=BOTH, expand=True)

output_frame = tkinter.LabelFrame(sky_frame, bg=output_color, width=225, height=225)
input_frame = tkinter.LabelFrame(grass_frame, bg=input_color, width=325)
output_frame.pack(pady=30)
input_frame.pack(pady=15)


#Run root window's main loop
root.mainloop()
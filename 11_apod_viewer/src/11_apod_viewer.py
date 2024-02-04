import tkinter, requests, webbrowser
from tkcalendar import DateEntry
from PIL import ImageTk, Image
from io import BytesIO
from tkinter import filedialog

#Define window

root = tkinter.Tk()
root.title("APOD Photo Viewer")

#Define fonts and colors
text_font = ('Times New Roman', 14)
nasa_blue = "#043c93"
nasa_light_blue = "#7aa5d3"
nasa_red = "#ff1923"
nasa_white = "#ffffff"



root.config(bg=nasa_blue)



#Define functions
def get_request():
    """Get request data from NASA APOD API"""
    global response

    #Set the parameters for the request
    url = "https://api.nasa.gov/planetary/apod"
    api_key = "1ytXjgTRJ5HTcqNqtoACMKzqtU5FUarebIqsn1nK"
    date = calendar.get_date()
    print(date)

    querystring = {"api_key":api_key, "date":date}
    
    #Call the request and turn it into a python usable format
    response = requests.request("GET", url, params=querystring)
    response = response.json()

    print(response)
    set_info()

def set_info():
    """Update output labels based on API Call"""
    #Example response
    '''{'date': '2024-02-04', 
    'explanation': "Stars are forming in the gigantic dust pillar called the Cone Nebula. Cones, pillars, and majestic flowing shapes abound in stellar nurseries where natal clouds of gas and dust are buffeted by energetic winds from newborn stars. The Cone Nebula, a well-known example, lies within the bright galactic star-forming region NGC 2264. The Cone was captured in unprecedented detail in this close-up composite of several observations from the Earth-orbiting Hubble Space Telescope. While the Cone Nebula, about 2,500 light-years away in Monoceros, is around 7 light-years long, the region pictured here surrounding the cone's blunted head is a mere 2.5 light-years across. In our neck of the galaxy that distance is just over half way from our Sun to its nearest stellar neighbors in the Alpha Centauri star system. The massive star NGC 2264 IRS, seen by Hubble's infrared camera in 1997, is the likely source of the wind sculpting the Cone Nebula and lies off the top of the image. The Cone Nebula's reddish veil is produced by dust and glowing hydrogen gas.", 
    'hdurl': 'https://apod.nasa.gov/apod/image/2402/cone_hubbleschmidt_4048.jpg', 
    'media_type': 'image', 
    'service_version': 'v1', 
    'title': 'The Cone Nebula from Hubble', 
    'url': 'https://apod.nasa.gov/apod/image/2402/cone_hubbleschmidt_960.jpg'}'''

    #Update the picture date and explanation

    picture_date.config(text=response['date'])
    picture_explanation.config(text=response['explanation'])

    #We need to use 3 images in other functions: an img, a thum and a full_img
    global img
    global thumb
    global full_img


    url = response['url']


    if response['media_type'] == 'image':
        img_response = requests.get(url, stream=True)
        img_data = img_response.content
        img = Image.open(BytesIO(img_data))

        full_img = ImageTk.PhotoImage(img)

        #Create the thumbnail for the main screen
        thumb_data = img_response.content
        thumb = Image.open(BytesIO(thumb_data))
        thumb.thumbnail((200,200))
        thumb = ImageTk.PhotoImage(thumb)

        #Set the thumbnail image
        picture_label.config(image=thumb)
    elif response['media_type']=='video':
        
        picture_label.config(text=url, image="")

        webbrowser.open(url)

def full_photo():
    """Open the full size photo in a new window"""
    top = tkinter.Toplevel()
    top.title("Full APOD Photo")
    
    #Load the full image in the new window
    img_label = tkinter.Label(top, image=full_img)
    img_label.pack()

def save_photo():
    """Save the desired photo"""
    save_name = filedialog.asksaveasfilename(initialdir="./", title="Save image", filetypes=(("JPEG","*.jpg"), ("All Files", "*")))
    img.save(save_name + ".jpg")


#Define layout
#Create frames
input_frame = tkinter.Frame(root, bg=nasa_blue)
output_frame = tkinter.Frame(root, bg=nasa_white)
input_frame.pack()
output_frame.pack(padx=50, pady=(0,25))

#Layout for the input frame
calendar = DateEntry(input_frame, width=10, font=text_font, background=nasa_blue, foreground=nasa_white)
submit_button = tkinter.Button(input_frame, text="Submit", font=text_font, bg=nasa_light_blue, command=get_request)
full_button = tkinter.Button(input_frame, text="Full Photo", font=text_font, bg=nasa_light_blue, command=full_photo)
save_button = tkinter.Button(input_frame, text="Save Photo", font=text_font, bg=nasa_light_blue, command=save_photo)
quit_button = tkinter.Button(input_frame, text="Exit", font=text_font, bg=nasa_red, command=root.destroy)

calendar.grid(row=0, column=0, padx=5, pady=10)
submit_button.grid(row=0, column=1, padx=5, pady=10,ipadx=35)
full_button.grid(row=0, column=2, padx=5, pady=10,ipadx=25)
save_button.grid(row=0, column=3, padx=5, pady=10, ipadx=25 )
quit_button.grid(row=0, column=4, padx=5, pady=10, ipadx=50)


#Layout for the output frame
picture_date = tkinter.Label(output_frame,  font=text_font, bg=nasa_white)
picture_explanation = tkinter.Label(output_frame, font=text_font, bg=nasa_white,wraplength=600)
picture_label = tkinter.Label(output_frame)


picture_date.grid(row=1, column=1, pady=10)
picture_explanation.grid(row=0, column=0, padx=10, pady=10, rowspan=2)
picture_label.grid(row=0, column=1, padx=10, pady=10)


#Get today's photo to start with
get_request()


#Run the root window's main loop
root.mainloop()
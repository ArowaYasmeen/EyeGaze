from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

# creating tkinter window 
root = Tk()
root.title("HCI Project")
root.geometry("850x400")
# Adding widgets to the root window 
#Label(root, text='HCI Project', font=('Verdana', 15))

# Creating a photoimage object to use image 
photo1 = ImageTk.PhotoImage(Image.open("ImagesPy/img1a.PNG"))
photo2 = ImageTk.PhotoImage(Image.open("ImagesPy/img1b.PNG"))
photo3 = ImageTk.PhotoImage(Image.open("ImagesPy/img2a.PNG"))
photo4 = ImageTk.PhotoImage(Image.open("ImagesPy/img2b.PNG"))
photo5 = ImageTk.PhotoImage(Image.open("ImagesPy/img3a.PNG"))
photo6 = ImageTk.PhotoImage(Image.open("ImagesPy/img3b.PNG"))

# here, image option is used to 
# set image on button 
Button1=Button(root, text='Click Me !', image=photo1)
Button2=Button(root, text='Click Me !', image=photo3)
Button3=Button(root, text='Click Me !', image=photo5)

#Label.grid(row =0, column=1)
Button1.grid(row=3, column=0)
Button2.grid(row=3, column=1)
Button3.grid(row=3, column=2)

def button_hover1(e):
    Button1.config(image=photo2)
    Button1.image=photo2

def button_leave1(e):
    Button1.config(image=photo1)
    Button1.image = photo1

def button_hover2(e):
    Button2.config(image=photo4)
    Button2.image=photo4

def button_leave2(e):
    Button2.config(image=photo3)
    Button2.image = photo3

def button_hover3(e):
    Button3.config(image=photo6)
    Button3.image=photo6

def button_leave3(e):
    Button3.config(image=photo5)
    Button3.image = photo5


Button1.bind("<Enter>",button_hover1)
Button1.bind("<Leave>",button_leave1)
Button2.bind("<Enter>",button_hover2)
Button2.bind("<Leave>",button_leave2)
Button3.bind("<Enter>",button_hover3)
Button3.bind("<Leave>",button_leave3)

mainloop() 
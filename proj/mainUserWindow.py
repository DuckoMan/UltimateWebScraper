from tkinter import *
from PIL import Image, ImageTk
import math
import random

import main_vendor

window=Tk()
window.title("Web Scraper")
window.minsize(500 , 500)
window.resizable(True,True)

def scrap():
    url = enterLink.get()
    tag = enterTag.get()
    className = enterClass.get()
    resault = main_vendor.scrapElement(url, tag, className)
    print(resault)
    output.config(text = resault)

mainWindTttle = Label(window, text = "WEB scraping", font = ( "Arial",25,"bold" ), fg = "black")
mainWindTttle.pack(padx = 50,pady = 5)

link_inputTitle = Label(window, text = "Link to scrap", font = ( "Arial",20,"bold" ), fg = "black")
link_inputTitle.pack(padx = 50, pady = 15)
enterLink=Entry(window, font = ("Arial",20,))
enterLink.pack(padx = 50, pady = 0)

tag_inputTitle = Label(window, text = "tag in wich scraping target is", font = ( "Arial",20,"bold" ), fg = "black")
tag_inputTitle.pack(padx = 50, pady = 15)
enterTag=Entry(window , font = ("Arial",20,))
enterTag.pack(padx = 50, pady = 0)

class_inputTitle = Label(window, text = "class of this tag", font = ( "Arial",20,"bold" ), fg = "black")
class_inputTitle.pack(padx = 50, pady = 15)
enterClass=Entry(window, font=("Arial",20,))
enterClass.pack(padx = 50, pady = 0)

btn = Button(window, command = scrap )
btn.config(text="Scrap" , background="white", foreground="black", font="30",width="40", height="2",
        activebackground="#696969", activeforeground="white",highlightcolor="#C0C0C0", border="2 px solid black")
btn.pack(side=BOTTOM, pady=20)

label5 = Label(window, text="Resault:", font=( "Arial",25,"bold" ), fg="black")
label5.pack(padx=50)

output=Label(window, font=( "Arial",24,"bold" ), fg="gray")
output.pack(padx=50)
window.mainloop()



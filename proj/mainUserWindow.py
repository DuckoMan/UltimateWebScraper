from tkinter import *
from PIL import Image, ImageTk
import math
import random

import main_vendor

#Window settings
window=Tk()
window.title("Web Scraper")
window.minsize(500 , 500)
window.resizable(True,True)

def scrap(): # reacts on button click
    #Getting values from the inputs
    url = enterLink.get()
    tag = enterTag.get()
    className = enterClass.get()
    #Using our vendor to scrap and putting it into output tab
    resault = main_vendor.scrapElement(url, tag, className)
    outputText.config(text = resault)

#Interface settings
mainWindTttle = Label(window, text = "WEB scraping", font = ( "Arial",25,"bold" ), fg = "black") #window heading and its display settings
mainWindTttle.pack(padx = 50,pady = 5)

link_inputTitle = Label(window, text = "Link to scrap", font = ( "Arial",20,"bold" ), fg = "black")#input heading and its settings
link_inputTitle.pack(padx = 50, pady = 15)
enterLink=Entry(window, font = ("Arial",20,))#actual input and its display settings
enterLink.pack(padx = 50, pady = 0)

tag_inputTitle = Label(window, text = "tag in wich scraping target is", font = ( "Arial",20,"bold" ), fg = "black")
tag_inputTitle.pack(padx = 50, pady = 15)
enterTag=Entry(window , font = ("Arial",20,))
enterTag.pack(padx = 50, pady = 0)

class_inputTitle = Label(window, text = "class of this tag", font = ( "Arial",20,"bold" ), fg = "black")
class_inputTitle.pack(padx = 50, pady = 15)
enterClass=Entry(window, font=("Arial",20,))
enterClass.pack(padx = 50, pady = 0)

#Button settngs
btn = Button(window, command = scrap )
btn.config(text="Scrap" , background="white", foreground="black", font="30",width="40", height="2",
        activebackground="#696969", activeforeground="white",highlightcolor="#C0C0C0", border="2 px solid black")
btn.pack(side=BOTTOM, pady=20)

#Resault output
resaultHeading = Label(window, text="Resault:", font=( "Arial",25,"bold" ), fg="black")
resaultHeading.pack(padx=50)

outputText=Label(window, font=( "Arial",24,"bold" ), fg="gray")
outputText.pack(padx=50)

window.mainloop()



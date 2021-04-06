from tkinter import *
from tkcalendar import *

Vs = str("     ")                                                       #Frequently Used: 5 Spaces as a string
defFont = ("Arial", "22")                                               #Frequently Used: Default Font

root = Tk()
root.minsize(640,480)
root.maxsize(1280,1024)                                                 #Maximum size not explicitly needed

#module 1 - Title
title = Label(text="Reservation System Manager v.A", font=(defFont))    #specs for said string
title.grid(row=0,column=1,sticky="w")                                   #positional arguments; "w" means west; NSEW and can use NW & SE

#module 2 - First Name Entry
FN = Label(text="First Name:" + Vs, font=(defFont))                     #~: Sets up the actual text
FN.grid(row=2, column=1, sticky="w")                                    #~~: positional arguments

FN_entry = Entry(bd=6, width=25)                                        #~~~: Creates the entry box next to it
FN_entry.grid(row=2, column=2, sticky="w")                              #~~~~: positional arguments; ".grid()" always indicates this.

#module 3 - Last Name Entry
LN = Label(text="Last Name: ", font =(defFont))
LN.grid(row=3, column=1, sticky="w")

LN_entry = Entry(bd=6, width=25)
LN_entry.grid(row=3, column=2, sticky="w")

#module 4 - Starting Date Entry
SD = Label(text="Starting Date:" + Vs,font=(defFont))
SD.grid(row=4, column=1, sticky="w")

SD_calendar = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)   #visual arguments
SD_calendar.grid(row=4, column=2, sticky="w")

#module 5 - Ending Date Entry
ED = Label(text="Ending Date:" + Vs, font=(defFont))
ED.grid(row=5, column=1, sticky="w")

ED_calendar = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)   #visual arguments
ED_calendar.grid(row=5, column=2, sticky="w")


root.mainloop() #Calls the mainloop of TK, per the description
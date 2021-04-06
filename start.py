from tkinter import *
from tkcalendar import *

Vs = str("     ")                                                       #Frequently Used: 5 Spaces as a string
defFont = ("Arial", "22")                                               #Frequently Used: Default Font

root = Tk()
root.minsize(640,480)
root.maxsize(1280,1024)                                                 #Maximum size not explicitly needed
root.title("Reservations Manager v.A")
variable = StringVar()

#module 1 - First Name Entry
FN = Label(text="First Name:" + Vs, font=(defFont)).grid(row=2, column=0, sticky="w")

FN_entry = Entry(bd=6, width=15).grid(row=2, column=1, sticky="w")

#module 2 - Last Name Entry
LN = Label(text="Last Name: ", font =(defFont)).grid(row=3, column=0, sticky="w")

LN_entry = Entry(bd=6, width=15).grid(row=3, column=1, sticky="w")

#module 3 - Starting Date Entry
SD = Label(text="Reservation Date:" + Vs,font=(defFont)).grid(row=4, column=0, sticky="w")

TimeChoiceMenu = OptionMenu(root,variable,"start of day","end of day").grid(row=4,column=2,sticky="w")

SD_calendar = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2).grid(row=4, column=1, sticky="w") #borderwidth adds shadow to the box

#module 4 - Ending Date Entry
DueBy = Label(text="Due by", font=(defFont)).grid(row=5, column=0, sticky="w")

variable.set("Select a time...")
TimeChoiceMenu2 = OptionMenu(root,variable,"start of day","end of day").grid(row=5,column=2,sticky="w")

ED_calendar = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2).grid(row=5, column=1, sticky="w")

root.mainloop() #Calls the mainloop of TK, per the description
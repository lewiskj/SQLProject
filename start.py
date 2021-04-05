from tkinter import *
root = Tk()
root.minsize(640,480)
root.maxsize(1280,1024) #Maximum size not explicitly needed

#module 1
var = StringVar()                                                               #Sets internal variable for this module, a label, as a string.
titleLabel = Label(root, textvariable=var, relief=FLAT, font=("Arial", "22"))   #specs for said string
var.set("Reservation System Manager v.A")                                       #the text itself
titleLabel.grid(row=0,column=0,sticky="w")                                                      #I believe this prints it to the window

#module 2
L1 = Label(text="\n"*2 + "User Name" + " "*5)
L1.grid(row=2, column=0, sticky="w")
E1 = Entry(bd=6)
E1.grid(row=3, column=0, sticky="w")

root.mainloop() #Calls the mainloop of TK, per the description
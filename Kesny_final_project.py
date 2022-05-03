from tkinter import *


mainWindow = Tk()
#mainWindow.configure(bg = "#68A7AD")

#adjut the file from the page
mainWindow.geometry("600x400")
#name title
mainWindow.title("The Cake ordering app")

title=Label(mainWindow, text="The Cake Ordering App", font="times 25 bold")
title.grid(row=0, column=6)

#name label
name_label = Label(mainWindow, text="Customer Name: ")
name_label.grid(row=2, column=5)


#name for user to enter
name_entry = Entry(mainWindow, width=30)
name_entry.grid(row=2, column=6)


#phone label
phone_label = Label(mainWindow, text="Phone Number: ")
phone_label.grid(row=3, column=5)

#phone for user to enter
phone_entry = Entry(mainWindow, width=30)
phone_entry.grid(row=3, column=6)

#address label
address_label = Label(mainWindow, text="Address: ")
address_label.grid(row=4, column=5)

#addressfor user to enter
address_entry = Entry(mainWindow, width=30)
address_entry.grid(row=4, column=6)

#-----menu secton ----

menu=Label(mainWindow, text="Menu", font="times 18 bold")
menu.grid(row=6, column=5)

label1=Label(mainWindow, text="Small Cake             $25 ")
label1.grid(row=7, column=5)

label2=Label(mainWindow, text="Medium Cake         $35 ")
label2.grid(row=8, column=5)

label3=Label(mainWindow, text="Large Cake             $45 ")
label3.grid(row=9, column=5)

label4=Label(mainWindow, text="Cupcake                 $1.5 ")
label4.grid(row=10, column=5)

#------Billing section------

qty=Label(mainWindow, text="Qty", font="times 18 bold")
qty.grid(row=6, column=6)

e1=Entry(mainWindow, width= 5)
e1.grid(row=7, column=6)

e2=Entry(mainWindow, width= 5)
e2.grid(row=8, column=6)

e3=Entry(mainWindow, width= 5)
e3.grid(row=9, column=6)

e4=Entry(mainWindow, width= 5)
e4.grid(row=10, column=6)

flavors=Label(mainWindow, text="Flavors", font="times 18 bold")
flavors.grid(row=6, column=7)

#radio button
response = StringVar()
response.set(" ")
radio1 = Radiobutton(mainWindow, text="Chololate", variable = response, value ="chololate")
radio1.grid(row=7, column=7)
radio2 = Radiobutton(mainWindow, text="Strawberry", variable = response, value ="strawberry")
radio2.grid(row=8, column=7)
radio3 = Radiobutton(mainWindow, text="Red Velvet", variable = response, value ="redvelvet")
radio3.grid(row=9, column=7)
radio4 = Radiobutton(mainWindow, text="Vanilla", variable = response, value ="vanilla")
radio4.grid(row=10, column=7)


mainWindow.mainloop()
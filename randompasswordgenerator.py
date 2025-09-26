import random
from tkinter import *
from tkinter import messagebox

def password_generate():
    try:
        length=int(length_entry.get())
    except:
        messagebox.showerror(message="Please enter the required inputs")
        return
    
    #since,the returned value is list we convert it into String using join
    password=random.choices(character_string, k=length)  
    password=''.join(password)
    password="Created password is:"+str(password)

    #assign the password to declared string variable 
    password_v.set(password) 
    password_label=Entry(password_gen,bd=0,bg="gray",textvariable=password_v,state="readonly") 
    password_label.place(x=10,y=140,height=50,width=320)

#Define a string which contains letters,digits,special characters
character_string="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+?/.|"
#Defining the user interface
password_gen=Tk()
password_gen.geometry("450x300")
password_gen.title("Random Password Generator")

#Title of the appliaction
title_label=Label(password_gen,text="Random Password Generator",font=('Ubuntu Mono',12))
title_label.pack()

#Read Length of the password
length_label=Label(password_gen,text="Enter length of password")
length_label.place(x=20,y=30)
length_entry=Entry(password_gen,width=3)
length_entry.place(x=190,y=30)

#output
password_v=StringVar()
password_label=Entry(password_gen,bd=0,bg="gray",textvariable=password_v,state="readonly")
password_label.place(x=10,y=140,height=50,width=320)

#Generate password
password_button=Button(password_gen,text="Generate Password",command=password_generate)
password_button.place(x=100,y=100)

#Exit the app
password_gen.mainloop()

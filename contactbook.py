from tkinter import *
from tkinter import messagebox
#Initialization of window
root=Tk()
root.geometry('600x600')
root.config(bg='#d3f3f5')
root.title('Contact Book')
root.resizable(0,0)
contactlist=[
    ['Manisha','1234567890','Mani@gmail.com','Hyderabad'],
    ['Sunny','2345615630','Sunny@gmail.com','Siddipet'],
    ['Ravi','9723445189','Ravi@gmail.com','Warangal'],
    ['vignesh','7654391027','Vignesh@gmail.com','Nizambad'],
    ['Trisha','9845367209','Trisha@gmail.com','Vizag'],
    ['Sirisha','8764530986','Sirisha@gmail.com','Hyderabad'],
    ['Varsha','7665890442','Varsha@gmail.com','Bangalore']

]
Name=StringVar()
Number=StringVar()
Email=StringVar()
Address=StringVar()
#creation of frame
frame=Frame(root)
frame.pack(side=RIGHT)
scroll=Scrollbar(frame,orient=VERTICAL)
select=Listbox(frame,yscrollcommand=scroll.set,font=('Times new roman',12))
scroll.config(command=select.yview)
scroll.pack(side=RIGHT,fill=Y)
select.pack(side=LEFT,fill=BOTH,expand=1)

#scelecting Value
def Selected():
    print("Hello",len(select.curselection()))
    if len(select.curselection())==0:
        messagebox.showerror("Error","Please Select the Name")
    else:
        return int(select.curselection()[0])
#Add new contact
def AddContact():
    if Name.get()!="" and Number.get()!="" and Email.get()!="" and Address.get():
        contactlist.append([Name.get(),Number.get(),Email.get(),Address.get()])
        print(contactlist)        
        Select_set()
        EntryReset()
        messagebox.showinfo("Confiramation:,Successfully added new contact")
    else:
        messagebox.showinfo("Error","Please fill the information")    
#Edit existing contact
def UpdateContact():
    if Name.get() and Number.get() and Email.get and Address.get():
        contactlist[Selected()]=[Name.get(),Number.get(),Email.get(),Address.set()] 

        messagebox.showinfo("Confirmation","updated contact")
        EntryReset()
        Select_set()
    elif not(Name.get()) and not (Number.get()) and not (Email.get()) and not (Address.get()):
        messagebox.showerror("Error","Please select the name and edit")
    else:
        message1="""To Load all information of \n
                 selected row press Load button\n.
                 """
        messagebox.showerror("Error",message1)
def EntryReset():
    Name.set('')
    Number.set('')
    Email.set('')
    Address.set('')
#Delete selected contact
def Delete_Contact():
    if len(select.curselection())!=0:
        result=messagebox.askyesno('Confirmation','Do You want to delete the selected contact') 
        if result==True:
            del contactlist[Selected()] 
            Select_set()
    else:
        messagebox.showerror("Error","Please select the contact to delete")

#view contact
def View():
    NAME,PHONE,EMAIL,ADDRESS=contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
    Email.set(EMAIL)
    Address.set(ADDRESS)
def Exit():
    root.destroy()

def Select_set():
    contactlist.sort()
    select.delete(0,END)
    for NAME,PHONE,EMAIL,ADDRESS in contactlist:
        select.insert(END,NAME) 
Select_set()

#Define button labels and entry widget
Label(root,text='Name',font=("Times new roman",12,"bold"),bg='#d3f3f5').pack(pady=5)
Entry(root,textvariable=Name,width=40).pack()
Label(root,text='Contact No.',font=("Times new roman",12,"bold"),bg='#d3f3f5').pack(pady=5)
Entry(root,textvariable=Number,width=40).pack()
Label(root,text='Email',font=("Times new roman",12,"bold"),bg='#d3f3f5').pack(pady=5)
Entry(root,textvariable=Email,width=40).pack()
Label(root,text='Address',font=("Times new roman",12,"bold"),bg='#d3f3f5').pack(pady=5)
Entry(root,textvariable=Address,width=40).pack()
Button(root,text="ADD",font='Helvetica 10 bold',bg="#bb3247",command=AddContact).pack(pady=3)
Button(root,text="Edit",font='Helvetica 10 bold',bg="#bb3247",command=UpdateContact).pack(pady=3)
Button(root,text="Delete",font='Helvetica 10 bold',bg='#bb3247',command=Delete_Contact).pack(pady=3)
Button(root,text="VIEW",font='Helvetica 10 bold',bg='#bb3247',command=View).pack(pady=3)
Button(root,text="RESET",font='Helvetica 10 bold',bg='#bb3247',command=EntryReset).pack(pady=3)
Button(root,text="EXIT",font='Helvetica 10 bold',bg='red',command=Exit).pack(pady=3)

root.mainloop()

from tkinter import *
ob = Tk()
ob.configure(bg="white")
ob.geometry("1536x864")
def login():
    username = t1.get()
    password = t2.get()

    if username=="admin" and password == "123":
        l3 = Label(text="Login Successful", font=20)
        l3.place(x=650, y=550)
    else :
        l4 = Label(text="Login Failed", font=20)
        l4.place(x=650, y=550)


ob.title("HOSPITAL LOGIN")
l1 = Label(text="WELCOME TO THE LOGIN PAGE" ,font=30).place(x=600,y=80)

l1 = Label(text = "Username",font=20)
l1.place(x=600,y=250)

t1 = Entry()
t1.place(x=750,y=250)
l2 = Label(text = "Password",font=20)
l2.place(x=600,y=350)
t2 = Entry(show="*")
t2.place(x=750,y=350)
b = Button(text = "Login",font=20,command=login)
b.place(x=695,y= 450)
ob.mainloop()
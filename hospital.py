from tkinter import *
import pandas as pd
ob = Tk()
ob.configure(bg="white")
ob.geometry("1536x864")
def add():
   
    patient = Tk()
    patient.title("Add Patient")
    patient.geometry("800x500")
    l6 = Label(patient,text="Patient ID",font=20)
    l6.place(x=100,y=50)
    t3=  Entry(patient)
    t3.place(x=300,y=50)

    l7 = Label(patient,text="Name",font=20)
    l7.place(x=100,y=100)
    t4 = Entry(patient)
    t4.place(x=300,y=100)

    l8 = Label(patient,text="Age",font=20)
    l8.place(x=100,y=150)
    t5 = Entry(patient)
    t5.place(x=300,y=150)

    l9 = Label(patient,text="Gender",font=20)
    l9.place(x=100,y=200)
    t6 = Entry(patient)
    t6.place(x=300,y=200)

    l10 = Label(patient,text="Disease",font=20)
    l10.place(x=100,y=250)
    t7 = Entry(patient)
    t7.place(x=300,y=250)

    l11 = Label(patient,text="Contact No",font=20)
    l11.place(x=100,y=300)
    t8 = Entry(patient)
    t8.place(x=300,y=300)

    def save():
       patientid = t3.get()
       name = t4.get()
       age = t5.get()
       gender = t6.get()
       disease = t7.get()
       contactno= t8.get()
       data = {
        "Patient ID" :[patientid],
        "Name" : [name],
        "Age" : [age],
        "Gender" : [gender],
        "Disease" : [disease],
        "Contactno": [contactno]
         }
       new_df=pd.DataFrame(data)
      
       try:
           old_df = pd.read_excel("patients.xlsx")
           df = pd.concat([old_df,new_df],ignore_index=True)
           
       except:
           df = new_df; 
       df.to_excel("patients.xlsx",index=False)   
    b5 = Button(patient,text="Save",font=20,command=save)
    b5.place(x=300,y=380)
    patient.mainloop()


def search():

    s = Tk()
    s.geometry("800x400")
    s.title("Search Patient Window")

    l12 = Label(s,text="ENTER PATIENT ID",font=20)
    l12.place(x=100,y=100)

    t9 = Entry(s)
    t9.place(x=350,y=100)

    def find():

        pid = t9.get()

        df = pd.read_excel("patients.xlsx")

        result = df[df["Patient ID"].astype(str) == pid]

        if len(result) > 0:

           l13 = Label(s,text="Patient Found",font=20)
           l13.place(x=250,y=250)

           l14 = Label(s,text=str(result))
           l14.place(x=100,y=300)

        else:

            l15 = Label(s,text="Patient Not Found",font=20)
            l15.place(x=250,y=250)

    b6 = Button(s,text="Find",font=20,command=find)
    b6.place(x=300,y=200)

    s.mainloop()


def analytics():

    df = pd.read_excel("patients.xlsx")

    total = len(df)

    a = Tk()
    a.geometry("500x300")

    Label(a,text="TOTAL PATIENTS = "+str(total),
          font=20).place(x=50,y=100)

    a.mainloop()




def login():
    username = t1.get()
    password = t2.get()
    if username=="admin" and password == "123":
        l3 = Label(text="Login Successful", font=20)
        l3.place(x=650, y=550)
        ob.destroy()
        dash = Tk()
        dash.configure(bg="white")
        dash.title("dashboard")
        dash.geometry("1536x864")
        l5 = Label(text = "DASHBOARD",font=80).place(x=700,y=80)
        b2 =Button(text = "Add Patient",font= 20,command=add)
        b2.place(x=700,y=250) 
        b3 =Button(text = "Search Patient",font= 20,command = search)
        b3.place(x=700,y=350)
        b4 =Button(text = "Analytics",font= 20,command = analytics)
        b4.place(x=700,y=450) 
        dash.mainloop()


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
b1 = Button(text = "Login",font=20,command=login)
b1.place(x=695,y= 450)
ob.mainloop()
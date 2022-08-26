from tkinter import *
from tkinter import messagebox as mb
import random, string
from tkinter import ttk
from datetime import *

open("user.txt", "a+")
open("usernames.txt", "a+")
open("passenger.txt", "a+")
open("trains.txt","a+")
open("destination.txt","a+")
today = datetime.today()

username = ""
def mainpage():
    global username
    def signin():
        f = open("user.txt", "r")
        r = f.readlines()
        for j in range(len(r)):
            r[j] = r[j].strip()
        def delete_train():
            delete=Tk()
            train_delete=StringVar(delete)
            delete.configure(bg="papaya whip")
            delete.title("Delete Train(ADMIN)")
            Label(delete,text="Enter the name of the train you want to delete",font=("times new roman",15),bg="papaya whip").pack()
            Entry(delete,bg="Light Grey",width=50,textvariable=train_delete,font=("times new roman",15,"bold")).pack()
            def e():
                y = open("trains.txt","r")
                f = y.readlines()
                for i in range(len(f)):
                    f[i]=f[i].strip()
                if train_delete.get()=="":
                    mb.showerror("","All fields are necessary")
                    delete.destroy()
                    delete_train()
                elif train_delete.get() not in f:
                    mb.showerror("Error","Train does not exist")
                    delete.destroy()
                    delete_train()
                else:
                    f.remove(train_delete.get())
                    x = open("trains.txt","w")
                    for i in f:
                        print(i,file=x)
                    mb.showinfo("SUCCESS","Train removed")
                    y.close()
                    x.close()
            Button(delete,text="Submit",bg="blue",fg="white",command=e).pack()

        def add():
            train_add=Tk()
            train = StringVar(train_add)
            train_add.configure(bg="papaya whip")
            train_add.title("Add Train(ADMIN)")
            Label(train_add,text="Please Enter the train's name",font=("Times new roman",15),bg="papaya whip").pack()
            Entry(train_add,bg="light grey",width=50,textvariable=train,font=("Times new roman",15,"bold")).pack()
            def add_train():
                o = open("trains.txt", "r")
                l = o.readlines()
                for i in range(len(l)):
                    l[i] = l[i].strip()
                if train.get()=="":
                    mb.showerror("","All feilds are necessary!")
                    train_add.destroy()
                    add()

                elif train.get() in l:
                    mb.showerror("","Train already exists")
                    train_add.destroy()
                    o.close()
                    add()
                else:
                    l.append(train.get())
                    p = open("trains.txt","w")
                    for i in l:
                            print(i, file=p)
                    p.close()
                    mb.showinfo("SUCCESS",(train.get()," was added!"))
                    train_add.destroy()
            Button(train_add,text="Submit",bg="blue",fg="white",command=add_train).pack()

        def add1():
            destadd = Tk()
            dest = StringVar(destadd)
            destadd.configure(bg="papaya whip")
            destadd.title("Add More Destinations")
            Label(destadd,text="Enter the Destination you want to add",bg="papaya whip",font=("Times new roman",15)).pack()
            Entry(destadd,font=("Times new roman",15),width=50,bg="Light grey",textvariable=dest).pack()
            def ap():
                y = open("destination.txt","r")
                q = y.readlines()
                for i in range(len(q)):
                    q[i]=q[i].strip()
                if dest.get()=="":
                    mb.showerror("","All feilds are necessary")
                    destadd.destroy()
                    add1()
                elif dest.get() in q:
                    mb.showerror("","Destination already present")
                    destadd.destroy()
                    add1()
                else:
                    q.append(dest.get())
                    h = open("destination.txt","w")
                    for i in q:
                        print(i,file=h)
                    h.close()
                    mb.showinfo("SUCCESS",(dest.get()," was successfully added!"))
                    destadd.destroy()
                y.close()

            Button(destadd,text="Submit",fg="white",bg="blue",command=ap).pack()
        if username.get()=="admin" and password.get()=="admin":
            admin = Tk()
            admin.configure(bg="papaya whip")
            admin.title("admin")
            Label(admin,text="Welcome to ADMIN Page!",font=("Times new roman",25,"bold"),bg="papaya whip").pack()
            Button(admin,text = "Add more trains",bg="blue",fg="white",command=add).pack()
            Button(admin,text="Add more destinations",bg="blue",fg="white",command=add1).pack()
            Button(admin,text="Delete Trains",bg="blue",fg="white",command=delete_train).pack()
            root.destroy()
            mainpage()
        elif username.get()=="" and password.get()=="":
            mb.showerror('',"All feilds are necessary!")
            root.destroy()
            mainpage()
        elif str((username.get(), password.get())) not in r:
            mb.showerror("", "Please Check the Entered Details")
            root.destroy()
            mainpage()
        else:
            root.destroy()
            user = Tk()
            user.title("Dashboard")
            user.configure(bg="Papaya Whip")
            Label(user, text="Train Booking Services", font=("Times New Roman", 25, "bold"), bg="papaya Whip").grid(row=0,
                                                                                                                column=2)
            msg = "Welcome", username.get(), "!"
            Label(user, text=msg, font=("Times new Roman", 15), bg="papaya whip").grid(row=2, column=0)


        def logout():
            mainpage()
            exit()


        def checkpnr():
            pnrpage = Tk()
            pnr = StringVar(pnrpage)
            name = StringVar(pnrpage)
            dob = StringVar(pnrpage)
            f = open("trains.txt", "r")
            t = f.readlines()
            for i in range(len(t)):
                t[i] = t[i].strip()
            w = open("destination.txt", "r")
            a1 = w.readlines()
            for i in range(len(a1)):
                a1[i] = a1[i].strip()
            pnrpage.title("Check PNR Status")
            pnrpage.configure(bg="papaya whip")
            Label(pnrpage, text="Please Provide the following details", font=("Times new Roman", 15),
                  bg="papaya whip").grid(row=0, column=0)
            Label(pnrpage, text="Please Enter your name", font=("Times new Roman", 15), bg="papaya whip").grid(row=2,
                                                                                                               column=0)
            Entry(pnrpage, width=50, textvariable=name, bg="light grey", font=("Times new Roman", 15)).grid(row=3,
                                                                                                            column=0)
            Label(pnrpage, text="Please Enter your 6 digit PNR number", bg="papaya whip",
                  font=("Times new Roman", 15)).grid(row=4, column=0)
            Entry(pnrpage, width=50, textvariable=pnr, bg="light grey", font=("Times new Roman", 15)).grid(row=5,
                                                                                                           column=0)
            Label(pnrpage, text="Date of Travel DD-MM-YYYY format", bg="papaya whip", font=("Times new Roman", 15)).grid(
                row=6, column=0)
            Entry(pnrpage, width=50, textvariable=dob, bg="light grey", font=("Times new Roman", 15)).grid(row=7,
                                                                                                           column=0)
            Label(pnrpage, text="Enter the train name: ", bg="papaya whip", font=("Times new roman", 15)).grid(row=8,
                                                                                                               column=0)
            n = StringVar(pnrpage)
            trainsel = ttk.Combobox(pnrpage, width=27, textvariable=n)
            trainsel['values'] = t
            trainsel.grid(row=8, column=1)
            Label(pnrpage, text="Select Your Starting Station: ", font=("Times new Roman", 15), bg="Papaya whip").grid(
                row=9, column=0)
            m = StringVar(pnrpage)
            startsel = ttk.Combobox(pnrpage, width=27, textvariable=m)
            startsel['values'] = a1
            startsel.grid(row=9, column=1)
            Label(pnrpage, text="Select Your Destination Station: ", font=("Times new Roman", 15),
                  bg="Papaya whip").grid(row=10, column=0)
            o = StringVar(pnrpage)
            endsel = ttk.Combobox(pnrpage, width=27, textvariable=o)
            endsel['values'] = a1
            endsel.grid(row=10, column=1)

            def read():
                f = open("passenger.txt", "r")
                e = f.readlines()
                for i in range(len(e)):
                    e[i] = e[i].strip()
                if pnr.get()=="" and name.get()=="" and dob.get()=="":
                    mb.showerror("","All feilds are necessary!")
                    pnrpage.destroy()
                    checkpnr()
                elif len(pnr.get())!=6:
                    mb.showerror("","Please Enter a  6 digit PNR number ")
                    pnrpage.destroy()
                    checkpnr()
                    
                elif str((username.get(),name.get(), pnr.get(), dob.get(), n.get(), m.get(), o.get())) not in e:
                    mb.showerror("Not Found", "Please check the entered details")
                    pnrpage.destroy()
                    checkpnr()
                else:
                    mb.showinfo("",
                            "The status of your booking is confirmed.Please Board Your train on time to avoid delays in schedule")

                f.close()

            Button(pnrpage, text="Submit", bg="blue", fg="White", command=read).grid(row=11, column=5)

        Button(user, text="Check Your PNR status", bg="blue", fg="white", command=checkpnr).grid(row=50, column=0)

        def booknew():
            ticket = Tk()
            name_new = StringVar(ticket)
            dot_new = StringVar(ticket)
            train_new = StringVar(ticket)
            start = StringVar(ticket)
            end = StringVar(ticket)
            f = open("trains.txt","r")
            t = f.readlines()
            for i in range(len(t)):
                t[i]=t[i].strip()
            w = open("destination.txt","r")
            a1 = w.readlines()
            for i in range(len(a1)):
                a1[i]=a1[i].strip()
            ticket.title("Book a New ticket")
            ticket.configure(bg='papaya whip')
            Label(ticket, text="Please provide the following details", font=("Times new roman", 15),
                  bg="papaya whip").grid(row=0, column=0)
            Label(ticket, text="Please Enter your name", font=("Times new roman", 15), bg="papaya whip").grid(row=1,
                                                                                                              column=0)
            Entry(ticket, font=("Times new roman", 15), bg="Light grey", textvariable=name_new, width=50).grid(row=2,
                                                                                                               column=0)
            Label(ticket, text="Please Enter your Date of Travel DD-MM-YYYY format", font=("Times new roman", 15),
                  bg="papaya whip").grid(row=3, column=0)
            Entry(ticket, font=("Times new roman", 15), bg="Light grey", textvariable=dot_new, width=50).grid(row=4,
                                                                                                              column=0)
            Label(ticket, text="Enter the train you would like to travel in", font=("Times new roman", 15),
                  bg="papaya whip").grid(row=5, column=0)
            trainsel_new = ttk.Combobox(ticket, textvariable=train_new)
            trainsel_new.grid(row=5, column=2)
            trainsel_new['values'] = t
            Label(ticket, text="Please Enter the starting station", font=("Times new roman", 15),
                  bg="papaya whip").grid(row=6, column=0)
            start_new = ttk.Combobox(ticket, textvariable=start)
            start_new.grid(row=6, column=2)
            start_new['values'] = a1
            Label(ticket, text="Please Enter your destination station", font=("Times new roman", 15),
                  bg="papaya whip").grid(row=7, column=0)
            end_new = ttk.Combobox(ticket, textvariable=end)
            end_new.grid(row=7, column=2)
            end_new['values'] = a1
            pnrnum = random.randint(100000, 999999)

            def d():
                f = open("passenger.txt", "a")
                if name_new.get()=="" and dot_new.get()=="" and train_new.get()==""and start.get()=="" and end.get()=="":
                    mb.showerror("","All feilds are necessary!")
                    ticket.destroy()
                    booknew()
                elif start.get()==end.get():
                    mb.showerror("Invaid","You Cannot Book a ticket the same Destination as Starting station!")
                    ticket.destroy()
                    booknew()

                else:
                    print((username.get(),name_new.get(), str(pnrnum), dot_new.get(), train_new.get(), start.get(), end.get()), file=f)
                    mb.showinfo("SUCCESS", ("Your Ticket has been confirmed. Your 6 Digit PNR number is ", str(pnrnum)))
                    ticket.destroy()

                f.close()

            Button(ticket, text="Submit", fg="White", bg="blue", command=d).grid(row=10, column=5)

        Button(user, text="Book New Ticket", bg="Blue", fg="white", command=booknew).grid(row=50, column=2)

        def cancel():
            tc = Tk()
            tc.configure(bg="papaya whip")
            tc.title("Cancel Ticket")
            f = open("trains.txt", "r")
            t = f.readlines()
            for i in range(len(t)):
                t[i] = t[i].strip()
            w = open("destination.txt", "r")
            a1 = w.readlines()
            for i in range(len(a1)):
                a1[i] = a1[i].strip()
            name_cancel = StringVar(tc)
            dot_cancel = StringVar(tc)
            pnr_cancel = StringVar(tc)
            train_cancel = StringVar(tc)
            start_cancel = StringVar(tc)
            end_cancel = StringVar(tc)
            Label(tc,text="Please provide the following details",bg="papaya whip",font=("Times new roman",15)).grid(row=0,column=0)
            Label(tc,text="Please Enter your name",bg="papaya whip",font=("Times new roman",15)).grid(row=1,column=0)
            Entry(tc,bg="Light grey",font=("Times new roman",15),width=50,textvariable=name_cancel).grid(row=2,column=0)
            Label(tc,text="Enter Your 6 Digit PNR number",bg="Papaya whip",font=("Times new roman",15)).grid(row=3,column=0)
            Entry(tc,bg="Light grey",font=("Times new roman",15),width=50,textvariable=pnr_cancel).grid(row=4,column=0)
            Label(tc,text="Please Enter your Date of Travel DD-MM-YYYY Format",font=("Times new roman",15),bg="papaya whip").grid(row=5,column=0)
            Entry(tc,bg="Light grey",font=("Times new roman",15),width=50,textvariable=dot_cancel).grid(row=6,column=0)
            Label(tc,text="Name of the Train in which you are booked",bg="Papaya whip",font=("Times new roman",15)).grid(row=7,column=0)
            Train = ttk.Combobox(tc,textvariable=train_cancel)
            Train.grid(row=7,column=2)
            Train['values']=t
            Label(tc,text="Enter the starting station",font=("Times new roman",15),bg="papaya Whip").grid(row=8,column=0)
            Start = ttk.Combobox(tc,textvariable=start_cancel)
            Start.grid(row=8,column=2)
            Start['values']=a1
            Label(tc,text="Enter your Destination Station",bg="papaya whip",font=("Times new roman",15)).grid(row=9,column=0)
            End=ttk.Combobox(tc,textvariable=end_cancel)
            End.grid(row=9,column=2)
            End['values']=a1
            w.close()
            f.close()
            def q():
                f = open("passenger.txt", "r")
                rd = f.readlines()
                for i in range(len(rd)):
                    rd[i]=rd[i].strip()
                if name_cancel.get()=="" and dot_cancel.get()=="" and pnr_cancel.get()=="" and train_cancel.get()=="" and start_cancel.get()=="" and end_cancel.get()=="":
                    tc.destroy()
                    mb.showerror('',"All feilds are necessary")
                    cancel()
                elif len(pnr_cancel.get())!=6:
                    mb.showerror("","Please Enter a 6 digit PNR Number")
                    tc.destroy()
                    cancel()
                elif str((username.get(), name_cancel.get(), pnr_cancel.get(), dot_cancel.get(), train_cancel.get(), start_cancel.get(), end_cancel.get())) not in rd:
                    mb.showerror("Not found","Ticket Details not found.Please Check the entered details")
                    tc.destroy()
                    cancel()
                else:
                    rd.remove(str((username.get(), name_cancel.get(), pnr_cancel.get(), dot_cancel.get(), train_cancel.get(), start_cancel.get(), end_cancel.get())))
                    f.close()
                    g = open("passenger.txt","w")
                    for i in rd:
                        print(i,file=g)
                    g.close()
                    mb.showinfo("Sucess","Your Ticket was cancelled successfully")
                    tc.destroy()

            Button(tc, text="Submit", fg="white", bg="blue", command=q).grid(row=10, column=5)
        Button(user,text="Cancel Ticket",bg="Blue",fg="white",command=cancel).grid(row=50,column=3)
        Button(user,text="Logout",bg="blue",fg="white",command=logout).grid(row=0,column=50)






    def sign_up():

        page = Tk()
        page.configure(bg="papaya whip")
        username_new = StringVar(page)
        password_new = StringVar(page)
        password_reconfirm = StringVar(page)
        page.title("Sign up")
        Label(page, text="Create a New User name", font=("Times New roman", 15, "bold"), width=50,
              bg="papaya whip").grid(row=0, column=0)
        Entry(page, bg="Light Grey", width=50, textvariable=username_new, font=("arial", 15, "bold"),
              borderwidth=3).grid(row=1, column=0)
        Label(page, text="Create a New Password", font=("Times New roman", 15, "bold"), width=50,
              bg="papaya whip").grid(row=2, column=0)
        Entry(page, show="*", bg="Light Grey", width=50, textvariable=password_new, font=("arial", 15, "bold"),
              borderwidth=3).grid(row=3, column=0)
        Label(page, text="Reconfirm your New Password", font=("Times New roman", 15, "bold"), width=50,
              bg="papaya whip").grid(row=4, column=0)
        Entry(page, show="*", bg="Light Grey", width=50, textvariable=password_reconfirm, font=("arial", 15, "bold"),
              borderwidth=3).grid(row=5, column=0)

        def c():
            q = open("usernames.txt", "r")
            rd = q.read()
            if username_new.get()=="" and password_new.get()=="" and password_reconfirm.get()=="":
                mb.showerror("","All feilds are necessary!")
                page.destroy()
                sign_up()
            elif username_new.get() in rd:
                mb.showerror("", "Username Already taken.Please try another username")
                page.destroy()
                sign_up()
            elif password_new.get() != password_reconfirm.get():
                mb.showerror("ERROR", "The passwords are not matching please re-enter")
                page.destroy()
                sign_up()
            else:
                p = open("user.txt", "a")
                d = (username_new.get(), password_new.get())
                q = open("usernames.txt", "a")
                print(username_new.get(), file=q)
                q.close()
                print(d, file=p)
                p.close()
                mb.showinfo("SUCCESS", ("Your Username is ", username_new.get(), "Please login in the main login page"))
                page.destroy()

        Button(page, text="Submit", command=c, bg="blue", fg="white").grid(row=6, column=0)

    root = Tk()
    username = StringVar(root)
    password = StringVar(root)
    root.title("Railway Reservation System")
    root.configure(bg="papaya whip")
    Heading = Label(root, text="RAILWAY RESERVATION SYSTEM", font=("Times new roman", 23, "bold"), bg="papaya whip")
    Heading.grid(row=0, column=0)
    Label(root, text="Username", font=("Times New roman", 15, "bold"), width=10, bg="papaya whip").grid(row=10,
                                                                                                        column=0,
                                                                                                        padx=10,
                                                                                                        pady=10)
    username_entry = Entry(root, bg="Light Grey", width=50, textvariable=username, font=("Arial", 15, "bold"),
                           borderwidth=3).grid(row=11, column=0)

    Label(root, text="Password", font=("Times New roman", 15, "bold"), bg="papaya whip").grid(row=12, column=0)
    password_Entry = Entry(root, show="*", bg="Light Grey", width=50, font=("arial", 15, "bold"), textvariable=password,
                           borderwidth=3).grid(row=14, column=0)
    New_user_button = Button(root, text="Click Here to Sign up", command=sign_up, bg="blue", fg="white").grid(row=18,
                                                                                                              column=0)
    Sign_in = Button(root, text="Sign In", command=signin, bg="blue", fg="white").grid(row=16, column=0)


mainpage()
mainloop()


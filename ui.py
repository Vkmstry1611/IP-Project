# =============================== Importing Packages ========================================
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import numpy as np
import mysql.connector as sql   
import random
import matplotlib.pyplot as plt
# =============================== Connecting Database ========================================

db = sql.connect(
    host="localhost",
    user="root",
    password="root",
    database="db")

print(db)

cursor = db.cursor()

# =============================== Home ========================================

def home():
    
    clear()


    Label(frame,text="Welcome to Flight Reservation System ",font=('Calibri',20)).place(x=250,y=10)
    
    bookingdetails_button=Button(frame,text="View Booking Details",width=30,height=2,padx=3,pady=3,command=bookingdetails).place(x=350,y=100)
    
    flight_schedule_button=Button(frame,text="View Flight Schedules",width=30,height=2,command=flightschedule,padx=3,pady=3).place(x=350,y=150)
    
    button=Button(frame,text="Book Seats",width=30,height=2,command=bookseats,padx=3,pady=3).place(x=350,y=200)
    
    button2=Button(frame,text="Customer Management",width=30,height=2,command=cust_mangement,padx=3,pady=3).place(x=350,y=250)
    
    button3=Button(frame,text="View Graphs",width=30,height=2,command=graph,padx=3,pady=3).place(x=350,y=300)
    
    button4=Button(frame,text="Exit",width=30,height=2,command=ui.destroy,padx=3,pady=3).place(x=350,y=350)


# =============================== Clear Frame ========================================
def clear():
 
    for widgets in frame.winfo_children():
        widgets.destroy()
    
    Button(frame,text="Home",height=2,command=home).grid(padx=5,pady=5,sticky="NW")


# =============================== Selecting Flight Csv ========================================
def select_flight():
    global flight
    global df
    global save_csv
    if flight=="1" or flight=="flight1":
        flight="flight1"
        df = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight1.csv", index_col=0)
        def save_csv():
            df.to_csv(path_or_buf="D:/Study/12th/Project/IP/Practical/IP-Project/flight1.csv",sep=',')
    elif flight=="2" or flight=="flight2":
        flight="flight2"
        df = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight2.csv", index_col=0)
        def save_csv():
            df.to_csv(path_or_buf="D:/Study/12th/Project/IP/Practical/IP-Project/flight2.csv",sep=',')
        
    elif flight=="3" or flight=="flight3":
        flight="flight3"
        df = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight3.csv", index_col=0)
        def save_csv():
            df.to_csv(path_or_buf="D:/Study/12th/Project/IP/Practical/IP-Project/flight3.csv",sep=',')
    elif flight=="4" or flight=="flight4":
        flight="flight4"
        df = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight4.csv", index_col=0)
        def save_csv():
            df.to_csv(path_or_buf="D:/Study/12th/Project/IP/Practical/IP-Project/flight4.csv",sep=',')
    elif flight=="5" or flight=="flight5":
        flight="flight5"
        df = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight5.csv", index_col=0)
        def save_csv():
            df.to_csv(path_or_buf="D:/Study/12th/Project/IP/Practical/IP-Project/flight5.csv",sep=',')
    

# ===================================== Booking Details ====================================

def bookingdetails():
    clear()
    
    
    Label(frame,text="Enter Phone Number : ",font=('Calibri',15)).place(x=350,y=150)
    phone_entry=Entry(frame,width=25,font=('Calibri',12))
    phone_entry.place(x=350,y=200)

    def check_int(input):
        if len(input)>10:
            return False
        elif input.isdigit() or input=="":
            return True
        else:
            return False

    check=frame.register(check_int)
    phone_entry.config(validate="key", validatecommand=(check, '%P'))

    
    cursor.execute("select phone from customer_details")
    result=cursor.fetchall()
    phone_lst=[]
    for i in result:
        for j in i:
            phone_lst.append(j)
    
    
    def check_phone():
        global phone
        var = IntVar()
        button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
        button.place(x=375,y=250)
        button.wait_variable(var)
        phone=int(phone_entry.get())

    check_phone()
    while phone not in phone_lst:
        messagebox.showinfo("Invalid Phone Number","Phone Number Doesn't Exist in Database")
        check_phone()

    
    clear()

    cursor.execute("select * from customer_details where phone={}".format(phone))
    result=cursor.fetchall()

    for i in result:
        result=i
    cust_id=result[0]
    name=result[1]
    email=result[3]
    Label(frame,text="Name : \t\t\t {}".format(name),font=('Calibri',13)).place(x=250,y=10)
    Label(frame,text="Phone Number : \t\t {}".format(phone),font=('Calibri',13)).place(x=250,y=35)
    Label(frame,text="Email : \t\t\t {}".format(email),font=('Calibri',13)).place(x=250,y=60)
    cursor.execute("select * from booking_details where cust_id={}".format(cust_id))
    result=cursor.fetchall()


    lst=[]
    for i in result:
        lst.append(list(i))
    for i in lst:
        i.pop(0)
        row=i[2]
        col=i[3]
        i.pop(2)
        i.pop(2)
        i.insert(2,"{}{}".format(col,row))

    
    columns = ("Ticket Number",'Booking Date', 'Seat',"Flight Number")
        
    tree = ttk.Treeview(frame,columns=columns,show='headings')
    tree.heading("Ticket Number",text="Ticket Number")
    tree.heading('Booking Date', text='Booking Date')
    tree.heading('Seat', text='Seat')
    tree.heading('Flight Number', text='Flight Number')
    for i in lst:
        tree.insert("",END,values=i)

    scrollbar=Scrollbar(frame,command=tree.yview) 
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.place(x=860,y=255)
    tree.place(x=45,y=125)


# ===================================== Flight Schedule ====================================

def flightschedule():
    clear()

    cursor.execute("select * from flight_details")
    result = cursor.fetchall()
    
    columns = ("Flight",'To', 'From')
        
    tree = ttk.Treeview(frame,columns=columns,show='headings')
    tree.heading("Flight",text="Flight")
    tree.heading('To', text='To')
    tree.heading('From', text='From')
    for i in result:
        tree.insert("",END,values=i)

    scrollbar=Scrollbar(frame,command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.place(x=755,y=180)
    tree.place(x=150,y=100)
 

# ===================================== Book Seats ====================================

    
def bookseats():
    global flight           
    clear()
    
    flightschedule()
    
    lst_flight=["1","2","3","4","5","flight1","flight2","flight3","flight4","flight5"]
    
    Label(frame,text="Enter Flight Number : ",font=('Calibri',11)).place(x=370,y=330)
    flightno_entry=Entry(frame,width=25,font=('Calibri',12))
    flightno_entry.place(x=370,y=350)

    def check_flight():
        global flight
        var = IntVar()
        button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
        button.place(x=400,y=385)
        button.wait_variable(var)
        flight=flightno_entry.get()
    
    check_flight()
    while flight not in lst_flight:
        messagebox.showinfo("Invalid Input","Enter '1','2','3','4' or '5' as Flight Number"  )
        check_flight()
    
    select_flight()
    clear()
    Label(frame,text="Select Seats",font=('Calibri',14)).place(x=400,y=35)

    
    l1 = ["A", "B", "C", "D", "E", "F"]
    
    canvas = Canvas(frame,width=250,height=300)
    scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas,width=300,height=300)
    scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.place(x=340,y=100)
    scrollbar.place(x=560,y=250)
    def book(row,col):
        clear()
        tic = random.randint(10000000, 99999999)
        
        cursor.execute("select ticket_no from booking_details")
        result=cursor.fetchall()
        lst=[]
        for i in result:
            for j in i:
                lst.append(j)
        while tic in lst:
            tic = random.randint(10000000, 99999999)
        
        Label(frame,text="Your Ticket Number is :    {} \n".format(tic),font=('Calibri',11)).place(x=350,y=100)
        Label(frame,text="Enter Phone Number :",font=('Calibri',11)).place(x=375,y=130)
        phone_entry=Entry(frame,font=('Calibri',11),width=25)
        phone_entry.place(x=370,y=150)

        def check_int(input):
            if len(input)>10:
                return False
            elif input.isdigit() or input=="":
                return True
            else:
                return False

        check=frame.register(check_int)
        phone_entry.config(validate="key", validatecommand=(check, '%P'))

        

        
        var = IntVar()
        button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
        button.place(x=385,y=175)
        button.wait_variable(var)
        phone=int(phone_entry.get())

        
        cursor.execute("select phone from customer_details")
        result=cursor.fetchall()
        phone_lst=[]
        for i in result:
            for j in i:
                phone_lst.append(j)
        if phone in phone_lst:
            pass
        else:
            clear()
            Label(frame,text="Enter Name :",font=('Calibri',11)).place(x=375,y=150)
            name_entry=Entry(frame,font=('Calibri',11),width=25)
            name_entry.place(x=370,y=175)
            Label(frame,text="Enter Email :",font=('Calibri',11)).place(x=375,y=225)
            email_entry=Entry(frame,font=('Calibri',11),width=25)
            email_entry.place(x=370,y=250)
            

            cursor.execute("select email from customer_details")
            result=cursor.fetchall()
            email_lst=[]
            for i in result:
                for j in i:
                    email_lst.append(j)

            def check_email():
                global email
                global name
                var = IntVar()
                button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
                button.place(x=385,y=350)
                button.wait_variable(var)
                name=name_entry.get()
                email=email_entry.get()
                

            check_email()
            while email in email_lst or name=="" or email=="":
                messagebox.showinfo("Invalid Input","Email Exists in Database or Column is Empty")
                check_email()

        cursor.execute("insert into customer_details(name,phone,email) values('{}',{},'{}')".format(name,phone,email))
        db.commit()
       
        cursor.execute("select cust_id from customer_details where phone={} ".format(phone))
        result=cursor.fetchall()
        for i in result:
            for j in i:
                cust_id=j
        cursor.execute("insert into booking_details values({},{},curdate(),{},'{}','{}')".format(cust_id,tic,row,col,flight))
        db.commit()
        df.loc[row, col] = "X"
        save_csv()
        

        messagebox.showinfo('Success',"Seat Booked Successfully")
        home()
        
    
    for row in range(1,31):
        for col in l1:
            if col=="F":
                b=Button(scrollable_frame,text="{}{}".format(col,row),command= lambda row=row,col=col:book(row,col))
                b.grid(column=l1.index(col)+1,row=row,padx=2,pady=2)
                if df.loc[row,col]=="X":
                    b.configure(bg="orangered",state=DISABLED)
                else:
                    b.configure(bg="springgreen")
            else:
                b=Button(scrollable_frame,text="{}{}".format(col,row),command= lambda row=row,col=col:book(row,col))
                b.grid(column=l1.index(col)+1,row=row,padx=2,pady=2)
                if df.loc[row,col]=="X":
                    b.configure(bg="orangered",state=DISABLED)
                else:
                    b.configure(bg="springgreen")
    col=col.upper()


# ===================================== Customer Management ====================================

def cust_mangement():
    clear()

    Button(frame,text="Display all Customer Records",width=30,height=2,command=display_records).place(x=350,y=100)
    Button(frame,text="Update Customer Record",width=30,height=2,command=update_cust).place(x=350,y=200)
    Button(frame,text="Search Customer Record",width=30,height=2,command=search_cust).place(x=350,y=150)
    Button(frame,text="Cancel Customer Booking",width=30,height=2,command=cancel_booking).place(x=350,y=250)
    Button(frame,text="Add Customer Record",width=30,height=2,command=add_cust).place(x=350,y=300)

    # ===================================== Display Records ====================================

def display_records():
    clear()

    cursor.execute("select * from customer_details")
    result = cursor.fetchall()
    
    columns = ("Customer Id",'Name', 'Phone', 'Email')
    
    tree = ttk.Treeview(frame,columns=columns,show='headings')

    tree.heading("Customer Id",text="Customer Id")
    tree.heading('Name', text='First Name')
    tree.heading('Phone', text='Phone')
    tree.heading('Email', text='Email')

    for i in result:
        tree.insert("",END,values=i)
   

    scrollbar=Scrollbar(frame,command=tree.yview,orient=VERTICAL)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.place(x=860,y=190)

    tree.place(x=50,y=100)

        # ===================================== Search Customer ====================================
def search_cust():

        # ===================================== Search Name ====================================

    def search_name():
        clear()

        Label(frame,text="Enter Name : ",font=('Calibri',15)).place(x=350,y=150)
        name_entry=Entry(frame,width=25,font=('Calibri',12))
        name_entry.place(x=350,y=200)


        var = IntVar()
        button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
        button.place(x=375,y=250)
        button.wait_variable(var)
        name=name_entry.get()
        clear()

        cursor.execute('select * from customer_details where name like "%{}%"'.format(name))
        result = cursor.fetchall()
            
        columns = ("Customer Id",'Name', 'Phone', 'Email')
        
        tree = ttk.Treeview(frame,columns=columns,show='headings')

        tree.heading("Customer Id",text="Customer Id")
        tree.heading('Name', text='First Name')
        tree.heading('Phone', text='Phone')
        tree.heading('Email', text='Email')

        for i in result:
            tree.insert("",END,values=i)
    
        scrollbar=Scrollbar(frame,command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=860,y=190)

        tree.place(x=50,y=100)
        
        # ===================================== Search Phone ====================================

    def search_phone():

        clear()
        
        Label(frame,text="Enter Phone : ",font=('Calibri',15)).place(x=350,y=150)
        phone_entry=Entry(frame,width=25,font=('Calibri',12))
        phone_entry.place(x=350,y=200)

        def check_int(input):
            if len(input)>10:
             return False
            elif input.isdigit() or input=="":
                return True
            else:
             return False
        check=frame.register(check_int)
        phone_entry.config(validate="key", validatecommand=(check, '%P'))

        var = IntVar()
        button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
        button.place(x=375,y=250)
        button.wait_variable(var)
        phone=int(phone_entry.get())
            
        clear()
        
        cursor.execute('select * from customer_details where phone like "%{}%"'.format(phone))
        result = cursor.fetchall()
            
        columns = ("Customer Id",'Name', 'Phone', 'Email')
        
        tree = ttk.Treeview(frame,columns=columns,show='headings')

        tree.heading("Customer Id",text="Customer Id")
        tree.heading('Name', text='First Name')
        tree.heading('Phone', text='Phone')
        tree.heading('Email', text='Email')

        for i in result:
            tree.insert("",END,values=i)
        
        scrollbar=Scrollbar(frame,command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=860,y=190)


        tree.place(x=50,y=100)


        # ===================================== Search Email ====================================

    def search_email():
        clear()

        Label(frame,text="Enter Email : ",font=('Calibri',15)).place(x=350,y=150)
        email_entry=Entry(frame,width=25,font=('Calibri',12))
        email_entry.place(x=350,y=200)

        var = IntVar()
        button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
        button.place(x=375,y=250)
        button.wait_variable(var)
        email=email_entry.get()
        
        clear()
        
        cursor.execute('select * from customer_details where email like "%{}%"'.format(email))
        result = cursor.fetchall()
            
        columns = ("Customer Id",'Name', 'Phone', 'Email')
        
        tree = ttk.Treeview(frame,columns=columns,show='headings')

        tree.heading("Customer Id",text="Customer Id")
        tree.heading('Name', text='First Name')
        tree.heading('Phone', text='Phone')
        tree.heading('Email', text='Email')

        for i in result:
            tree.insert("",END,values=i)
    
        scrollbar=Scrollbar(frame,command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=860,y=190)

        tree.place(x=50,y=100)


    clear()
    Button(frame,text="Search By Name",width=30,height=2,command=search_name).place(x=350,y=150)
    Button(frame,text="Search By Phone",width=30,height=2,command=search_phone).place(x=350,y=200)
    Button(frame,text="Search By Email",width=30,height=2,command=search_email).place(x=350,y=250)


        # ===================================== Add Customer Record ====================================

def add_cust():
    clear()

    Label(frame,text="Enter Phone Number :",font=('Calibri',11)).place(x=375,y=130)
    phone_entry=Entry(frame,font=('Calibri',11),width=25)
    phone_entry.place(x=370,y=150)

    def check_int(input):
        if len(input)>10:
            return False
        elif input.isdigit() or input=="":
            return True
        else:
            return False
    
    check=frame.register(check_int)
    phone_entry.config(validate="key", validatecommand=(check, '%P'))      

    Label(frame,text="Enter Name :",font=('Calibri',11)).place(x=375,y=205)
    name_entry=Entry(frame,font=('Calibri',11),width=25)
    name_entry.place(x=370,y=225)

    Label(frame,text="Enter Email :",font=('Calibri',11)).place(x=375,y=280)
    email_entry=Entry(frame,font=('Calibri',11),width=25)
    email_entry.place(x=370,y=300)

    cursor.execute("select phone,email from customer_details")
    result=cursor.fetchall()
    lst=[]
    for i in result:
        for j in i:
            lst.append(j)



    def check_data():
        global phone
        global email
        var = IntVar()
        button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
        button.place(x=375,y=325)
        button.wait_variable(var)
        phone=int(phone_entry.get())
        name=name_entry.get()
        email=email_entry.get()

    check_data()
    while phone or email in lst or len(phone)!=10:
        messagebox.showinfo("Invalid Data","Similar Data Exists in Database or Invalid Input")
        check_data()
    

    cursor.execute("insert into customer_details (name,phone,email) values('{}',{},'{}')".format(name,phone,email))
    db.commit()
    messagebox.showinfo("Success","Details Added Successfully")

    home()

    # ===================================== Update Customer Record ====================================
def update_cust():
    clear()
    
        # ===================================== Update Name ====================================

    def update_name():
        clear()

        Label(frame,text="Enter Phone Number : ",font=('Calibri',15)).place(x=350,y=150)
        phone_entry=Entry(frame,width=25,font=('Calibri',12))
        phone_entry.place(x=350,y=200)

        def check_int(input):
            if len(input)>10:
                return False
            elif input.isdigit() or input=="":
                return True
            else:
                return False
    
        check=frame.register(check_int)
        phone_entry.config(validate="key", validatecommand=(check, '%P'))      

        cursor.execute("select phone from customer_details")
        result=cursor.fetchall()
        phone_lst=[]
        for i in result:
            for j in i:
                phone_lst.append(j)
        
        
        def check_phone():
            global phone
            var = IntVar()
            button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
            button.place(x=375,y=250)
            button.wait_variable(var)
            phone=int(phone_entry.get())

        check_phone()
        while phone not in phone_lst:
            messagebox.showinfo("Invalid Phone Number","Phone Number Doesn't Exist in Database")
            check_phone()

        clear()

        Label(frame,text="Enter Updated Name :",font=('Calibri',15)).place(x=350,y=150)
        name_entry=Entry(frame,width=25,font=('Calibri',12))
        name_entry.place(x=350,y=200)

        var = IntVar()
        button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
        button.place(x=375,y=250)
        button.wait_variable(var) 
        name=name_entry.get()

        cursor.execute("update customer_details set name='{}' where phone={}".format(name, phone))
        db.commit()

        messagebox.showinfo("Success","Details Updated Successfully")

        home()

        # ===================================== Update Phone ====================================
    def update_phone():
        clear()
        
        Label(frame,text="Enter Email : ",font=('Calibri',15)).place(x=350,y=150)
        email_entry=Entry(frame,width=25,font=('Calibri',12))
        email_entry.place(x=350,y=200)

        cursor.execute("select email from customer_details")
        result=cursor.fetchall()
        email_lst=[]
        for i in result:
            for j in i:
                email_lst.append(j)

        def check_email():
            global email
            var = IntVar()
            button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
            button.place(x=375,y=250)
            button.wait_variable(var)
            email=email_entry.get()
            

        check_email()
        while email not in email_lst:
            messagebox.showinfo("Invalid Email","Email Doesn't Exist in Database")
            check_email()

        clear()

        Label(frame,text="Enter Updated Phone :",font=('Calibri',15)).place(x=350,y=150)
        phone_entry=Entry(frame,width=25,font=('Calibri',12))
        phone_entry.place(x=350,y=200)

        def check_int(input):
            if len(input)>10:
                return False
            elif input.isdigit() or input=="":
                return True
            else:
                return False

        check=frame.register(check_int)
        phone_entry.config(validate="key", validatecommand=(check, '%P'))

        cursor.execute("select phone from customer_details")
        result=cursor.fetchall()
        phone_lst=[]
        for i in result:
            for j in i:
                phone_lst.append(j)
        
        
        def check_phone():
            global phone
            var = IntVar()
            button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
            button.place(x=375,y=250)
            button.wait_variable(var)
            phone=int(phone_entry.get())

        check_phone()
        while phone or email in lst or len(phone)!=10:
            messagebox.showinfo("Invalid Data","Similar Data Exists in Database or Phone Number is less than 10 digits ")
            check_phone()
    

        cursor.execute("update customer_details set phone='{}' where email={}".format(phone,email))
        db.commit()

        messagebox.showinfo("Success","Details Updated Successfully")
        
        home()
   
       # ===================================== Update Email ====================================
    def update_email():
        clear()

        Label(frame,text="Enter Phone Number : ",font=('Calibri',15)).place(x=350,y=150)
        phone_entry=Entry(frame,width=25,font=('Calibri',12))
        phone_entry.place(x=350,y=200)

        def check_int(input):
            if len(input)>10:
                return False
            elif input.isdigit() or input=="":
                return True
            else:
                return False

        check=frame.register(check_int)
        phone_entry.config(validate="key", validatecommand=(check, '%P'))        

        cursor.execute("select phone from customer_details")
        result=cursor.fetchall()
        phone_lst=[]
        for i in result:
            for j in i:
                phone_lst.append(j)
        
        
        def check_phone():
            global phone
            var = IntVar()
            button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
            button.place(x=375,y=250)
            button.wait_variable(var)
            phone=int(phone_entry.get())

        check_phone()
        while phone not in phone_lst:
            messagebox.showinfo("Invalid Phone Number","Phone Number Doesn't Exist in Database")
            check_phone()

        clear()

        Label(frame,text="Enter Updated Email :",font=('Calibri',15)).place(x=350,y=150)
        email_entry=Entry(frame,width=25,font=('Calibri',12))
        email_entry.place(x=350,y=200)

        cursor.execute("select email from customer_details")
        result=cursor.fetchall()
        email_lst=[]
        for i in result:
            for j in i:
                email_lst.append(j)
        def check_email():
            global email
            var = IntVar()
            button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
            button.place(x=375,y=250)
            button.wait_variable(var)
            email=email_entry.get()
            

        check_email()
        while email in email_lst:
            messagebox.showinfo("Invalid Email","Email Exists in Database")
            check_email()

        cursor.execute("update customer_details set email='{}' where phone={}".format(email, phone))
        db.commit()

        messagebox.showinfo("Success","Details Updated Successfully")

        home()


    Button(frame,text="Update Name",width=30,height=2,command=update_name).place(x=350,y=150)
    Button(frame,text="Update Phone",width=30,height=2,command=update_phone).place(x=350,y=200)
    Button(frame,text="Update Email",width=30,height=2,command=update_email).place(x=350,y=250)


    # ===================================== Cancel Booking ====================================
def cancel_booking():
    bookingdetails()

    Label(frame,text="Enter Ticket Number To Cancel: ",font=('Calibri',15)).place(x=320,y=370)
    tic_entry=Entry(frame,width=25,font=('Calibri',12))
    tic_entry.place(x=350,y=400)

    def check_int(input):
        if len(input)>8:
            return False
        elif input.isdigit() or input=="":
            return True
        else:
            return False
    check=frame.register(check_int)
    tic_entry.config(validate="key", validatecommand=(check, '%P'))
    
    cursor.execute("select ticket_no from booking_details")
    result=cursor.fetchall()
    tic_lst=[]
    for i in result:
        for j in i:
            tic_lst.append(j)
    
    def check_tic():
        global tic
        var = IntVar()
        button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
        button.place(x=375,y=430)
        button.wait_variable(var)
        tic=int(tic_entry.get())

    check_tic()
    while tic not in tic_lst:
        messagebox.showinfo("Invalid Ticket Number","Ticket Number Doesn't Exist in Database")
        check_tic()

    cursor.execute("select * from booking_details where ticket_no={}".format(tic))
    result=cursor.fetchall()

    for i in result:
        global flight
        row=i[3]
        col=i[4]
        flight=i[5]


    select_flight()

    df.loc[row, col] = "0"

    cursor.execute("delete from booking_details where ticket_no={}".format(tic))
    db.commit()

    messagebox.showinfo("Success" , "Booking Canceled Successfully")

    home()

# ===================================== Graph ====================================

def graph():
    clear()
    # customer vs booking graph
    def cust_vs_booking():
        cursor.execute("SELECT c.cust_id, COUNT(*) FROM customer_details AS c JOIN booking_details ON booking_details.cust_id = c.cust_id GROUP BY c.cust_id;")
        result = cursor.fetchall()

        x_axis=[]
        y_axis=[]
        for i in result:
            x=i[0]
            y=i[1]
            x_axis.append(x)
            y_axis.append(y)


        plt.bar(x_axis, y_axis)
        plt.yticks(y_axis)
        plt.xticks(x_axis)
        plt.xlabel(" Customer Id ") #add the Label on x-axis
        plt.ylabel("No. of Bookings") #add the Label on y-axis
        plt.title("User vs Bookings graph")
        plt.show()


    # booking vs booking date graph
    def booking_vs_date():   
        cursor.execute("SELECT booking_date, COUNT(*) FROM booking_details GROUP BY booking_date")

        result=cursor.fetchall()

        x_axis=[]
        y_axis=[]
        for i in result:
            x=i[0]
            y=i[1]
            x_axis.append(x)
            y_axis.append(y)
            
        plt.bar(x_axis, y_axis)
        plt.yticks(y_axis)
        plt.xlabel("Date") #add the Label on x-axis
        plt.ylabel("No. of Bookings") #add the Label on y-axis
        plt.title("Date vs Bookings graph")
        plt.show()

    Button(frame,text="View Customer vs Booking Graph",width=30,height=2,command=cust_vs_booking).place(x=350,y=175)
    Button(frame,text="View Booking vs Date Graph ",width=30,height=2,command=booking_vs_date).place(x=350,y=225)




# ===================================== UI ====================================

ui=Tk()
ui.title("Flight Reservation System")
ui.geometry("900x500")
frame = Frame(ui)
frame.pack(fill='both',expand=True)
canvas=Canvas(frame)
canvas.grid(sticky=E)

home()

ui.mainloop()
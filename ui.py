# =============================== Importing Packages ========================================
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
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
    
    bookingdetails_button=Button(frame,text="View Booking Details",width=30,height=2,command=bookingdetails).place(x=350,y=100)
    
    flight_schedule_button=Button(frame,text="View Flight Schedules",width=30,height=2,command=flightschedule).place(x=350,y=150)
    
    button=Button(frame,text="Book Seats",width=30,height=2,command=bookseats).place(x=350,y=200)
    
    button2=Button(frame,text="Customer Management",width=30,height=2,command=cust_mangement).place(x=350,y=250)
    
    button3=Button(frame,text="View Graphs",width=30,height=2,command=graph).place(x=350,y=300)
    
    button4=Button(frame,text="Exit",width=30,height=2,command=ui.destroy).place(x=350,y=350)


# =============================== Clear ========================================
def clear():
 
    for widgets in frame.winfo_children():
        widgets.destroy()
    
    Button(frame,text="Home",height=2,command=home).grid(padx=5,pady=5,sticky="NW")


# =============================== Select Flight Csv ========================================
def select_flight():
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
    
    var = IntVar()
    button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
    button.place(x=375,y=250)
    button.wait_variable(var)

    phone=phone_entry.get()
    
    cursor.execute("select * from customer_details where phone={}".format(phone))
    result_cust=cursor.fetchall()
    for i in result_cust:
        result_cust=i
    cust_id=result_cust[0]
    name=result_cust[1]
    email=result_cust[3]
    cursor.execute("select * from booking_details where cust_id={}".format(cust_id))
    
    clear()
    Label(frame,text="Name \t\t\t : {}".format(name),font=('Calibri',11)).place(x=250,y=20)
    Label(frame,text="Phone Number \t\t : {}".format(phone),font=('Calibri',11)).place(x=250,y=40)
    Label(frame,text="Email \t\t\t : {}".format(email),font=('Calibri',11)).place(x=250,y=60)
    
    result_booking=cursor.fetchall()
    for i in result_booking:
        tic=i[1]
        booking_date=i[2]
        row=i[3]
        col=i[4]
        col=col.upper()
        y=60
        y=y+20
        Label(frame,text="").place(y=y)
        Label(frame,text="Ticket Number \t\t :  {}".format(tic),font=('Calibri',11)).place(y=(y+20),x=250)
        Label(frame,text="Booking Date \t\t :  {}".format(booking_date),font=('Calibri',11)).place(y=(y+40),x=250)
        Label(frame,text="Seat Number \t\t :  {} {}".format(col,row),font=('Calibri',11)).place(y=(y+60),x=250)
    

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
    

                
    clear()
    
    flightschedule()

    cursor.execute("select * from flight_details")

    result = cursor.fetchall()

    f1=result[0]
    f2=result[1]
    f3=result[2]
    f4=result[3]
    f5=result[4]

    
    lst_flight=["1","2","3","4","5","flight1","flight2","flight3","flight4","flight5"]
    
    Label(frame,text="Enter Flight Number : ",font=('Calibri',11)).place(x=370,y=280)
    flightno_entry=Entry(frame,width=25,font=('Calibri',12))
    flightno_entry.place(x=370,y=300)

    var = IntVar()
    button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
    button.place(x=400,y=335)
    button.wait_variable(var)

    flight=flightno_entry.get()
    select_flight()
    clear()
    Label(frame,text="Select Seats",font=('Calibri',14)).place(x=400,y=35)

    
    l1 = ["A", "B", "C", "D", "E", "F"]
    
    canvas = Canvas(frame,width=250,height=300,bg="skyblue3")
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
            
            var = IntVar()
            button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
            button.place(x=385,y=350)
            button.wait_variable(var)
            name=name_entry.get()
            email=email_entry.get()
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


def search_cust():
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
        


    def search_phone():

        clear()
        
        Label(frame,text="Enter Phone : ",font=('Calibri',15)).place(x=350,y=150)
        phone_entry=Entry(frame,width=25,font=('Calibri',12))
        phone_entry.place(x=350,y=200)

        var = IntVar()
        button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
        button.place(x=375,y=250)
        button.wait_variable(var)
        phone=phone_entry.get()
        
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

def add_cust():
    clear()

    Label(frame,text="Enter Phone Number :",font=('Calibri',11)).place(x=375,y=130)
    phone_entry=Entry(frame,font=('Calibri',11),width=25)
    phone_entry.place(x=370,y=150)      

    Label(frame,text="Enter Name :",font=('Calibri',11)).place(x=375,y=205)
    name_entry=Entry(frame,font=('Calibri',11),width=25)
    name_entry.place(x=370,y=225)

    Label(frame,text="Enter Email :",font=('Calibri',11)).place(x=375,y=280)
    email_entry=Entry(frame,font=('Calibri',11),width=25)
    email_entry.place(x=370,y=300)

    var = IntVar()
    button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
    button.place(x=380,y=340)
    button.wait_variable(var)
    
    name=name_entry.get()
    email=email_entry.get()
    phone=phone_entry.get()

    cursor.execute("insert into customer_details (name,phone,email) values('{}',{},'{}')".format(name,phone,email))
    db.commit()
    messagebox.showinfo("Success","Details Added Successfully")

    home()


def update_cust():
    clear()
    
    def update_name():
        clear()
        Label(frame,text="Enter Phone :").grid()
        phone_entry=Entry(frame)
        phone_entry.grid()

        var = IntVar()
        button = Button(frame, text="Confirm", command=lambda: var.set(1))
        button.grid()
        button.wait_variable(var)

        phone=phone_entry.get()

        Label(frame,text="Enter Updated Name :").grid()
        name_entry=Entry(frame)
        name_entry.grid()

        var = IntVar()
        button = Button(frame, text="Confirm", command=lambda: var.set(1))
        button.grid()
        button.wait_variable(var) 
        name=name_entry.get()

        cursor.execute("update customer_details set name='{}' where phone={}".format(name, phone))
        db.commit()

        messagebox.showinfo("Success","Details Updated Successfully")

        home()


    def update_phone():
        clear()
        Label(frame,text="Enter Email :").grid()
        email_entry=Entry(frame)
        email_entry.grid()

        var = IntVar()
        button = Button(frame, text="Confirm", command=lambda: var.set(1))
        button.grid()
        button.wait_variable(var)

        email=email_entry.get()
   
   
    def update_email():
        clear()
        Label(frame,text="Enter Phone :").grid()
        phone_entry=Entry(frame)
        phone_entry.grid()
        
        
        var = IntVar()
        button = Button(frame, text="Confirm", command=lambda: var.set(1))
        button.grid()
        button.wait_variable(var)    

        phone=phone_entry.get()


    Button(frame,text="Update Name",width=30,height=2,command=update_name).place(x=350,y=150)
    Button(frame,text="Update Phone",width=30,height=2,command=update_phone).place(x=350,y=200)
    Button(frame,text="Update Email",width=30,height=2,command=update_email).place(x=350,y=250)

def cancel_booking():
    bookingdetails()

    Label(frame,text="Enter Ticket Number : ",font=('Calibri',15)).place(x=350,y=300)
    tic_entry=Entry(frame,width=25,font=('Calibri',12))
    tic_entry.place(x=350,y=320)
    
    var = IntVar()
    button = Button(frame, text="Confirm", command=lambda: var.set(1),height=1,width=20)
    button.place(x=375,y=350)
    button.wait_variable(var)

    tic=tic_entry.get()
    cursor.execute("select * from booking_details where ticket_no={}".format(tic))
    result=cursor.fetchall()

    for i in result:
        row=i[3]
        col=i[4]
        flight=i[5]

    select_flight()

    df.loc[row, col] = "0"

    tic=int(tic)

    # cursor.execute("delete from booking_details where ticket_no={}".format(tic))
    # db.commit()

    messagebox.showinfo("Success" , "Booking Canceled Successfully")

    home()
# ===================================== Graph ====================================
def graph():
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
    plt.xlabel("User") #add the Label on x-axis
    plt.ylabel("No. of Bookings") #add the Label on y-axis
    plt.title("User vs Bookings graph")
    plt.show()


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
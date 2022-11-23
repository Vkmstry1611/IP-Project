# importing packages
import os
import pandas as pd
import random
import mysql.connector as sql
import matplotlib as plt

#connecting to database

db = sql.connect(
    host="localhost",
    user="root",
    password="root",
    database="db")

print(db)

cursor = db.cursor()


df = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight1.csv", index_col=0)

# functions

def cust_mangement():
    while True:
        print("1) \t Display all Customer Records")
        print("2) \t Search Customer Record")
        print("3) \t Update Customer Record")
        print("4) \t Delete Customer Record")
        print("5) \t Add Customer Record")
        print("6) \t exit \n")

        op = int(input("Enter your Choice :  "))

        os.system("cls")

        if op == 1:
            display_records()
        elif op == 2:
            print()
        elif op == 3:
            update_cust()
        elif op == 4:
            delete_cust()
        elif op == 5:
            add_cust()
        elif op == 6:
            break
        else:
            print("Invalid Option")


def display_records():
    cursor.execute("select * from customer_details")
    result = cursor.fetchall()

    id=[]
    for i in result:
        
        
        id.append(i[0])
    col=["Customer Id","Name","Phone","Email"]

    details=pd.DataFrame(result,index=id,columns=col)
    details=details.drop('Customer Id',axis=1)
    print("\n",details,"\n")


def search_cust():
    name = input("Enter Name :  ")

    cursor.execute('select * from customer_details where name like "%{}%"'.format(name))

    result = cursor.fetchall()

    for i in result:
        print(i)

def add_cust():
    name=str(input("Enter Name :  "))
    phone=int(input("Enter Phone :  "))
    email=str(input("Enter Email :  "))

    cursor.execute("insert into customer_details (name,phone,email) values('{}',{},'{}')".format(name,phone,email))
    db.commit()
    print("Details Added Successfully")
    



def update_cust():
    print("1) Update Name ")
    print("2) Update Phone ")
    print("3) Update Email")

    opt = int(input("Enter Your Option :  "))

    if opt == 1:
        phone = int(input("Enter Phone Number :  "))

        name = str(input("Enter Updated Name :  "))
        cursor.execute("update customer_details set name='{}' where phone={}".format(name, phone))
        db.commit()
        print("Details Updated Successfully")

    elif opt == 2:
        name = str(input("Enter Name :  "))
        phone = int(input("Enter Updated Phone Number :  "))
        cursor.execute("update customer_details set phone={} where name='{}'".format(phone, name))
        db.commit()
        print("Details Updated Successfully")

    elif opt == 3:

        name = str(input("Enter Name :  "))
        email = str(input("Enter Updated Email :  "))

        cursor.execute("update customer_details set email={} where name={}".format(email, name))
        db.commit()
        print("Details Updated Successfully")

    else:
        print("Invalid Option")


def delete_cust():
    phone=("Enter Phone Number :  ")
    cursor.execute("delete from customer_details where phone={}".format(phone))

    db.commit()

    print("Details Deleted Successfully")


def bookseats():
    flightschedule()

    cursor.execute("select * from flight_details")

    result = cursor.fetchall()

    f1=result[0]
    f2=result[1]
    f3=result[2]
    f4=result[3]
    f5=result[4]

    print("\n\n")

    lst_flight=["1","2","3","4","5","flight1","flight2","flight3","flight4","flight5"]
    flight=str(input("Enter Flight Number : "))

    while flight not in lst_flight:
        print("Invalid Input")
        flight=str(input("Enter Flight Number : "))

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


    print ("***** Select Seats ***** \n")
    print(df,"\n")
    l1 = ["A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f"]
    col = input("Enter Column :  ")
    col.upper()

    while col not in l1:
        col = input("Enter Column :  ")

    row = int(input("Enter Row :  "))


    while row not in range(1,31):

        print(" \n Invalid Input\n ")    
        row = int(input("Enter Row :  "))


    if df.loc[row, col] == "X":
        print("Seat Already Booked")
    else:
        df.loc[row, col] = "X"
        print("\n",df,"\n")
        print("Your Seat Is ", col, row)
        
        
        tic = random.randint(10000000, 99999999)
        
        cursor.execute("select ticket_no from booking_details")
        result=cursor.fetchall()

        lst=[]

        for i in result:
            for j in i:
                lst.append(j)

        while tic in lst:
            tic = random.randint(10000000, 99999999)

        print("Your Ticket Number is : ", tic,"\n")

        phone=int(input("Enter Phone Number : "))

        
        cursor.execute("select phone from customer_details")
        result=cursor.fetchall()
        phone_lst=[]
        for i in result:
            for j in i:
                phone_lst.append(j)

        if phone in phone_lst:
            print()
        else:
            name=input("Enter Name : ")
            email=input("Enter Email : ")
            cursor.execute("insert into customer_details(name,phone,email) values('{}',{},'{}')".format(name,phone,email))
            db.commit()

        cursor.execute("select cust_id from customer_details where phone={} ".format(phone))

        result=cursor.fetchall()


        for i in result:
            for j in i:
                cust_id=j


        cursor.execute("insert into booking_details values({},{},curdate(),{},'{}','{}')".format(cust_id,tic,row,col,flight))

        db.commit()

        save_csv()
        print("Seat Booked Successfully")


def flightschedule():
    cursor.execute("select * from flight_details")

    result = cursor.fetchall()

    f1=result[0]
    f2=result[1]
    f3=result[2]
    f4=result[3]
    f5=result[4]


    print("\t\t Flight \t\t | \t\t To \t\t | \t\t From \t\t" )
    print("---------------------------------------------------------------------------------------------------")
    print("\t\t",f1[0]," \t\t | \t\t",f1[1],"\t\t | \t\t",f1[2],"\t\t" )
    print("\t\t",f2[0]," \t\t | \t\t",f2[1],"\t\t | \t\t",f2[2],"\t\t" )
    print("\t\t",f3[0]," \t\t | \t\t",f3[1],"\t\t | \t\t",f3[2],"\t\t" )
    print("\t\t",f4[0]," \t\t | \t\t",f4[1],"\t\t | \t\t",f4[2],"\t\t" )
    print("\t\t",f5[0]," \t\t | \t\t",f5[1],"\t\t | \t\t",f5[2],"\t\t" )





def bookingdetail():
    phone=int(input("Enter Phone Number : "))

    cursor.execute("select * from customer_details where phone={}".format(phone))

    result_cust=cursor.fetchall()

    for i in result_cust:
        result_cust=i

    cust_id=result_cust[0]
    name=result_cust[1]
    email=result_cust[3]

    cursor.execute("select * from booking_details where cust_id={}".format(cust_id))

    print("Name \t\t\t :  " ,name)
    print("Phone Number \t\t :  ", phone)
    print("Email \t\t\t :  ", email)
    print()
    result_booking=cursor.fetchall()

    for i in result_booking:
        tic=i[1]
        booking_date=i[2]
        row=i[3]
        col=i[4]
        col=col.upper()
        print("Ticket Number \t\t :  " , tic)
        print("Booking Date \t\t :  ",booking_date)
        print("Seat Number \t\t :  " , col , row)
        print()


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

    print(x_axis)
    print(y_axis)

            

    plt.bar(x_axis, y_axis)
    plt.xlabel("User") #add the Label on x-axis
    plt.ylabel("No. of Bookings") #add the Label on y-axis
    plt.title("User vs Bookings graph")
    plt.show()


    
#############

while True:
    print("1) \t View Booking Details")
    print("2) \t View Flight Schedules")
    print("3) \t Book Seats")
    print("4) \t Customer Management")
    print("5) \t View Graphs")
    print("6) \t Exit")

    opt = int(input("Enter Your Choice :  "))

    # os.system("cls")

    if opt == 1:
        bookingdetail()
    elif opt == 2:
        flightschedule()
    elif opt == 3:
        bookseats()
    elif opt == 4:
        cust_mangement()
    elif opt == 5:
        graph()
    elif opt==6:
        break

    else:
        print("Invalid Option")

        

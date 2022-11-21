# importing packages
import os
import pandas as pd
import random
import mysql.connector as sql

#connecting to database

db = sql.connect(
    host="localhost",
    user="root",
    password="root",
    database="db")

print(db)

cursor = db.cursor()


flight1 = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight1.csv", index_col=0)

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

    for i in result:
        print(i)


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
        cursor.execute("update customer_details set phone={} where name={}".format(phone, name))
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
        
    print ("***** Select Seats ***** \n")
    print(flight1 ,"\n")
    l1 = ["A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f"]
    col = input("Enter Column :  ")
    if col not in l1:
        print("Invalid Input \n")
    else:
        print()
    row = int(input("Enter Row :  "))
    if row >= 1 and row <= 30:
        print()
    else:
        print("Invalid Input \n")
    if flight1.loc[row, col] == "X":
        print("Seat Already Booked")
    else:
        flight1.loc[row, col] = "X"
        print("\n",df,"/n")
        print("Your Seat Is ", col, row)
        
        df.to_csv(path_or_buf="D:/Study/12th/Project/IP/Practical/IP-Project/flight.csv", sep=',')
        
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

        name=input("Enter Name : ")
        phone=int(input("Enter Phone Number : "))
        email=input("Enter Email : ")
        
        cursor.execute("insert into customer_details(name,phone,email) values('{}',{},'{}')".format(name,phone,email))
        
        db.commit()

        cursor.execute("select cust_id from customer_details where name='{}' ".format(name))

        result=cursor.fetchall()

    

        for i in result:
            for j in i:
                cust_id=j


        cursor.execute("insert into booking_details values({},{},curdate(),{},'{}')".format(cust_id,tic,row,col))

        db.commit()

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

    result_booking=cursor.fetchall()
    for i in result_booking:
        result_booking=i


    tic=result_booking[1]
    booking_date=result_booking[2]
    row=result_booking[3]
    col=result_booking[4]
    col=col.upper()
    print()
    print("Ticket Number \t\t :  " , tic)
    print("Name \t\t\t :  " ,name)
    print("Phone Number \t\t :  ", phone)
    print("Email \t\t\t :  ", email)
    print("Booking Date \t\t :  ",booking_date)
    print("Seat Number \t\t :  " , col , row)

    

while True:
    print("1) \t View Booking Details")
    print("2) \t View Flight Schedules")
    print("3) \t Book Seats")
    print("4) \t Customer Management")
    print("5) \t Exit")

    opt = int(input("Enter Your Choice :  "))

    os.system("cls")

    if opt == 1:
        bookingdetail()
    elif opt == 2:
        flightschedule()
    elif opt == 3:
        bookseats()
    elif opt == 4:
        cust_mangement()
    elif opt == 5:
        break
    else:
        print("Invalid Option")

        

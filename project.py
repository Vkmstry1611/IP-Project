#importing packages
import os
import pandas as pd
import random 
import mysql.connector as sql

db=sql.connect(
    host="localhost",
    user="root",
    password="root",
    database="db"
)

print(db)

cursor=db.cursor()


df=(pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight.csv",index_col=0))

def cust_mangement():
    while True:
        print("1) \t Display all Customer Records")
        print("2) \t Search Customer Record")
        print("3) \t Update Customer Record")
        print("4) \t Delete Customer Record")
        print("5) \t exit \n")

        
        op=int(input("Enter your Choice :  " ))

        os.system("cls")

        if op==1:
            display_records()
        elif op==2:
            print()
        elif op==3:
            print()
        elif op==4:
            print()
        elif op==5:
            break
        else:
            print("Invalid Option")



def display_records():
    cursor.execute("select * from customer_details")
    result=cursor.fetchall()

    for i in result:
        print(i)

def search_cust():
    print()

def update_cust():
    print()

def delete_cust():
    print( )





def bookseats():
    
    l1=["A","B","C","D","E","F","a","b","c","d","e","f"]
    col=input("Enter Column :  ")
    if col not in l1:
        print("Invalid Input \n")
    else:
        print()

    row=int(input("Enter Row :  "))
    if row>=1 and row <=30:
        print()
    else:
        print("Invalid Input \n")
    if df.loc[row,col]=="X":
        print("Seat Already Booked")
    else:
        df.loc[row,col]="X"
        df.to_csv(path_or_buf="D:/Study/12th/Project/IP/Practical/IP-Project/flight.csv",sep=',')
    print(df)

    print("Your Seat Is ",col,row)

    tic=random.randint(10000000,99999999)


    



def flightschedule():
    while True:
        print()


def bookingdetail():
    while True:
        tic=int(input("Enter Ticket Number :  "))

       

        



while True:
    print("1) \t View Booking Details")
    print("2) \t View Flight Schedules")
    print("3) \t Book Seats")
    print("4) \t Customer Management")
    print("5) \t Exit")

    opt=int(input("Enter Your Choice :  "))
    
    os.system("cls")
    
    if opt==1:
        bookingdetail()
    elif opt==2:
        flightschedule()    
    elif opt==3:
        bookseats()
    elif opt==4:
        cust_mangement()
    elif opt==5:
        break
    else:
        print("Invalid Option") 
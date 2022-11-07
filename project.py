#importing packages

import pandas as pd

def cust_mangement():
    while True:
        print("1) \t Display all Customer Records")
        print("2) \t Search Customer Record")
        print("3) \t Update Customer Record")
        print("4) \t Delete Customer Record")
        print("5) \t exit")
        
        op=int(input("Enter your Choice :  "))

        if op==1:
            print()
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


def book():
    while True:
        print()

    

        

#print(pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight.csv"))

while True:
    print("1) \t View Booking Details")
    print("2) \t View Flight Schedules")
    print("3) \t Book Seats")
    print("4) \t Customer Management")
    print("5) \t Exit")

    opt=int(input("Enter Your Choice :  "))
    
    if opt==1:
        print("")
    elif opt==2:
        print("")    
    elif opt==3:
        print("")
    elif opt==4:
        print("")
    elif opt==5:
        break
    else:
        print("Invalid Option") 
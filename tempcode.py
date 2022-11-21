import mysql.connector as sql
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

# dict1={
# 'A': pd.Series([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],index=np.arange(1,31,1)),
# 'B': pd.Series([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],index=np.arange(1,31,1)),
# 'C': pd.Series([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],index=np.arange(1,31,1)),
# '    ': pd.Series(["    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    ","    "],index=np.arange(1,31,1)),
# 'D': pd.Series([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],index=np.arange(1,31,1)),
# 'E': pd.Series([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],index=np.arange(1,31,1)),
# 'F': pd.Series([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],index=np.arange(1,31,1)),
# }

# df=pd.DataFrame(dict1)


# print(df,"\n \n")
# df.to_csv(path_or_buf="D:/Study/12th/Project/IP/Practical/IP-Project/flight.csv",sep=',')
# seat_col=input()

# df=pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight.csv")
# print(df)

# l1=["A","B","C","D","E","F","a","b","c","d","e","f"]
# col=input("Enter Column :  ")
# if col not in l1:
#     print("Invalid Input \n")
# else:
#     print()

# row=int(input("Enter Row :  "))
# if row>=1 and row <=30:
#     print()
# else:
#     print("Invalid Input \n")
# if df.loc[row,col]=="X":
#     print("Seat Already Booked")
# else:
#     df.loc[row,col]="X"
# print(df)
# df.to_csv(path_or_buf="D:/Study/12th/Project/IP/Practical/IP-Project/flight.csv",sep=',')

db=sql.connect(
    host="localhost",
    user="root",
    password="root",
    database="db"
)

print(db)

cursor=db.cursor()

def display():

    cursor.execute("select * from customer_details")
    result=cursor.fetchall()

    for i in result:
        print(i)


# search records

# name=input("Enter Name :  ")

# cursor.execute('select * from customer_details where name like "%{}%"'.format(name))

# result=cursor.fetchall()

# for i in result:
#     print(i) 


# update record

# print("1) Update Name ")
# print("2) Update Phone ")
# print("3) Update Email")

# opt=int(input("Enter Your Option :  "))

# if opt==1:
#     phone=int(input("Enter Phone Number :  "))

#     name=str(input("Enter Updated Name :  "))
#     cursor.execute("update customer_details set name='{}' where phone={}".format(name,phone))
#     db.commit()
#     print("Details Updated Successfully")
    
# elif opt==2:
#     name=str(input("Enter Name :  "))
#     phone=int(input("Enter Updated Phone Number :  "))
#     cursor.execute("update customer_details set phone={} where name={}".format(phone,name))

#     print("Details Updated Successfully")
    

# elif opt==3:
    
#     name=str(input("Enter Name :  "))
#     email=str(input("Enter Updated Email :  "))

#     cursor.execute("update customer_details set email={} where name={}".format(email,name))
#     db.commit()
#     print("Details Updated Successfully")
    

# delete record

# phone=("Enter Phone Number :  ")
# cursor.execute("delete from customer_details where phone={}".format(phone))

# db.commit()

# print("Details Deleted Successfully")
# # add record 
 
# name=str(input("Enter Name :  "))
# phone=int(input("Enter Phone :  "))
# email=str(input("Enter Email :  "))

# cursor.execute("insert into customer_details (name,phone,email) values('{}',{},'{}')".format(name,phone,email))
# db.commit()
# print("Details Added Successfully")


# df = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight.csv", index_col=0)


#booking details

# phone=int(input("Enter Phone Number : "))

# cursor.execute("select * from customer_details where phone={}".format(phone))

# result_cust=cursor.fetchall()

# for i in result_cust:
#     result_cust=i

# cust_id=result_cust[0]
# name=result_cust[1]
# email=result_cust[3]

# cursor.execute("select * from booking_details where cust_id={}".format(cust_id))

# result_booking=cursor.fetchall()
# for i in result_booking:
#     result_booking=i


# tic=result_booking[1]
# booking_date=result_booking[2]
# row=result_booking[3]
# col=result_booking[4]
# col=col.upper()
# print()
# print("Ticket Number \t\t :  " , tic)
# print("Name \t\t\t :  " ,name)
# print("Phone Number \t\t :  ", phone)
# print("Email \t\t\t :  ", email)
# print("Booking Date \t\t :  ",booking_date)
# print("Seat Number \t\t :  " , col , row)


# graph

# def customer_vs_tickets():
# 	cursor.execute("SELECT c.cust_id, COUNT(*) FROM customer_details AS c JOIN booking_details ON booking_details.cust_id = c.cust_id GROUP BY c.cust_id;")
# 	result = cursor.fetchall()
# 	plt.plot(result[0], result[1], kind="bar")
# 	plt.xlabel("User") #add the Label on x-axis
# 	plt.ylabel("No. of Bookings") #add the Label on y-axis
# 	plt.title("User vs Bookings graph")
# 	plt.show()
    

#customer_vs_tickets()

flight1 = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight1.csv", index_col=0)
flight2 = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight2.csv", index_col=0)
flight3 = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight3.csv", index_col=0)
flight4 = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight4.csv", index_col=0)
flight5 = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight5.csv", index_col=0)


#book seats
flightschedule()

cursor.execute("select * from flight_details")

result = cursor.fetchall()

f1=result[0]
f2=result[1]
f3=result[2]
f4=result[3]
f5=result[4]

print("\n\n")

lst_flight=["flight1","flight2","flight3","flight4","flight5"]
flight=str(input("Enter Flight Number : "))

while flight not in lst_flight:
    print("Invalid Input")
    flight=str(input("Enter Flight Number : "))




print ("***** Select Seats ***** \n")
print(df,"\n")
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
if df.loc[row, col] == "X":
    print("Seat Already Booked")
else:
    df.loc[row, col] = "X"
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


#flight schedule
# cursor.execute("select * from flight_details")

# result = cursor.fetchall()

# f1=result[0]
# f2=result[1]
# f3=result[2]
# f4=result[3]
# f5=result[4]


# print("\t\t Flight \t\t | \t\t To \t\t | \t\t From \t\t" )
# print("---------------------------------------------------------------------------------------------------")
# print("\t\t",f1[0]," \t\t | \t\t",f1[1],"\t\t | \t\t",f1[2],"\t\t" )
# print("\t\t",f2[0]," \t\t | \t\t",f2[1],"\t\t | \t\t",f2[2],"\t\t" )
# print("\t\t",f3[0]," \t\t | \t\t",f3[1],"\t\t | \t\t",f3[2],"\t\t" )
# print("\t\t",f4[0]," \t\t | \t\t",f4[1],"\t\t | \t\t",f4[2],"\t\t" )
# print("\t\t",f5[0]," \t\t | \t\t",f5[1],"\t\t | \t\t",f5[2],"\t\t" )




import mysql.connector as sql
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
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


#book seats
# cursor.execute("select * from flight_details")
# # result = cursor.fetchall()
# f1=result[0]
# f2=result[1]
# f3=result[2]
# f4=result[3]
# # f5=result[4]
# # print("\n\n")
# lst_flight=["1","2","3","4","5","flight1","flight2","flight3","flight4","flight5"]
# # flight=str(input("Enter Flight Number : "))
# while flight not in lst_flight:
    # print("Invalid Input")
    # # flight=str(input("Enter Flight Number : "))
# if flight=="1" or flight=="flight1":
    # flight="flight1"
    # df = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight1.csv", index_col=0)
    # def save_csv():
        # # df.to_csv(path_or_buf="D:/Study/12th/Project/IP/Practical/IP-Project/flight1.csv",sep=',')
# elif flight=="2" or flight=="flight2":
    # flight="flight2"
    # df = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight2.csv", index_col=0)
    # def save_csv():
        # df.to_csv(path_or_buf="D:/Study/12th/Project/IP/Practical/IP-Project/flight2.csv",sep=',')
    # 
# elif flight=="3" or flight=="flight3":
    # flight="flight3"
    # df = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight3.csv", index_col=0)
    # def save_csv():
        # df.to_csv(path_or_buf="D:/Study/12th/Project/IP/Practical/IP-Project/flight3.csv",sep=',')
# elif flight=="4" or flight=="flight4":
    # flight="flight4"
    # df = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight4.csv", index_col=0)
    # def save_csv():
        # df.to_csv(path_or_buf="D:/Study/12th/Project/IP/Practical/IP-Project/flight4.csv",sep=',')
# elif flight=="5" or flight=="flight5":
    # flight="flight5"
    # df = pd.read_csv("D:/Study/12th/Project/IP/Practical/IP-Project/flight5.csv", index_col=0)
    # def save_csv():
        # # df.to_csv(path_or_buf="D:/Study/12th/Project/IP/Practical/IP-Project/flight5.csv",sep=',')
# print ("***** Select Seats ***** \n")
# print(df,"\n")
# l1 = ["A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f"]
# col = input("Enter Column :  ")
# # col.upper()
# while col not in l1:
    # # col = input("Enter Column :  ")
# # row = int(input("Enter Row :  "))
# row = int(input("Enter Row :  "))
# # while row not in range(1,31):
    # print(" \n Invalid Input\n ")    
    # # row = int(input("Enter Row :  "))
# if df.loc[row, col] == "X":
    # print("Seat Already Booked")
# else:
    # df.loc[row, col] = "X"
    # print("\n",df,"/n")
    # print("Your Seat Is ", col, row)
    # 
    # 
    # tic = random.randint(10000000, 99999999)
    # 
    # cursor.execute("select ticket_no from booking_details")
    # # result=cursor.fetchall()
    # # lst=[]
    # for i in result:
        # for j in i:
            # # lst.append(j)
    # while tic in lst:
        # # tic = random.randint(10000000, 99999999)
    # # print("Your Ticket Number is : ", tic,"\n")
    # name=input("Enter Name : ")
    # phone=int(input("Enter Phone Number : "))
    # email=input("Enter Email : ")
    # 
    # cursor.execute("insert into customer_details(name,phone,email) values('{}',{},'{}')".format(name,phone,email))
    # 
    # # db.commit()
    # # cursor.execute("select cust_id from customer_details where name='{}' ".format(name))
    # # result=cursor.fetchall()
# 
    # for i in result:
        # for j in i:
            # # cust_id=j
    # # cursor.execute("insert into booking_details values({},{},curdate(),{},'{}','{}')".format(cust_id,tic,row,col,flight))
    # # db.commit()
    # save_csv()
    # print("Seat Booked Successfully")
# 

    
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


#view customer details

cursor.execute("select * from customer_details")
result = cursor.fetchall()

# print("\t Customer ID \t | \t Name \t\t | \t Phone \t | \t Email \t" )
# print("---------------------------------------------------------------------------------------------------")
 # print(result)

# id=[]
# for i in result:
    
    
#     id.append(i[0])
# col=["Customer Id","Name","Phone","Email"]

# details=pd.DataFrame(result,index=id,columns=col)
# details=details.drop('Customer Id',axis=1)
# print(details)



# cursor.execute("select phone from customer_details")
# result=cursor.fetchall()
# phone_lst=[]
# for i in result:
#     for j in i:
#         phone_lst.append(j)

# print(phone_lst)


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

# print("Name \t\t\t :  " ,name)
# print("Phone Number \t\t :  ", phone)
# print("Email \t\t\t :  ", email)
# print()
# result_booking=cursor.fetchall()

# for i in result_booking:
#     tic=i[1]
#     booking_date=i[2]
#     row=i[3]
#     col=i[4]
#     col=col.upper()
#     print("Ticket Number \t\t :  " , tic)
#     print("Booking Date \t\t :  ",booking_date)
#     print("Seat Number \t\t :  " , col , row)
#     print()


l1 = ["A", "B", "C", "D", "E", "F"]

# for row in range(1,31):
#     for col in l1:

#         if col=="F":
            
#             print(col,row,"  ")
#         else:
#             print(col,row,end="  ")

# tic=int(input("Enter Ticket Number :  "))
# cursor.execute("select cust_id from booking_details where ticket_no={}".format(tic))

# result=cursor.fetchall()
# for i in result:
#     for j in i:
#         cust_id=j

# cursor.execute("delete from booking_details where ticket_no={}".format(tic))
# db.commit()


# phone=9876543210
# cursor.execute("select * from customer_details where phone={}".format(phone))
# result=cursor.fetchall()

# for i in result:
#     result=i
# cust_id=result[0]
# name=result[1]
# email=result[3]

# cursor.execute("select * from booking_details where cust_id={}".format(cust_id))
# result=cursor.fetchall()


# lst=[]
# for i in result:
#     lst.append(list(i))

# for i in lst:
#     i.pop(0)
#     row=i[2]
#     col=i[3]
#     i.pop(2)
#     i.pop(2)
#     i.insert(2,"{}{}".format(col,row))

ui=Tk()
frame = Frame(ui)
frame.pack(fill='both',expand=True)
canvas=Canvas(frame)
canvas.grid(sticky=E)
ui.geometry("900x500")



# cursor.execute("select email from customer_details")
# result=cursor.fetchall()
# email_lst=[]
# for i in result:
#     for j in i:
#         email_lst.append(j)

print(email_lst)

Label(frame,text="Enter Email : ",font=('Calibri',15)).place(x=350,y=150)
email_entry=Entry(frame,width=25,font=('Calibri',12))
email_entry.place(x=350,y=200)


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

ui.destroy()


ui.mainloop()




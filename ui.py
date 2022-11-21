import tkinter as tk
import pandas as pd
import numpy as np
import mysql.connector as sql   
import random
        
# dict1={
# 'A': pd.Series([False,False,False,False,False,False,False,False,False,False],index=np.arange(1,11,1)),
# 'B': pd.Series([False,False,False,False,False,False,False,False,False,False],index=np.arange(1,11,1)),
# 'C': pd.Series([False,False,False,False,False,False,False,False,False,False],index=np.arange(1,11,1)),
# '    ': pd.Series(["    ","    ","    ","    ","    ","    ","    ","    ","    ","    "],index=np.arange(1,11,1)),
# 'D': pd.Series([False,False,False,False,False,False,False,False,False,False],index=np.arange(1,11,1)),
# 'E': pd.Series([False,False,False,False,False,False,False,False,False,False],index=np.arange(1,11,1)),
# 'F': pd.Series([False,False,False,False,False,False,False,False,False,False],index=np.arange(1,11,1)),
# }
# back=""

# df=pd.DataFrame(dict1)

# def checkseat(col,row):
#     if df.loc[row,col]==True:
#         back="red"
#         return back
#     else:
#         back="green"
#         return back

# top=tk.Tk()


# a1=tk.Button(top,text="A1",command=checkseat("A",1), bg=back)





# a1.pack( )
# top.mainloop()


db = sql.connect(
    host="localhost",
    user="root",
    password="root",
    database="db")

print(db)

cursor = db.cursor()

# cursor.execute("select ticket_no from booking_details")
# result=cursor.fetchall()

# lst=[]

# for i in result:
#     for j in i:
#         lst.append(j)
# tic=random.randint(10000000,99999999)
# print(tic)
# while tic in lst:
#     tic = random.randint(10000000, 99999999)

# print (tic)
# name=input("Enter Name : ")
# cursor.execute("select cust_id from customer_details where name='{}' ".format(name))

# result=cursor.fetchall()

# print(result)

# for i in result:
#     for j in i:
#         cust_id=j

# print (cust_id)

lst_flight=[1,2,3,4,5,"flight1","flight2","flight3","flight4","flight5"]
flight=input("Enter Flight Number : ")

while flight not in lst_flight:
    flight=input("Enter Flight Number : ")
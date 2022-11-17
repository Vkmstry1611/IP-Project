import mysql.connector as sql
import numpy as np
import pandas as pd

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

#display records 

# cursor.execute("select * from customer_details")
# result=cursor.fetchall()

# for i in result:
#     print(i)


# search records

query='select * from customer_details where name like "%s"'
name="akash verma"

cursor.execute(query ,[name])

result=cursor.fetchall()

for i in result:
    print(i) 
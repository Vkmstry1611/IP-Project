import matplotlib.pyplot as plt
import mysql.connector as sql

db=sql.connect(
    host = "localhost",
    user = "root",
    password = "root",
	database = "db"
)

cursor=db.cursor()


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

cursor.execute("SELECT booking_date, COUNT(*) FROM booking_details GROUP BY booking_date;")

result_booking=cursor.fetchall()

x_axis_bookings=[]
y_axis_bookings=[]
for i in result:
	x=i[0]
	y=i[1]
	x_axis_bookings.append(x)
	y_axis_bookings.append(y)
	
plt.bar(x_axis, y_axis)
plt.xlabel("Date") #add the Label on x-axis
plt.ylabel("No. of Bookings") #add the Label on y-axis
plt.title("Date vs Bookings graph")
plt.show()



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


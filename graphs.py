import matplotlib.pyplot as plt
import mysql.connector as sql

db=sql.connect(
    host = "localhost",
    user = "root",
    password = "root",
	database = "db"
)

cursor=db.cursor()

def customer_vs_tickets graph:
	cursor.execute("SELECT c.cust_id, COUNT(*) FROM customer_details AS c JOIN booking_details ON booking_details.cust_id = c.cust_id GROUP BY c.cust_id;")
	result = cursor.fetchall()
	plt.plot(result[0], result[1])
	plt.xlabel("User") #add the Label on x-axis
	plt.ylabel("No. of Bookings") #add the Label on y-axis
	plt.title("User vs Bookings graph")
	plt.show()

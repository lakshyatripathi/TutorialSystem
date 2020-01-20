import pymysql

q = int(input("Enter the id to check status"))

# Open database connection
db = pymysql.connect("localhost", "root", "", "tutorial")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql1 = "SELECT status FROM student WHERE id = %s"

try:
            # Execute the SQL command
            cursor.execute(sql1, q)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchone()
            if (results == None):
                print("Record not found")
            else:
                for row in results:
                    row=results


                ab = pymysql.connect("localhost", "root", "", "tutorial")
                cursor = ab.cursor()
                abc = "SELECT tname,phone from teacher where tid=%s"

                cursor.execute(abc, row)
                x = cursor.fetchone()
                a = x[0]
                b = x[1]
                print("Your Faculty Name is:",a)
                print("Your faculty contact number is:",b)

                ab.close()






except:
            print("Error: unable to fetch data")

db.close()


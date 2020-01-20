import pymysql
import Appoint
import Appoint2

def admin(pas):
    x=1234
    if(pas!= x):
        return("Invalid password!\n"
               "Try Again\n\n")

    else:
        print("Login Sucessful\n")

        print("1.All Student\n2.All Teacher\n3.Pending request")
        z=int(input("Enter your choice"))

        if(z==1):

            # Open database connection
            db = pymysql.connect("localhost", "root", "", "tutorial")

            # prepare a cursor object using cursor() method
            cursor = db.cursor()

            # Prepare SQL query to INSERT a record into the database.
            sql = "SELECT * FROM student"
            try:
                # Execute the SQL command
                cursor.execute(sql)
                # Fetch all the rows in a list of lists.
                results = cursor.fetchall()
                print("id name area time status")
                for row in results:
                    id = row[0]
                    name = row[1]
                    area = row[2]
                    sub = row[3]
                    time = row[4]
                    status = row[5]
                    # Now print fetched result

                    print(id, end=" ")
                    print(name, end="      ")
                    print(area, end="    ")
                    print(sub, end="   ")
                    print(time, end="    ")
                    print(status, end="\n")



            except:
                print("Error: unable to fetch data")

            # disconnect from server
            db.close()
            return ("sucessgul")


        elif (z == 2):
            # Open database connection
            db = pymysql.connect("localhost", "root", "", "tutorial")

            # prepare a cursor object using cursor() method
            cursor = db.cursor()

            # Prepare SQL query to INSERT a record into the database.
            sql9 = "SELECT * FROM teacher"
            try:
                # Execute the SQL command
                cursor.execute(sql9)
                # Fetch all the rows in a list of lists.
                results = cursor.fetchall()
                print("id name area time phone")
                for row in results:
                    tid = row[0]
                    tname = row[1]
                    area = row[2]
                    sub = row[3]
                    time = row[4]
                    phone = row[5]
                    # Now print fetched result

                    print(tid, end=" ")
                    print(tname, end="      ")
                    print(area, end="    ")
                    print(sub, end="   ")
                    print(time, end="    ")
                    print(phone, end="\n")



            except:
                print("Error: unable to fetch data")

            # disconnect from server
            db.close()
            return ("sucessgul")


        elif(z==3):
            # Open database connection
            db = pymysql.connect("localhost", "root", "", "tutorial")

            # prepare a cursor object using cursor() method
            cursor = db.cursor()

            # Prepare SQL query to INSERT a record into the database.
            sql7 = "SELECT * FROM student where status='pending'"


            try:
                # Execute the SQL command
                cursor.execute(sql7)
                # Fetch all the rows in a list of lists.
                results = cursor.fetchall()
                print("id name area time status")
                for row in results:
                    id = row[0]
                    name = row[1]
                    area = row[2]
                    sub = row[3]
                    time = row[4]
                    status = row[5]
                    # Now print fetched result

                    print(id, end=" ")
                    print(name, end="      ")
                    print(area, end="    ")
                    print(sub, end="   ")
                    print(time, end="    ")
                    print(status, end="\n")



            except:
                print("Error: unable to fetch data")

            # disconnect from server
            db.close()


            db = pymysql.connect("localhost", "root", "", "tutorial")


            cursor = db.cursor()

            # Prepare SQL query to INSERT a record into the database.
            sq33 = "SELECT COUNT(id) FROM student where status='pending'"

            try:
                # Execute the SQL command
                cursor.execute(sq33)
                # Fetch all the rows in a list of lists.
                results1 = cursor.fetchall()

                for row in results1:
                    id = row[0]

                if (id==0):
                    return("No request pending")

                else:


                    print("\nTotal request pending:", end="")
                    print(id)

                    x = input("Do you want to assign request(Y/N)")

                    if (x.lower() == "y"):
                        Appoint.appoint()

                    return ("Done")







                    # Now print fetched result





            except:
                print("Sorry! No tutor found for you,your request is still pending...")








            # disconnect from server
            db.close()
            return ("Exit sucessful")



        else:
            print("Invalid Choice")















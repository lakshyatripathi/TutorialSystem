import pymysql

def student():
    print("1.New\n2.Existing")
    x = int(input("Enter your choice:"))

    status = "pending"
    id = 1001

    if (x == 1):
        name = input("Enter your name:")
        sub = input("Enter the subject you want to study:")
        ch=int(input("1.Morning\n2.Afternoon\n3.Evening\nEnter your time slot:"))
        if (ch==1):
            time="Morning"
        elif (ch==2):
            time="Afternoon"
        elif(ch==3):
            time="Evening"
        else:
            print(("Invalid Choice"))

        area = input("Enter your locality")
        time = time.lower()
        sub = sub.lower()
        area = area.lower()
        name = name.lower()
        db = pymysql.connect("localhost", "root", "", "tutorial")
        ll = db.cursor()
        sql3 = """SELECT MAX(id) FROM student"""
        ll.execute(sql3)
        rlt = ll.fetchone()
        id = rlt[0]
        id = int(id)
        id += 1
        print("Your Id is",id)
        id=str(id)

        cursor = db.cursor()
        sql = """INSERT INTO student (id, name, area, subject,time,status) 
                                    VALUES (%s, %s, %s, %s, %s, %s) """
        recordTuple = (id, name, area, sub, time, status)
        try:

            cursor.execute(sql, recordTuple)

            db.commit()
        except:

            db.rollback()

        db.close()

    elif (x == 2):
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


                if(row[0]=="pending"):
                    print("Your request is pending")
                    return(0)
                else:

                    ab = pymysql.connect("localhost", "root", "", "tutorial")
                    cursor = ab.cursor()
                    abc = "SELECT tname,phone from teacher where tid=%s"

                    cursor.execute(abc, row)
                    x = cursor.fetchone()
                    a = x[0]
                    b = x[1]
                    print("Your Faculty Name is:", a)
                    print("Your faculty contact number is:", b)
                    print("Please contact the faculty for more info")
                    ab.close()





        except:
            print("Error: unable to fetch data")

        db.close()
    else:
        print("Invalid Choice")








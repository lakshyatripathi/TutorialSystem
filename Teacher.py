#! usr/bin/env python3

import pymysql

def teacher():
    print("1.New\n2.Existing")
    a = int(input("Enter your choice:"))
    tid = 101
    if (a == 1):
        tname = input("Enter your name:")
        subj = input("Enter subject you teach:")
        are = input("Enter your locality:")
        ch = int(input("1.Morning\n2.Afternoon\n3.Evening\nEnter your time slot:"))
        if (ch == 1):
            tim = "Morning"
        elif (ch == 2):
            tim = "Afternoon"
        elif (ch == 3):
            tim = "Evening"
        else:
            print(("Invalid Choice"))
        ph = int(input("Enter your contact no:"))
        tname = tname.lower()
        subj = subj.lower()
        are = are.lower()
        tim = tim.lower()

        db = pymysql.connect("localhost", "root", "", "tutorial")
        lp = db.cursor()
        sql4 = """SELECT MAX(tid) FROM teacher"""
        lp.execute(sql4)
        rlt = lp.fetchone()
        tid = rlt[0]
        if (tid == None):
            tid = 101
        else:
            tid = int(tid)
            tid += 1

        cursor = db.cursor()
        sql = """INSERT INTO teacher (tid, tname, area, subject,time,phone) 
                                       VALUES (%s, %s, %s, %s, %s, %s) """
        recordTuplea = (tid, tname, are, subj, tim, ph)
        print("Your Teacher id is:",tid)
        try:

            cursor.execute(sql, recordTuplea)

            db.commit()
        except:

            db.rollback()

        db.close()

    if (a == 2):
        z = int(input("Enter your id:"))
        db = pymysql.connect("localhost", "root", "", "tutorial")

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        sql1 = "SELECT count(id) FROM student WHERE status = %s"

        try:
            # Execute the SQL command
            cursor.execute(sql1, z)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:
                a=row[0]

            if (a==0):
                print("No students For You")
                return(0)

            else:

                print("No of student in your class:",a)

        except:
            print("Unable to fetch data")

    if (a == 3):
        print("Invalid choice")





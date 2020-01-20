import pymysql
import Appoint2

id = []
sub = []
area = []
tim = []


def appoint():




    db = pymysql.connect("localhost", "root", "", "tutorial")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()


    sql7 = "SELECT id,subject ,area,time FROM student where status='pending'"

    try:

        cursor.execute(sql7)
        results = cursor.fetchall()
        for row in results:
            id.append(row[0])
            sub.append(row[1])
            area.append(row[2])
            tim.append(row[3])
    except:
        print("Error: unable to fetch data")
    db.close()



    Appoint2.appoint2()


import pymysql
import Appoint
def appoint2():
    i = 0

    for id in Appoint.id:
        q = 1

        db = pymysql.connect("localhost", "root", "", "tutorial")

        cursor = db.cursor()

        # Prepare SQL query to INSERT a record into the database.

        cursor.execute("SELECT tid,tname FROM teacher where area=%s and subject=%s and time=%s",
                       (Appoint.area[i], Appoint.sub[i], Appoint.tim[i]))
        result = cursor.fetchall()
        print("Teachers available for student:", id)
        i += 1


        for row in result:
            if (result == ""):
                print("No tutor found for student")

            else:
                name = row[1]
                ttid = row[0]
                print(ttid, ".", name)
                q += 1

        x = int(input("Enter the teacher id you want to appoint to student:"))

        pq = pymysql.connect("localhost", "root", "", "tutorial")

        cursor = pq.cursor()
        cursor.execute("UPDATE student set status=%s where id=%s", (x, id))
        pq.commit()
        pq.close()

        db.close()




import Student
import Admin
import Teacher
while True:

    print("1.Student\n2.Teacher\n3.Admin\n4.Exit")
    t = int(input("Enter your choice:"))
    if (t == 1):
        Student.student()
    elif (t == 2):
        Teacher.teacher()

    elif (t == 3):
        pas = int(input("Enter the admin password:"))
        p=Admin.admin(pas)
        print(p)

    elif (t==4):
        exit(0)

    else:
        print("Invalid choice")


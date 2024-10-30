#Nathan Hughes
#M02 Lab Project.py
#The code decides if a student with the appropriate GPA will be in Honor Roll or the Dean's list
#the lastName variable holds the student's last name as a string
#the firstName variable holds the student's first name as a string
#the gpa variable holds the student's gpa as a float, which is input from the user

lastName = input("Student Last Name: ")
while lastName != "ZZZ":
    firstName = input("Student First Name: ")
    gpa = float(input(f"{lastName}'s GPA: "))
    if gpa >= 3.5:
        print(f"{lastName}, {firstName} made the Dean's List")
    elif gpa >= 3.25:
          print(f"{lastName}, {firstName} made the Honor Roll")
    else:
         print(f"{lastName}, {firstName} did not make Dean's List or Honor Roll")
         print()
    print("Enter another student's last name below")
    lastName = input("Student's last name: ")
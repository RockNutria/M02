#3/31/2024
#Zachary Bergman
#this program allows names and gpa to be entered in and then returns wether or not the student meets requirements for honors or deans list
deans_list_count = 0
honor_roll_count = 0

while True:
    last_name = input("Enter student's last name (enter 'ZZZ' to quit): ")
    if last_name == 'ZZZ':
        print(f"Summary: {deans_list_count} student(s) made the Dean's List and {honor_roll_count} student(s) made the Honor Roll.")
        break
    first_name = input("Enter student's first name: ")
    try:
        gpa = float(input("Enter student's GPA: "))
    except ValueError:
        print("Please enter a valid GPA.")
        continue
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
        deans_list_count += 1
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
        honor_roll_count += 1
    else:
        print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")

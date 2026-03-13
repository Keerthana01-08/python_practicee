students = {}

while True:
    print("\n1.Add Student")
    print("2.View Students")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        students[name] = marks

    elif choice == "2":
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == "3":
        break

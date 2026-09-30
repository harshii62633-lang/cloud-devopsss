# Student Management System

students = []


def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")

    # Check if ID already exists
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")


def display_students():
    print("\n--- All Students ---")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("-------------------------")
        print("ID     :", student["id"])
        print("Name   :", student["name"])
        print("Age    :", student["age"])
        print("Course :", student["course"])
        print("Marks  :", student["marks"])


def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("ID     :", student["id"])
            print("Name   :", student["name"])
            print("Age    :", student["age"])
            print("Course :", student["course"])
            print("Marks  :", student["marks"])
            return

    print("Student not found.")


def update_student():
    print("\n--- Update Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:

            print("Leave a field empty if you don't want to change it.")

            name = input("Enter new name: ")
            age = input("Enter new age: ")
            course = input("Enter new course: ")
            marks = input("Enter new marks: ")

            if name != "":
                student["name"] = name

            if age != "":
                student["age"] = int(age)

            if course != "":
                student["course"] = course

            if marks != "":
                student["marks"] = float(marks)

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def calculate_average():
    print("\n--- Average Marks ---")

    if len(students) == 0:
        print("No students available.")
        return

    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)

    print("Average Marks:", average)


def show_top_student():
    print("\n--- Top Student ---")

    if len(students) == 0:
        print("No students available.")
        return

    top_student = students[0]

    for student in students:
        if student["marks"] > top_student["marks"]:
            top_student = student

    print("Top Student")
    print("ID     :", top_student["id"])
    print("Name   :", top_student["name"])
    print("Course :", top_student["course"])
    print("Marks  :", top_student["marks"])


def main():
    while True:
        print("\n==============================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Average Marks")
        print("7. Show Top Student")
        print("8. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            calculate_average()

        elif choice == "7":
            show_top_student()

        elif choice == "8":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
main()

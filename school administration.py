class Student:
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_no, grade):
        student = Student(name, roll_no, grade)
        self.students.append(student)

    def remove_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                return True
        return False

    def get_student_details(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                return f"Name: {student.name}\nRoll No: {student.roll_no}\nGrade: {student.grade}"
        return "Student not found."

    def get_all_students(self):
        student_list = "Student List:\n"
        for student in self.students:
            student_list += f"Name: {student.name}\tRoll No: {student.roll_no}\tGrade: {student.grade}\n"
        return student_list

def main():
    school = School()

    while True:
        print("\n--- School Administration System ---")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Get Student Details")
        print("4. View All Students")
        print("5. Quit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            name = input("Enter name: ")
            roll_no = int(input("Enter roll no: "))
            grade = input("Enter grade: ")
            school.add_student(name, roll_no, grade)
            print("Student added successfully!")

        elif choice == 2:
            roll_no = int(input("Enter roll no: "))
            if school.remove_student(roll_no):
                print("Student removed successfully!")
            else:
                print("Student not found.")

        elif choice == 3:
            roll_no = int(input("Enter roll no: "))
            print(school.get_student_details(roll_no))

        elif choice == 4:
            print(school.get_all_students())

        elif choice == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

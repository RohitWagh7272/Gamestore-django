class Student:
    def __init__(self, name, roll_number, age, grade):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.grade = grade

class StudentDatabase:
    def __init__(self):
        self.students = []

    def insert_student(self, student):
        self.students.append(student)

    def update_student(self, roll_number, updated_student):
        for i, student in enumerate(self.students):
            if student.roll_number == roll_number:
                self.students[i] = updated_student
                break

    def delete_student(self, roll_number):
        self.students = [student for student in self.students if student.roll_number != roll_number]

    def view_all_students(self):
        return self.students

class StudentManagement:
    def __init__(self):
        self.db = StudentDatabase()

    def insert_student(self, name, roll_number, age, grade):
        student = Student(name, roll_number, age, grade)
        self.db.insert_student(student)

    def update_student(self, roll_number, name=None, age=None, grade=None):
        for student in self.db.view_all_students():
            if student.roll_number == roll_number:
                if name:
                    student.name = name
                if age:
                    student.age = age
                if grade:
                    student.grade = grade
                break
        else:
            print("Student not found.")

    def delete_student(self, roll_number):
        self.db.delete_student(roll_number)

    def view_all_students(self):
        return self.db.view_all_students()

# Example
management = StudentManagement()

# Inserting a student
management.insert_student("Raj", 101, 15, "A")

# Updating a student
management.update_student(101, name="Aniket", age=16)


# Viewing all students
all_students = management.view_all_students()
for student in all_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, Age: {student.age}, Grade: {student.grade}")

management.delete_student(101)
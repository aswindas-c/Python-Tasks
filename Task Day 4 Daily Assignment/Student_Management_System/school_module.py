class Student:
    def __init__(self,student_id,name):
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.average = 0
    def add_grade(self):
        print("Enter 5 Student Grades : ")
        i = 0
        while i<5:
            try:
                grade = int(input())
                if grade < 0 or grade > 100:
                    raise ValueError
                self.grades.append(grade)
                i = i + 1
            except ValueError:
                print("Invalid input. Please enter a grade between 0 and 100.")
        self.calculate_average_grade()
        return self.grades
    def calculate_average_grade(self):
        avg = sum(self.grades)/len(self.grades)
        if avg >= 90:
            self.average = 'A'
        elif avg >=80:
            self.average = 'B'
        elif avg >= 70:
            self.average = 'C'
        elif avg >= 60:
            self.average = 'D'
        elif avg >= 50:
            self.average = 'P'
        else:
            self.average = 'F'

    def display_details(self):
            print(f"Name : {self.name}")
            print(f"Grades : {self.grades}")
            print(f"Average Grade : {self.average}")
class School:
    def __init__(self):
        self.students = {}
    def add_student(self,student):
        self.students[student.student_id] = student
    def remove_student(self,student_id):
        del self.students[student_id]
        print(f"Student with id {student_id} removed successfully")
    def search_student(self,student_id):
        print("Student Found Details :")
        print(f"Name : {self.students[student_id].name}")
        print(f"Grades : {self.students[student_id].grades}")
        print(f"Average Grade : {self.students[student_id].average}")
    def display_students(self):
        for student in self.students.values():
            yield student
    def get_student_by_id(self,student_id):
        if self.students.get(student_id) is None:
            raise KeyError("Student not found")
        else:
            return self.students.get(student_id)

class AdvancedSchool(School):
    def above_average(self):
        for student in self.students.values():
            if student.average <= 'D':
                print(f"Name = {student.name} Average Grade = {student.average}")
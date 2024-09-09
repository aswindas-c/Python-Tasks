import school_module as sm
class Main:
    student_id_counter = 1
    sc = sm.AdvancedSchool()
    student_instances = {}
    try:
        while True:
            print("1.Add student")
            print("2.Add Student Grades")
            print("3.Remove a student")
            print("4.Display Student Details")
            print("5.Above Average  Students")
            print("6.Search Student")
            print("7.Display all students using iterator")
            print("8.Exit")
            try:
                choice = int(input())
                if choice == 1:
                    name = input("Enter Student Name : ")
                    student_id = student_id_counter
                    student = sm.Student(student_id,name)
                    student_instances[student_id] = student
                    sc.add_student(student)
                    student_id_counter += 1
                elif choice == 2:
                    try:
                        student_id = int(input("Enter Student id : "))
                        if student_id in sc.students.keys():
                            student = student_instances[student_id]
                            student.add_grade()
                        else:
                            print(f"Student with {student_id} not exits")
                    except ValueError:
                        print("Enter Integer Student Id")
                elif choice == 3:
                    try:
                        student_id = int(input("Enter Student Id : "))
                        if student_id in sc.students.keys():
                            sc.remove_student(student_id)
                        else:
                            raise KeyError(f"Student with id {student_id} does not exist")
                    except ValueError:
                        print("Enter Integer Student id")
                    except KeyError as e:
                        print(f"Error : {e}")
                elif choice == 4:
                    try:
                        student_id = int(input("Enter student id : "))
                        if student_id in sc.students.keys():
                            student = student_instances[student_id]
                            student.display_details()
                        else:
                            print(f"Student with id {student_id} not found")
                    except ValueError:
                        print("Enter Integer Student id")
                elif choice == 5:
                    sc.above_average()
                elif choice == 6:
                    try:
                        student_id = int(input("Enter Student id : "))
                        if student_id in sc.students.keys():
                            sc.search_student(student_id)
                        else:
                            raise KeyError("No students found")
                    except ValueError:
                        print("Enter Integer Student id")
                    except KeyError as e:
                        print(f"Error : {e}")
                elif choice == 7:
                    students = sc.display_students()
                    student_iterator = iter(students)
                    student = next(student_iterator)
                    print(f"Name : {student.name}")
                    print(f"Grades : {student.grades}")
                    print(f"Average Grade : {student.average}")
                    while True:
                        print("\n1. Next Student")
                        print("2. Quit")
                        choice = input("Enter your choice: ")
                        if choice == "1":
                            try:
                                book = next(student_iterator)
                                print(f"Name : {student.name}")
                                print(f"Grades : {student.grades}")
                                print(f"Average Grade : {student.average}")
                            except StopIteration:
                                print("No more books available.")
                                break
                        elif choice == "2":
                            break
                        else:
                            print("Invalid choice. Please try again.")

                elif choice == 8:
                    exit()
            except ValueError:
                print("Enter Valid choice ")
    except Exception as e:
        print(e)
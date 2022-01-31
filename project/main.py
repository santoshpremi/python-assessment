from re import I
from prettytable import PrettyTable
from grade import Grade
from student import Student
import os
import sys
import json


class Manage:
    def __init__(self):

        self.students = []
        self.files = []
        self.grades = []
        self.selected_grade = ""
        self.selected_grade_name = ""

    def load_files(self):

        if (os.path.isdir("project/records")):
            files = os.listdir('project/records')
            if (len(files) == 0):
                print("No grades available. Please create one first:")
                return False

            names = []
            for v in files:
                with open("project/records/{}".format(v)) as file:
                    file_content = json.load(file)
                    names.append(file_content.get('name'))
            self.grades = names
            self.files = files
            return True

        print("No records found")
        return False

    def load_grade(self):
        with open("project/records/{}".format(self.selected_grade), "r") as file_content:
            content = json.load(file_content)
            students = content.get('students')
            self.students = [
                Student(
                    i['first_name'],
                    i['last_name'],
                    i['roll'],
                    i['age'],
                    i['major']
                ) for i in students]

    def show_menu(self):

        print("\n========================================\n")
        print('1. create a class')
        print('2. manage the class')
        print('3. delete the class')
        print('0. quit application')
        print("\n========================================\n")

    def rename_class(self):
        name = int(input("select Grade No. : "))
        grade_name = "Grade {}".format(name)
        if grade_name in self.grades:
            print("Grade already exists")
        else:
            print("Name changed successfully!!")
            os.rename("project/records/{}".format(self.selected_grade),
                      "project/records/grade{}.json".format(name))

            self.selected_grade_name = grade_name
            self.selected_grade = "grade{}.json".format(name)
            self.save_grade()
            self.load_files()

    def has_students(self):
        print("\n======================================\n")
        if len(self.students) == 0:
            print("No students in database")
            return False
        print("\n======================================\n")
        return True

    def list_students(self):
        print("\n======================================\n")
        if len(self.students) == 0:
            print("No students in database")
            return
        table = PrettyTable(['Full name', 'Roll',  'Age', 'Major'])

        for i in self.students:
            table.add_row(
                [i.first_name + " " + i.last_name, i.roll, i.age, i.major])

        print("\n======================================\n")
        print(table)

    def save_grade(self):
        filename = "project/records/{}".format(self.selected_grade)
        data = {
            "name": self.selected_grade_name,
            "students": [{"first_name": i.first_name,  "last_name": i.last_name,
                          "roll": i.roll, "age": i.age, "major": i.major} for i
                         in self.students]
        }
        with open(filename, "w") as f:
            f.write(json.dumps(data))
            print("\nData updated !! \n")

    def show_manage_menu(self):
        print("\n================================\n")
        for i, v in enumerate(self.grades):
            print("{} {}".format(i+1, v))
        print("0. Exit application")
        print("9. Go to main menu")

    def modify_student(self):

        has_student = self.has_students()
        if not has_student:
            return

        roll = int(input("Enter roll of student to modify: "))
        for i in self.students:
            if i.roll != roll:
                print("no record found")
            else:

                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                age = int(input("Age: "))
                roll = int(input("Roll: "))
                major = input("Major (science or math or computer): ")

                i.first_name = first_name
                i.last_name = last_name
                i.age = age
                i.roll = roll
                i.major = major

                self.save_grade()

    def show_class_manage_menu(self):
        print("\n========================================\n")
        print("{} manage console".format(self.selected_grade_name))
        print("1. Rename the class")
        print("2. List Students")
        print("3. Add Student")
        print("4. Remove Student")
        print("5. Modify Student")
        print("0. Go to main menu")
        print("9. Quit application")
        print("\n========================================\n")

    def del_student(self):
        has_student = self.has_students()
        if not has_student:
            return

        roll = int(input("Enter roll of student to be delete: "))
        for i in self.students:
            if i.roll == roll:
                self.students.remove(i)
            else:
                print("Not found")
        self.save_grade()

    def add_student(self):
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        age = int(input("Age: "))
        roll = int(input("Roll: "))
        major = input("Major (science or math or computer): ")
        student = Student(first_name, last_name, roll, age, major)
        self.students.append(student)
        self.save_grade()

    def run(self):
        while True:
            self.show_menu()
            choice = int(input("\nplease enter your choice: "))

            if choice == 0:
                sys.exit()

            if choice == 1:            #creating the new grade 
                grade = int(input("\nEnter Class Name: Grade "))

                if not os.path.exists('project/records'):
                    os.makedirs('project/records')

                if os.path.exists('project/records/grade{}.json'.format(grade)):
                    print("Grade already exists !!")
                    continue

                with open("project/records/grade{}.json".format(grade), "w") as content:
                    data = {
                        "name": "Grade {}".format(grade),
                        "students": []
                    }
                    content.write(json.dumps(data))
                    print("\nGrade {} Created Successfully".format(grade))

                print("==================================== \n")
                continue

            if choice == 2:
                loaded = self.load_files()
                if (not loaded):
                    continue

                while True:
                    self.show_manage_menu()
                    choice = int(input("\nSelect an option: "))

                    if choice not in [0, 9]:
                        self.selected_grade = self.files[choice - 1]
                        self.selected_grade_name = self.grades[choice - 1]
                        self.load_grade()
                        while True:

                            self.show_class_manage_menu()
                            choice = int(input("\nSelect an option: "))

                            if choice == 1:
                                self.rename_class()
                            elif choice == 2:
                                self.list_students()
                            elif choice == 3:
                                self.add_student()
                            elif choice == 4:
                                self.del_student()
                            elif choice == 5:
                                self.modify_student()
                            elif choice == 9:
                                sys.exit()
                            else:
                                break

                    elif choice == 0:
                        sys.exit()
                    else:
                        break
            elif choice == 3:
                self.load_files()
                while True:
                    grade =int(input("Enter the grade integer, Want to delete:"))
                    for i in self.files:
                        if i  == "grade{}.json".format(grade):
                            os.remove("project/records/{}".format(i))
                            break
                    break

            else:
                continue  
                print("please enter the available choice")

                




if __name__ == "__main__":
    manager = Manage()
    manager.run()

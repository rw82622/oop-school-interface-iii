from classes.person import Person
import csv

class Student(Person):
    students_list = []
    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, password, role)
        self.school_id = school_id
    
    @classmethod
    def all_students(self):
        with open("./data/students.csv") as file:
            students = csv.reader(file)
            student_data = {}
            for row in students:
                if row[0] != "name":
                    student_data['name'] = row[0]
                    student_data['age'] = row[1]
                    student_data['role'] = row[2]
                    student_data['school_id'] = row[3]
                    student_data['password'] = row[4]
                    Student.students_list.append(Student(**student_data))
        return Student.students_list
    
    def __str__(self):
        return f'{self.name}\n---------------\nage: {self.age}\nid: {self.school_id}'
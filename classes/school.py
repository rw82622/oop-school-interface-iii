from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()
        
    def list_students(self):
        for index in range(len(self.students)):
            print(f'{index+1}. {self.students[index][0]} {self.students[index][3]}')
            
    def find_student_by_id(self, student_id):
        student = []
        for item in self.students:
            if item[3] == student_id:
                student = item
                break
        return student

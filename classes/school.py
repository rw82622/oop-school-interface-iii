from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()
        
    def list_students(self):
        for index, student in enumerate(self.students):
            print(f'{index+1}. {student.name} {student.school_id}')
            
    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student
    
    def add_student(self, student):
        the_student = Student(**student) 
        self.students.append(the_student)
        
    def delete_student(self, input_id):
        for i, student in enumerate(self.students):
            if student.school_id == input_id:
                self.students.pop(i)

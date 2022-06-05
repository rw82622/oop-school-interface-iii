from classes.person import Person
import csv

class Staff(Person):
    staff_list = []
    def __init__(self, name, age, password, role, employee_id):
        super().__init__(name, age, password, role)
        self.employee_id = employee_id
    
    @classmethod        
    def all_staff(self):
        with open("./data/staff.csv") as file:
            staff = csv.reader(file)
            for row in staff:
                if row[0] != "name":
                    Staff.staff_list.append(row)
        return Staff.staff_list
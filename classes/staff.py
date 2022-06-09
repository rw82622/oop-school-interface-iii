from classes.person import Person
import csv

class Staff(Person):
    staff_list = []
    def __init__(self, name, age, role, password, staff_id):
        super().__init__(name, age, role, password)
        self.staff_id = staff_id
    
    @classmethod        
    def all_staff(self):
        with open("./data/staff.csv") as file:
            staff = csv.reader(file)
            staff_data = {}
            for row in staff:
                if row[0] != "name":
                    staff_data['name'] = row[0]
                    staff_data['age'] = row[1]
                    staff_data['role'] = row[2]
                    staff_data['staff_id'] = row[3]
                    staff_data['password'] = row[4]
                    Staff.staff_list.append(Staff(**staff_data))
        return Staff.staff_list
class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f'{self.name} = {self.position}'

    @staticmethod
    def is_valid_postion(position):
        valid_psitions = ['manager','Cashier','Cook','Janitor']
        return position in valid_psitions


employee1 = Employee('Eugene','Manager')
employee2 = Employee('Squidward','Cashier')
employee3 = Employee('spongebob','cook')

print(Employee.is_valid_postion("Rocket Science"))


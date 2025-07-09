#they are shared among all instances
#defined outside ofthe constructor
#shared by all instances

class Student:
    clss_year = 2024
    num_of_students = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_of_students += 1
        #NOTE that while accessing the class variable associate it with the class like you associate instance variables in nvchad 


print('WElCOME꧁ ꧂  TO OUR PROGRAM USER')
student1 = Student("【newton 😅】",21)
student2 = Student('❨olinda 🍎❩',23)


print(f'{student1.name} you are {student1.age} years old')
print(f'{student2.name} you are {student2.age} years old')
print(f'In your clas you are a total of {Student.num_of_students} students.')
print('so far we have everything smooth so far 😜')

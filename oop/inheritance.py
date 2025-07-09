#involves extending the base class by mor especific child classes 
class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

#In our code we have one major class and thre child classes all that descend from the Animal class

class Dog(Animal):#dog is inheriting from Animal
    pass #this says that the intended code will be written later 

class Cat(Animal):
    pass

class Mouse(Animal):
    pass


dog = Dog('Scobby')
cat = Cat('kanyau')
mouse = Mouse('mickey')

print(f'The dog(🐕) is named {dog.name}')
print(f"The cat's(🐱) name is {cat.name}")
print(f'The mice(🐁) name is {mouse.name}')

print()

dog.sleep()
cat.sleep()
mouse.sleep()






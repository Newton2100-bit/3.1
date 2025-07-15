from abc import ABC, abstractmethod

class Animal(ABC):  # Inherit from ABC
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def make_sound(self):
        pass  # Must be implemented by subclasses
    
    @abstractmethod
    def move(self):
        pass
    
    # Regular methods are allowed
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
    def move(self):
        return "Running on four legs"

class Bird(Animal):
    def make_sound(self):
        return "Tweet!"
    
    def move(self):
        return "Flying with wings"

# Usage
# animal = Animal("Generic")  # TypeError: Can't instantiate abstract class

dog = Dog("Buddy")
print(dog.make_sound())  # "Woof!"
dog.sleep()              # "Buddy is sleeping"

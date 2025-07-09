# Base class (Level 1)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Generic animal sound"

# Intermediate class (Level 2 - inherits from Animal)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class (Level 3 - inherits from Dog)
class GoldenRetriever(Dog):
    def fetch(self):
        return f"{self.name} fetches the ball!"

# Create instances
animal = Animal("Generic")
dog = Dog("Buddy")
golden = GoldenRetriever("Max")

# Test inheritance chain
print(animal.speak())
print(dog.speak())
print(golden.speak())
print(golden.fetch())

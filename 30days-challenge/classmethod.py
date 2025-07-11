class Person:
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def get_species(cls):  # cls refers to the class
        return cls.species
    
    @classmethod
    def from_string(cls, person_str):  # Alternative constructor
        name, age = person_str.split('-')
        return cls(name, int(age))  # Create new instance

print(Person.get_species())         # Homo sapiens
person = Person.from_string("John-25")
print(person.name, person.age)      # John 25

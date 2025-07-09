#we have a child class inherit from multiple base classes 
class Prey:
    def flee(self):
        print('This animal is fleeing')

class Predator:
    def hunt(self):
        print('This animal is hunting')

class Rabbit(Prey,):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

print(f'we have rabbit only inherriting from Prey and hence we can have')
print("\t", end="")
rabbit.flee()
print(f'we hav also hawk inherriting from Predator and hence we can have')
print("\t", end="")
hawk.hunt()
print(f'we have then the fish inherriting from two base classes that is the Prey and the Predator')
print('for that we have it having access to both hunt an flee as below')
print("\t", end="")
fish.flee()
print("\t", end="")
fish.hunt()

print()
print('That was our humble multiple inheritance tutoruial')



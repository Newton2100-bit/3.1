from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def stop(self):
        print(f'You stop the car after driving')

    def go(self):
        print(f'You drive the vehicle')


car: Car = Car()
car.go()
car.stop()

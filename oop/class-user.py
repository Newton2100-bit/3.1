from class_def import Car

car1: Car = Car("BMW",2025,'red',False)
print('priting the memory address of our object car1',car1)
print(car1.model)

car2 = Car("volkswargen",2023,'black',True)
print(f'Wehave car two with the following qualities moedel:{car2.model} year:{car2.year} color:{car2.year} and for-sale:{car2.for_sale}')

car2.stop()
car2.describe()
car1.describe()
car1.stop()

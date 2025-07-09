class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year =year
        print('at least we are making progressmy guys')
        self.color = color
        self.for_sale = for_sale
    def drive(self):
        print('You have stoped the',self.model,'car')
    def stop(self):
        print('You have stopped the',self.model,'car')
    def describe(self):
        print('This is a great car thouh you were scammed am sorry')






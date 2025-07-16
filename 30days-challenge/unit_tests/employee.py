class Employee:
    """
    A sample Employee class
    """

    raise_amt = 1.05
    def __init__(self, first, last, pay):
        self.first =  first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        """The email property."""
        #return '{}.{}@email.com'.format(self.first, self.last)
        return f'{self.first}.{self.last}@email.com'

    def apply_raise(self):
        self.pay = int(slef.pay * self.raise_amt)


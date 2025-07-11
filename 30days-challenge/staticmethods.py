class MathUtils:
    @staticmethod
    def add(a, b):  # No self parameter needed
        return a + b
    
    @staticmethod
    def is_even(num):
        return num % 2 == 0

# Can call without creating instance
print(MathUtils.add(5, 3))      # 8
print(MathUtils.is_even(4))     # True

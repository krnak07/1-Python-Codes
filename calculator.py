# class calculator containing calculator operations
class Calculator:

    # method to add two numbers
    def add(self, x: int, y: int): return x + y

    # method to subtract two numbers
    def subtract(self, x: int, y: int): return x - y

    # method to multiply two numbers
    def multiply(self, x: int, y: int): return x * y

    # method to divide two numbers
    def divide(self, x: int, y: int): return x / y


# calculator class object
calObj = Calculator()

# different operations of calculator
print(calObj.add(1, 2))
print(calObj.subtract(1, 2))
print(calObj.multiply(1, 2))
print(calObj.divide(1, 2))

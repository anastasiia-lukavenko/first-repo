class Calculator:

    def add(self, a, b):
        return a + b

    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError("b must not be zero")
        return a / b

    def sub(self, a, b):
        return a - b
    
    def mul(self, a, b):
        return a * b


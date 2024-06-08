class Calculator:
    
    def add(a, b):
        result = a + b
        return result

    def sub(a, b):
        result = a - b
        return result

    def multy(a, b):
        result = a * b
        return result

    def div(a, b):
        if b != 0:
            result = a / b
            return result
        else:
            raise ZeroDivisionError

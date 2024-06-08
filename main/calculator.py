class Calculator:
    def add(a, b):
        result = a + b
        # выполни сложение
        return result

    def sub(a, b):
        result = a - b
        # выполни вычитание
        return result

    def multy(a, b):
        result = a * b
        # выполни умножение
        return result

    def div(a, b):
        result = 0
        # выполни деление (с обработкой случая, когда b = 0)
        if b != 0: result = a / b
        else:
            raise ZeroDivisionError
        return result

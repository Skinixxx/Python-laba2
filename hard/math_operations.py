def add(a, b):
    """Сложение двух чисел"""
    return a + b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def power(base, exponent):
    """Возведение в степень"""
    return base ** exponent

def factorial(n):
    """Вычисление факториала"""
    if n == 0:
        return 1
    return n * factorial(n - 1)
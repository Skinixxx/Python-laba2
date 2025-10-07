def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"Факториал 5: {factorial(5)}")  
print(f"Факториал 0: {factorial(0)}")  
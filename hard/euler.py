def euclidean_algorithm(a, b):
    while b:
        a, b = b, a % b
    return a

num1, num2 = 48, 18
gcd = euclidean_algorithm(num1, num2)
print(f"НОД чисел {num1} и {num2} равен {gcd}")
def sum_odd(n: int):
    result = 0
    for i in range(1, n + 1, 2):
        result += i
    return result

print("Задача по поиску суммы всех нечетных чисел до N.\nВведите N: ", end="")
n = int(input())
print(f"Сумма всех нечетных чисел до N={n} равна {sum_odd(n)}")
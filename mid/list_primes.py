def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_up_to_100() -> list:
    primes = []
    for num in range(2, 101):
        if is_prime(num):
            primes.append(num)
    return primes


primes = primes_up_to_100()
print(f"Простые числа до 100: {primes}")
print(f"Количество простых чисел: {len(primes)}")
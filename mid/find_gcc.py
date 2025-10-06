def find_gcd(fir_num: int, sec_num: int):
    fir_num = abs(fir_num)
    sec_num = abs(sec_num)

    while fir_num > 0 and sec_num > 0:
        if fir_num >= sec_num:
            fir_num %= sec_num
        else:
            sec_num %= fir_num
    return max(fir_num, sec_num)

print("Задача по поиску НОД двух чисел.\n")
fir_num = int(input("Введите первое число: "))
sec_num = int(input("Введите второе число: "))
print(f"НОД равняется:{find_gcd(fir_num=fir_num,sec_num=sec_num)}")

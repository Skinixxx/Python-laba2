SET_VOWELS={
    'а',
    'о',
    'е',
    'и',
    'у',
    'э',
    'я',
    'ю',
    'А',
    'О',
    'Е',
    'И',
    'У',
    'Э',
    'Я',
    'Ю'
}

def counting_vowel(string: str):
    count_vowels=0
    for i in string:
        if i in SET_VOWELS:
            count_vowels+=1
    return count_vowels

print("Задача по нахождению гласных в строке.")
string=input("Введите строку(на русском): ")
print(counting_vowel(n))
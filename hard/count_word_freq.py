def count_word_frequency(filename: str) -> dict:
    
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~«»—'
    cleaned_text = ""
    for char in text:
        if char not in punctuation:
            cleaned_text += char
    words = cleaned_text.split()
    word_counter = {}
    for word in words:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
            
    return word_counter
    

def display_top_words(word_freq: dict, top_n: int = 10):

    word_items = list(word_freq.items())
    for i in range(len(word_items)):
        for j in range(0, len(word_items) - i - 1):
            if word_items[j][1] < word_items[j + 1][1]:
                word_items[j], word_items[j + 1] = word_items[j + 1], word_items[j]
    
    print(f"\nТоп-{top_n} самых частых слов:")
    print("-" * 30)
    for i in range(min(top_n, len(word_items))):
        word, count = word_items[i]
        print(f"{word}: {count}")

filename = "sample_text.txt"
word_frequency = count_word_frequency(filename)

if word_frequency:
    total_words = sum(word_frequency.values())
    unique_words = len(word_frequency)
    
    print(f"Всего слов в тексте: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    display_top_words(word_frequency, 10)
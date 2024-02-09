
# Шифр Цезаря
def ceaser_cipher(word, key, cipher=True):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    word = word.lower()
    res = ''
    
    for ch in word:
        if cipher:
            # шифровать
            res += alpha[(alpha.index(ch) + key) % len(alpha)]
        else:
            # декодировать
            res += alpha[(alpha.index(ch) - key) % len(alpha)]
    
    return res


cipher_dog = ceaser_cipher('dog', 3)
print(f'dog -> {cipher_dog}'); print()

cipher_python = ceaser_cipher('python', 5)
print(f'python -> {cipher_python}'); print()

print(f'{cipher_dog} -> {ceaser_cipher(cipher_dog, 3, False)}', end='\n\n');
print(f'{cipher_python} -> {ceaser_cipher(cipher_python, 5, False)}', end='\n\n');

if __name__ == '__main__':
    print()
    print('END!!!');
    #input();

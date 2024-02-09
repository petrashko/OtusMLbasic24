
# Функция разбивает число на разряды 
def number_filter(num):
    if num < 1000:
        return str(num)

    string_num = str(num)[::-1]
    tmp_list = []
    
    for i in range(0, len(string_num), 3):
        tmp_list.append(string_num[i:i+3])
    
    return ' '.join(tmp_list)[::-1]


print(f'1234567 -> {number_filter(1234567)}', end='\n\n')

print(f'34976 -> {number_filter(34976)}', end='\n\n')

print(f'267 -> {number_filter(267)}', end='\n\n')

print(f'1000 -> {number_filter(1000)}', end='\n\n')

print(f'100 -> {number_filter(100)}', end='\n\n')

print(f'99 -> {number_filter(99)}', end='\n\n')

if __name__ == '__main__':
    print()
    print('END!!!');
    #input();

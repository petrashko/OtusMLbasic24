
# Функция изменяет снейк_кейс на КамелКейс
def snake2camel(string):
    tmp_list = string.split('_')
    res_list = []
    
    for word in tmp_list:
        char_upper = word[0].upper()
        res_list.append( char_upper + word[1:len(word)] )
    
    return ''.join(res_list)


# Функция изменяет КамелКейс на снейк_кейс
def camel2snake(string):
    pos_index = {}
    len_str = len(string)
    
    for i in range(0, len_str):
        if string[i].isupper():
            pos_index[i] = string[i]
    
    # Обработать первый символ
    if 0 in pos_index:
        string = pos_index[0].lower() + string[1:len_str]
        del pos_index[0]
    
    # Обработать последний символ
    last_ind = len_str - 1
    if last_ind in pos_index:
        string = string[0:-1] + '_' + pos_index[last_ind].lower()
        len_str += 1
        del pos_index[last_ind]
    
    for key in sorted(pos_index.keys()):
        string = string[0:key] + '_' + pos_index[key].lower() + string[key+1:len_str]
        len_str += 1
    
    return string
    

print(f'my_first_func -> {snake2camel("my_first_func")}', end='\n\n');

print(f'AnotherFunctionZ -> {camel2snake("AnotherFunctionZ")}', end='\n\n');

if __name__ == '__main__':
    print()
    print('END!!!');
    #input();
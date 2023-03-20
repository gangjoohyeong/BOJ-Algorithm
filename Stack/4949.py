# 균형잡힌 세상
# 4949

while True:
    string = input()
    string2 = ''
    if string == '.':
        break
    
    for s in string:
        if s in '[]()':
            string2 += s
    
    while True:
        if '()' in string2 or '[]' in string2:
            string2 = string2.replace('()', '').replace('[]', '')
        else:
            print('yes') if not string2 else print('no')
            break
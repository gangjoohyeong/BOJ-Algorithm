# 괄호
# 9012

t = int(input())

for _ in range(t):
    VPS = input()
    stack = []
    while VPS:
        if '()' in VPS:
            VPS = VPS.replace('()', '')
        else:
            print('NO')
            break
    else:
        print('YES')
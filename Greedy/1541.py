# 1541
# 잃어버린 괄호
expression = input()
answer = 0
if '-' in expression:
    for idx, val in enumerate(expression.split('-')):
        if idx == 0:
            answer += sum(map(int, val.split('+')))
        else:
            answer -= sum(map(int, val.split('+')))
else:
    answer = sum(map(int, expression.split('+')))
    
print(answer)
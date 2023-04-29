# 1874
# 스택 수열

n = int(input())
stack = []
k = 1
answer = []

for _ in range(n):
    element = int(input())
    while k <= element:
        answer.append('+')
        stack.append(k)
        k += 1
    
    if stack[-1] == element:
        answer.append('-')
        stack.pop()
    else:
        print('NO')
        answer = []
        break
    
for i in answer:
    print(i)
# 14888
# 연산자 끼워넣기

n = int(input())
array = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())


maximum = -1000000000
minimum = 1000000000

def dfs(idx, result):
    global add, sub, mul, div, maximum, minimum
    
    if idx == n:
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        return None

    if add > 0:
        add -= 1
        dfs(idx+1, result + array[idx])
        add += 1
    
    if sub > 0:
        sub -= 1
        dfs(idx+1, result - array[idx])
        sub += 1
    
    if mul > 0:
        mul -= 1
        dfs(idx+1, result * array[idx])
        mul += 1
        
    if div > 0:
        div -= 1
        dfs(idx+1, int(result / array[idx]))
        div += 1

dfs(1, array[0])

print(maximum)
print(minimum)
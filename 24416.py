# 알고리즘 수업 - 피보나치 수 1
# 24416

def fibo(n):
    global cnt1
    if n == 1 or n == 2:
        return 1
    else:
        cnt1 += 1
        return fibo(n-1) + fibo(n-2)
    
def fibonacci(n):
    return n-2

n = int(input())
global cnt1
cnt1 = 1
fibo(n)
print(cnt1, fibonacci(n))
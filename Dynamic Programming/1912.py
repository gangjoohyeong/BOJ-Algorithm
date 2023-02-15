# 연속합
# 1912

n = int(input())
array = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
dp[1] = array[1]

for i in range(2, n+1):
    dp[i] = max(array[i], array[i] + dp[i-1])
print(max(dp[1:]))
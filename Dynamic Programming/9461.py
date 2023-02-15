# 파도반 수열
# 9461

# a_k = a_k-1 + a_k-5

dp = [0] * 101
dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2

t = int(input())

for _ in range(t):
    n = int(input())
    if n <= 5:
        print(dp[n])
        continue
    for i in range(6, n+1):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[n])
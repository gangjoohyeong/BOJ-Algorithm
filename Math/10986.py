# 10986
# 나머지 합

# S_k가 k-1번째 까지의 누적합이라 할 때,
# ( S_(j) - S_(i-1) ) % m == 0인 (i, j)의 개수
# i, j = 0, ..., n-1


# ( S_(j) - S_(i-1) ) % m == 0
# <=> ( S_(j) % m ) - ( S_(i-1) % m) == 0
# <=> S_(j) % m == S_(i-1) % m

from itertools import accumulate
from collections import Counter

answer = 0

n, m = map(int, input().split())
array = list(map(int, input().split()))

cum_array = list(accumulate(array))

remainder_array= list(map(lambda x : x % m, cum_array))
answer += remainder_array.count(0)

for key, val in Counter(remainder_array).items():
    answer += val * (val-1) // 2

print(answer)


# 15649
# N과 M (1)
from collections import deque

n, m = map(int, input().split())
seq = deque([])

def dfs():
    if len(seq) == m:
        print(' '.join(map(str, seq)))
        return
    
    for i in range(1, n+1):
        if i in seq:
            continue
        seq.append(i)
        dfs()
        seq.pop()
dfs()
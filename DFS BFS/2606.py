# 2606
# 바이러스
from collections import deque

n_computer = int(input())
t = int(input())
array = [ [] for _ in range(n_computer + 1) ]

for _ in range(t):
    start, end = map(int, input().split())
    array[start].append(end)
    array[end].append(start)
    
infected = [ False for _ in range(n_computer + 1) ]
queue = deque([1])

while queue:
    now = queue.popleft()
    for val in array[now]:
        if not infected[val]:
            infected[val] = True
            queue.append(val)
infected[1] = False
print(sum(infected))
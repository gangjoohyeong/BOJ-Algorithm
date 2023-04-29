# 1021
# 회전하는 큐

from collections import deque

n, m = map(int, input().split())
array = list(map(int, input().split()))

queue = deque([i for i in range(1, n+1)])

answer = 0
for val in array:
    if queue[0] == val: # rule 1
        queue.popleft()
        n -= 1
        
    elif queue.index(val) <= n / 2: # rule 2
        while queue[0] != val:
            queue.append(queue.popleft())
            answer += 1
        queue.popleft()
        n -= 1
            
    else: # rule 3
        while queue[0] != val:
            queue.appendleft(queue.pop())
            answer += 1
        queue.popleft()
        n -= 1
print(answer)
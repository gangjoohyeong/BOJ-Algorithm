# 큐 2
# 18258

from collections import deque
import sys

queue = deque()

n = int(sys.stdin.readline())

for _ in range(n):
    func = sys.stdin.readline().split()
    
    if func[0] == 'push':
        queue.append(func[1])
        
    elif func[0] == 'pop':
        try:
            print(queue.popleft())
        except IndexError:
            print(-1)
            
    elif func[0] == 'size':
        print(len(queue))
        
    elif func[0] == 'empty':
        print(1 if not queue else 0)
        
    elif func[0] == 'front':
        try:
            print(queue[0])
        except IndexError:
            print(-1)
            
    elif func[0] == 'back':
        try:
            print(queue[-1])
        except IndexError:
            print(-1)
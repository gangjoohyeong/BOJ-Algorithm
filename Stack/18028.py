# 스택
# 10828

import sys


n = int(sys.stdin.readline())
array = []

for _ in range(n):
    input_ = sys.stdin.readline().split()
    func = input_[0]
    
    # push
    if func == 'push':
        x = int(input_[1])
        array.append(x)
        
    else:
        # pop
        if func == 'pop':
            try:
                print(array.pop())
            except IndexError:
                print(-1)
        
        # size
        elif func == 'size':
            print(len(array))
        
        # empty
        elif func == 'empty':
            print(1 if not array else 0)
            
        # top
        elif func == 'top':
            try:
                print(array[-1])
            except IndexError:
                print(-1)
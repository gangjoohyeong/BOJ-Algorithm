# 20920
# 영단어 암기는 괴로워
from collections import Counter
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
words = []
for _ in range(n):
    words.append(sys.stdin.readline().rstrip())
    
words_ = [ word for word in words if len(word) >= m ]
words__ = sorted(Counter(words_).items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for word in words__:
    print(word[0])
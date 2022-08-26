## 백준 : 1021
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
idx = list(map(int, input().split()))
deq = deque([i for i in range(1, n+1)])

count = 0

for i in idx:
    while True:
        if deq[0] == i:
            deq.popleft()
            break
        else:
            if deq.index(i) < len(deq)/2:
                while deq[0] != i:
                    deq.append(deq.popleft())
                    count += 1
            else:
                while deq[0] != i:
                    deq.appendleft(deq.pop())
                    count += 1

print(count)

#@ 백준 : 2164
import sys
from collections import deque
input = sys.stdin.readline

queue = deque([i+1 for i in range(int(input()))])

while(len(queue) > 1):
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])


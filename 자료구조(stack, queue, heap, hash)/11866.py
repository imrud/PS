## 백준 : 11866
from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
que = deque([i for i in range(1, n+1)])
    
print('<', end='')
while len(que) != 0:      ## que가 비어있지 않는 동안
    
    for _ in range(k-1):    ## k번째 전까지 있는 요소 뒤로 보내기
        que.append(que.popleft())

    ## k번째 원소 출력
    print(que.popleft(), end='')

    if que:
        print(', ', end='')

print('>')
            
    

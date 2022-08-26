## 백준 : 2493
import sys
input = sys.stdin.readline

n = int(input())

tower = list(map(int, input().split()))
stack = []
result = [0]*n      ## 정답을 우선 0으로 초기화
                   
for i in range(n):
    while stack:
        if stack[-1][1] > tower[i]:     ## 스택 마지막값과 현재 tower 값과 비교
            result[i] = stack[-1][0]+1
            break
        else:
            stack.pop()
    stack.append((i, tower[i]))     ## 인덱스, 값
            
print(*result)            
    
 

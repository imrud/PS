## 백준 : 10799
import sys

input = sys.stdin.readline

line = list(input().rstrip())
stack = []
count = 0
for i in range(len(line)):
    if line[i] == '(':
        stack.append('(')
        
    else:
        if line[i-1] == '(':    ## 레이저인경우
            stack.pop() ## 마지막 요소 꺼내기
            count += len(stack)
            
        else:
            stack.pop()
            count += 1
            

print(count)
            
    
    

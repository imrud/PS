## [CH4]예제 4-1 : 상하좌우
import sys
input = sys.stdin.readline

n = int(input())
plan = list(input().split())

x, y = 0, 0
for i in range(len(plan)):
    if plan[i] == 'L':
        if y > 0:
            y -= 1
            
    elif plan[i] == 'R':
        if y < n-1:
            y += 1

    elif plan[i] == 'U':      
        if x > 0:
            x -= 1

    else:        
        if x < n-1:
            x += 1



print(x+1, y+1)
            
        
    

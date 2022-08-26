## 백준 10845: 큐
import sys
input = sys.stdin.readline

n = int(input())

queue = []
for _ in range(n):
    line = input().split()

    if line[0] == "push":
        queue.append(line[1])
        
    elif line[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
            
    elif line[0] == "size":
        print(len(queue))
              
    elif line[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
            
    elif line[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
        
    elif line[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

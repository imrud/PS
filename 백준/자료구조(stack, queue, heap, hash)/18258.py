## 백준: 18258
import sys
input = sys.stdin.readline

queue2 = []
front = 0       ## 인덱스 역할

for _ in range(int(input())):
    line = input().split()

    if line[0] == "push":
        queue2.append(line[1])

    elif line[0] == "pop":
        if len(queue2) > front:
            print(queue2[front])
            front += 1
        else:
            print(-1)
            
    elif line[0] == "size":
        print(len(queue2)-front)
        
    elif line[0] == "empty":
        if len(queue2) == front:    ## 비어 있을 경우
            print(1)
            front = 0       ## 초기화
            queue2 = []     ## 초기화
        else:
            print(0)
            
    elif line[0] == "front":
        if len(queue2) > front:
            print(queue2[front])
        else:
            print(-1)
            
    elif line[0] == "back":
        if len(queue2) > front:
            print(queue2[-1])
        else:
            print(-1)
    

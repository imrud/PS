## 백준 : 5430
from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p = input().rstrip()
    n = int(input())
    que = deque(input().rstrip()[1:-1].split(","))  ##',' 기준으로 나누기

    if n == 0:      ## 빈 배열 입력시, 다시 초기화 해줘야함.
        que = []

    flag = 0    ## 뒤집은 여부
    for ac in p:
        if ac == 'R':
            flag += 1
            
        elif ac == 'D':
            if que:
                if flag%2 == 0:      # 'R'이 짝수면 앞에서 제거 
                    que.popleft()
                else:           ## 홀수면 뒤에서 제거
                    que.pop()
                    
            else: ## 빈 배열이면 error 출력 뒤 break
                print('error')
                break

    else:
        if flag%2 == 0:
            print('['+','.join(que)+']')
        else:
            que.reverse()       ## reverse()는 최종적으로 한 번만
            print('['+','.join(que)+']')

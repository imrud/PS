import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    que = list(map(int, input().split()))
    loc = [0 for _ in range(n)]     ## deq 위치 담는 리스트
    loc[m] = 1      ## 찾으려는 문서의 위치만 1로 설정
    

    count = 0
    while True:
        if que[0] == max(que):
            count +=1

            if loc[0] == 1:         ## 찾으려는 문서인 경우
                print(count)
                break
            
            que.pop(0)
            loc.pop(0)

                
        else:
            que.append(que.pop(0))
            loc.append(loc.pop(0))

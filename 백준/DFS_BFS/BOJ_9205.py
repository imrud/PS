import sys
from collections import deque

input = sys.stdin.readline

def calculate(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

def bfs():
    que = deque()
    que.append((home[0], home[1]))      ## deque에 출발 위치(상근이네 집) 넣기

    while que:
        x, y = que.popleft()    ## deque의 맨 앞 요소 꺼내기
        if calculate(x, y, penta[0], penta[1]) <= 1000:   ## 맨해튼 거리가 1000이하일 경우, 현재 좌표에서 펜타까지 한 번에 갈 수 있음
            print("happy")
            return

        for i in range(nConv):
            if not visited[i]:          ## 해당 편의점 방문 전 일 경우
                cx, cy = conv[i]
                if calculate(x, y, cx, cy) <= 1000:  ## 현재 좌표에서 맨해튼 거리가 1000이하인 편의점 방문
                    que.append((cx, cy))    ## 현재 좌표를 편의점으로
                    visited[i] = True   ## 방문처리

    print("sad")
    return



t = int(input())    ## 테스트 케이스 개수
for _ in range(t):
    nConv = int(input())    ## 맥주를 파는 편의점의 개수
    home = list(map(int, input().split()))  ## 상근이네 집 좌표
    conv = []   ## 편의점 좌표를 담을 리스트
    for _ in range(nConv):
        conv.append(list(map(int, input().split())))    ##      편의점 좌표 추가
    penta = list(map(int, input().split()))         ## 펜타포트 락페 좌표
    visited = [False]*nConv     ## 방문확인

    bfs()
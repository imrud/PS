import sys

input= sys.stdin.readline

N, M = map(int, input().split())    ## 행(세로), 열(가로)
r, c, d = map(int, input().split())       ## 현재 위치, 방향
visited = [[0]*M for _ in range(N)]     ## 로봇 청소기 방문 확인

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split()) ))      ## 0 : 현재 청소 X, 1 : 벽

## 방향 전환 : 북, 동, 남, 서(r, c 순서 중요)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[r][c] = 1   ## 현재 위치 방문 완료
count = 1   ## 청소한 영역


while True:
    flag = 0    ## 청소 여부

    for _ in range(4):  ## 로봇이 바라보는 방향 회전
        d = (d+3) % 4   ## 반시계방향으로 회전
        nx = r + dx[d]
        ny = c + dy[d]

        ## 범위 안에 해당, 빈 칸 -> 청소 가능 할 때
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1     ## 방문 확인
                count += 1      ## 청소 수 증가
                ## 현재 위치 바꾸기
                r = nx
                c = ny

                ## 청소를 단 한 방향이라도 했으면 다음으로 넘어간다.
                flag = 1    ## 청소 완료
                break

    if flag == 0:   ## 4방향 모두 청소가 되어 있을 경우
        if graph[r-dx[d]][c-dy[d]] == 1:    ## 후진했는데 벽일 경우
            print(count)    ## 여태까지 청소한 영역의 개수 출력 후 반복문 종료
            break
        else:       ## 후진 가능할 경우
            r, c = r-dx[d], c-dy[d]




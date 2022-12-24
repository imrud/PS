import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())    ## 노드 개수, 간선 개수 입력받기
graph = [[INF] * (n+1) for _ in range(n+1)] ## 2차원 리스트(그래프) 만들고, 모든 값을 무한으로 초기화

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:  ## 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
            graph[a][b] = 0

## 간선 정보 입력받기
for _ in range(m):
    ## A -> B로 가는 비용은 1로 설정
    a, b = map(int, input().split())
    graph[a][b] = 1

## 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = 0  ## 순위를 알 수 있는 학생 수
## 학생 한 명씩 확인하며 번호마다 도달할 수 있는지 체크
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        ## 양 방향으로 모두 도달 가능해야 된다.
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    ## 하나의 번호에서 모든 번호로 도달 가능한 경우에만 순위를 알 수 있다.
    if cnt == n:
        result += 1

print(result)

import sys

input = sys.stdin.readline

n = int(input())    ## 전체 사람의 수
start, end = map(int, input().split())  ## 촌수 계산해야하는 서로 다른 두 사람

graph = [[] for _ in range(n+1)]   ## 가족 관계도
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())    ## 부모, 자식
    graph[x].append(y)
    graph[y].append(x)

visited = [[False] for _ in range(n+1)] ## 방문확인
check = [0]*(n+1)   ## 촌수를 계산할 리스트

def dfs(v):
    for idx in graph[v]:
        if check[idx] == 0:
            check[idx] = check[v] + 1   ## 다음 방문한 노트 가중치 = 현재 방문한 노드의 가중치 + 1
            dfs(idx)

dfs(start)

print(check[end] if check[end] > 0 else -1)
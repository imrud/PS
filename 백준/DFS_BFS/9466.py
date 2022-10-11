## 백준 9466 : 텀프로젝트
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    global result
    visited[x] = 1
    cycle.append(x)     ## cycle에 추가
    val = s_num[x]

    if visited[val] == 0:
        dfs(val)
        
    else:
        if val in cycle:
            result += cycle[cycle.index(val):]
        return

t = int(input())
count = 0   
for _ in range(t):
    n = int(input())    
    s_num = [0] + list(map(int, input().split()))   ## 학생 리스트
    visited = [0 for _ in range(n+1)]   ## 방문 확인
    result = []

    for i in range(1, n+1):
        if visited[i] == 0:
            cycle = []
            dfs(i)        

    print(n - len(result))       

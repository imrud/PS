## 백준 : 1260
import sys
input = sys.stdin.readline



n, m, v = map(int, input().strip().split())

node = dict()
for _ in range(m):
    v1, v2 = map(int, input().strip().split())
    node[v1] = v2
    
    

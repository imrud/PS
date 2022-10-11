## 백준 : 2630
import sys
input = sys.stdin.readline

res = [0, 0]
def solved(x, y, n):
    color = graph[x][y]     ## 시작점의 색을 기준

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != graph[i][j]:
                k = n//2
                solved(x, y, k)
                solved(x, y+k, k)
                solved(x+k, y, k)
                solved(x+k, y+k, k)
                return
            
    if color == 0:      ## color가 '0'으로 판정
        res[0] += 1
        #res.append(0)
    else:               ## color가 '1'로 판정
        res[1] += 1
        #res.append(1)
    




n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

solved(0, 0, n)     ## 시작은 [0, 0](0행 0열)

##print(res.count(0))
##print(res.count(1))
print(res[0])
print(res[1])



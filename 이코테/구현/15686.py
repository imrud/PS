## [CH4] 백준 : 15686 - 치킨배달
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
chicken, house = [], []

for i in range(n):
    area = list(map(int, input().split()))
    for j in range(n):
        if area[j] == 1:
            house.append((i, j))        ## 집 좌표 추가
        elif area[j] == 2:
            chicken.append((i, j))      ## 치킨 집 좌표 추가

## 모든 치킨집 중 m개의 치킨집 조합
cd = list(combinations(chicken, m))
result = []

for c in cd:
    answer = 0
    for hx, hy in house:
        tmp = int(1e9)
        for cx, cy in c:    ## 각 집으로부터 m개 조합의 치킨집과의 최소 치킨거리 구하기
            tmp = min(tmp, abs(hx-cx)+abs(hy-cy))

        answer += tmp
    result.append(answer)

print(min(result))



        
    

##n, m = map(int, input().split())
##area = []
##for _ in range(n):
##    area.append(list(map(int, input().split())))
##
##chicken = []
##for i in range(n):
##    for j in range(n):
##        if area[i][j] == 2:
##            chicken.append((i,j))       ## 치킨집 좌표
##
##
##result = {}
##for i in range(n):
##    for j in range(n):
##        if area[i][j] == 1:         # 집인 경우에만
##            tmp = []
##            m = 0
##            for k in range(len(chicken)):
##                tmp.append(abs(i - chicken[k][0]) + abs(j - chicken[k][1]))
##
##            m = tmp.index(min(tmp)) ## 최소 거리 치킨집
##            if chicken[m] in result:
##                result[chicken[m]].append(min(tmp))
##            
##            else:
##                result[chicken[m]] = [min(tmp)]
##
##
##result = dict(sorted(result.items(), key = lambda x: len(x[1]), reverse=True))
##
##min_road = 0
##cnt = 0
##for key in result:
##    if cnt < m:
##        min_road += sum(result[key])
##    
##    
##
##print(min_road)
        
            
        

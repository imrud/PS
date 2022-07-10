##백준 2667번: 단지 번호 붙이기
import sys
sys.setrecursionlimit(10**6)


## N입력받기
n = int(input())

field = [[]*n for _ in range(n)]
result = []
count = 0    ## 총 단지수


def dfs(x, y):
    global cnt

    ##범위 확인
    if x >= n or x < 0 or y >= n or y < 0:
        return False

    ## 집이 있는 경우
    if field[x][y] == 1:
        cnt += 1        ## 해당 영역의 단지 수 증가
        ## 방문확인
        field[x][y] = -1

        ## 근처에 집 탐색하기
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

for i in range(n):
    tmp = sys.stdin.readline()
    for j in range(n):
        field[i].append(int(tmp[j]))

cnt = 0  ## 영역 내 단지 수
for i in range(n):
    for j in range(n):
        if field[i][j] == 1:        ## 집이 있는 경우
            dfs(i, j)               ## 해당 집 중심으로 근처 탐방
            
            count += 1
            result.append(cnt)
            cnt = 0         ## cnt값 초기화
                 
                        
result.sort()            
print(count)
for i in result:
    print(i)



        
    
    
    

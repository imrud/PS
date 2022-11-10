## 1979. 어디에 단어가 들어갈 수 있을까
T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    area = []

    for i in range(n):
        area.append(list(map(int, input().split())))

    res = 0

    ## 행 탐색
    for i in range(n):
        cnt = 0
        for j in range(n):
            if area[i][j] == 1:
                cnt += 1
            if area[i][j] == 0 or j == n-1:
                if cnt == k:    ## 채우기 가능
                    res += 1
                if area[i][j] == 0:
                    cnt = 0
        
    ## 열 탐색
    for i in range(n):
        cnt = 0
        for j in range(n):
            if area[j][i] == 1:
                cnt += 1
            if area[j][i] == 0 or j == n-1:
                if cnt == k:    ## 채우기 가능
                    res += 1
                if area[j][i] == 0:
                    cnt = 0              



    print('#{} {}'.format(test_case, res))
        

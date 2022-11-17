T = 10

for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_val = 0     ## 가로 최대값

    ## 행
    for i in range(len(arr)):
        #print(arr[i])
        if sum(arr[i]) > max_val:
            max_val = sum(arr[i])
    #print(max_row)

    ## 열
    for i in range(len(arr)):
        tmp = 0
        for j in range(len(arr)):
            tmp += arr[j][i]
        if tmp > max_val:
            max_val = tmp

    ## 대각선 - 정방향
    t_dia = 0
    for i in range(1, len(arr)-1):          ## 2~9번째 대각선 값만 더해놓기
        t_dia += arr[i][i]
        if t_dia > max_val:
            max_val = t_dia

    ## 대각선 - 역방향
    t_dia = 0
    for i in range(1, len(arr) - 1):  ## 2~9번째 대각선 값만 더해놓기
        t_dia += arr[i][99-i]
        if t_dia > max_val:
            max_val = t_dia

    print('#{} {}'.format(test_case, max_val))
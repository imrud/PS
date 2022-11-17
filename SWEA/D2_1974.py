T = int(input())

for test_case in range(1, T + 1):
    arr = []
    ## 입력받기
    for _ in range(9):
        arr.append(list(map(int, input().split())))
    ## arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1          ## 처음 1로 설정하기
    ## 가로 세로 검사
    for i in range(9):
        row = [0] * 10
        column = [0] * 10
        for j in range(9):
            row[arr[i][j]] += 1             ## 행 : i, j
            column[arr[j][i]] += 1          ## 열 : j, i

        # 중복 체크
        for k in range(1, 10):
            if row[k] != 1:
                result = 0      ## 중복일 경우, result = 0으로 하고 break
                break
            if column[k] != 1:
                result = 0
                break

    ## 3*3 격자 검사
    for i in range(3):
        for j in range(3):
            grid = [0] * 10
            for k in range(3):
                for l in range(3):
                    grid[arr[3 * i + k][3 * j + l]] += 1

            ## 중복 체크
            for k in range(1, 10):
                if grid[k] != 1:
                    result = 0
                    break

    print("#{} {}".format(test_case, result))

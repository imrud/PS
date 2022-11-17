T = int(input())

## 우, 하, 좌, 상 (달팽이 이동 방향)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for test_case in range(1, T + 1):
    N = int(input())
    snail_nums = [[0]*N for _ in range(N)]

    ##초기 위치(행, 열), 방향 설정
    r = 0
    c = 0
    dist = 0  # 0:우, 1:하, 2:좌, 3:상

    for n in range(1, N * N + 1):       ## 배열에 1~N*M까지 들어간다
        snail_nums[r][c] = n            ## 숫자 채워나가기
        r += dr[dist]       ## 같은 dist(방향)로 따라 행, 열 이동
        c += dc[dist]

        ## r,c가 배열의 범위 밖 or 다음에 진입하려는 위치가 이미 채워졌을 경우
        if r < 0 or c < 0 or r >= N or c >= N or snail_nums[r][c] != 0:
            # 바로 위에서 증가한 값 이전의 값으로 돌아가기(더한 값 빼기)
            r -= dr[dist]
            c -= dc[dist]

            # 방향 바꾸기
            dist = (dist + 1) % 4

            ## 바꾼 dist(방향)으로 다시 r, c에 값 증가하기
            r += dr[dist]
            c += dc[dist]

    print('#{} '.format(test_case))
    for row in snail_nums:
        print(*row)     ##unpacking 출력







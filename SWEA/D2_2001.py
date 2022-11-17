T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = []

    for _ in range(N):
        nums.append(list(map(int, input().split())))

    max_area = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):

            tmp = 0
            for p in range(M):
                for q in range(M):
                    tmp += nums[i + p][j + q]

            if max_area < tmp:
                max_area = tmp

    print('#{} {}'.format(test_case, max_area))

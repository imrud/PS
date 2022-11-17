T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))

    max_cost = nums[-1]  ## 마지막 값을 최댓값으로 설정
    result = 0      ## 이익

    ## 뒤에서부터 계산
    for i in range(n-1, -1, -1):
        if max_cost > nums[i]:      ## 클 때
            result += max_cost - nums[i]
        else:       ## 작거나 같을 때
            max_cost = nums[i]

    print('#{} {}'.format(test_case, result))
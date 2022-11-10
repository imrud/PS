## 10505.소득 불균
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))

    avg = sum(nums)//n

    cnt = 0
    for i in range(n):
        if nums[i] <= avg:
            cnt += 1

    print('#{} {}'.format(test_case, cnt))

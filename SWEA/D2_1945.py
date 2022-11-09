## 1945. 간단한 소인수분해
T = int(input())

nums = [2, 3, 5, 7, 11]
for test_case in range(1, T + 1):
    n = int(input())
    res = [0] * len(nums)

    for i in range(len(nums)):
        while n > 1:
            if n % nums[i] == 0:
                res[i] += 1
                n = n//nums[i]
            else:
                break

    print('#{} '.format(test_case), end='')
    for i in res:
        print(i, end=' ')
    print()
    

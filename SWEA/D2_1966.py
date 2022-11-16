from __future__ import print_function
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    print('#{}'.format(test_case), end=" ")
    for i in nums:
        print(i, end=" ")
    print()

T = int(input())
arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for test_case in range(1, T + 1):
    res = []
    n = int(input())

    print('#{} '.format(test_case))
    for coin in arr:
        count = 0
        count = n//coin
        n %= coin
        print(count, end=' ')
    print()
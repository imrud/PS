T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())

    res = a + b
    if res >= 24:
        res = res - 24

    print('#{} {}'.format(test_case, res))
    

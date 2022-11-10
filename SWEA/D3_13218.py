## 13218. 조별과제
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    res = 0
    if int(n/3) < 1:
        res = 0
    else:
        res = int(n/3)

    print('#{} {}'.format(test_case, res))
        

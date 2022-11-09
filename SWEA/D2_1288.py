## D2_1288
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    res = set()     ## 집합으로
    cnt = 1
    
    while True:
        for i in list(str(n)):
            res.add(i)
        if len(res) == 10:  ## 구하려는 조건 만족
            break
        n //= cnt
        cnt += 1    ## cnt 증가
        n *= cnt

    print('#{} {}'.format(test_case, n))

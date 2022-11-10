## 1959
T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    res = 0
    ## 길이가 같을 때
    t = abs(n-m)
    if n > m:
        for i in range(0, t+1):
            tmp = 0
            for j in range(m):
                tmp += a[j+i]*b[j]
            
            if res == 0:
                res = tmp

            else:
                res = max(res, tmp)
            
        
    elif n < m:
        for i in range(0, t+1):
            tmp = 0
            for j in range(n):
                tmp += a[j]*b[j+i]
            
            if res == 0:
                res = tmp

            else:
                res = max(res, tmp)
    else:
        res = sum([a[i]*b[i] for i in range(len(n))])            


    print('#{} {}'.format(test_case, res))

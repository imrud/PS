## 3431.준환이의 운동관리
T = int(input())

for test_case in range(1, T + 1):
    L, U, X =  map(int, input().split())

    result = 0
    if X < L:
        result = L - X
        
    elif X > U:
        result = -1
        
    else:
        result = 0
        

    print('#{} {}'.format(test_case, result))

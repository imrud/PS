## 2007. 패턴 마디의 길이
T = int(input())

for test_case in range(1, T + 1):
    sen = input()

    for i in range(1, 10):
        if sen[:i] == sen[i:i*2]:
            print('#{} {}'.format(test_case, ))
            break
    

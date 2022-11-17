T = int(input())

for test_case in range(1, T + 1):
    area = input()

    ##stack = []  ## 괄호 모음
    cnt = 0     ## 공 개수

    for i in range(len(area)):
        if area[i] == ')':
            if area[i-1] == '(' or area[i-1] in ['.', '|']:
                cnt += 1
        elif area[i] in ['.', '|']:
            if area[i-1] == '(':
                cnt +=1

    print('#{} {}'.format(test_case, cnt))

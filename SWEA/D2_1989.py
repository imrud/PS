## D2_1989
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    word = input().strip()
    if word == word[::-1]:      ## 뒤집은 거랑 같으면 회문
        print('#{} {}'.format(test_case, 1))
    else:
        print('#{} {}'.format(test_case, 0))
    
        

    

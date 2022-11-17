#T = int(input())
T = 10

for test_case in range(1, T + 1):
    n = int(input())    ## 테스트케이스 번호
    word = input()      ## 찾을 문자
    sentence = input()      ## 문장

    res = 0     ## 찾은 문자의 개수
    start_word = word[0]        ## 시작 단어

    for i in range(len(sentence)):
        cnt = 0
        if sentence[i] == start_word and i <= len(sentence)-len(word):       ## 시작단어와 같을 때, 다음 순서들 비교
            for j in range(1, len(word)):
                if word[j] == sentence[i+j]:
                    #print(i, j)
                    cnt += 1

            if cnt == len(word)-1:
                res += 1
        ## 다른 풀이(슬라이싱)
        # if sentence[i] == word[0]:
        #     if sentence[i:i + len(word)] == word:
        #         word += 1

    print('#{} {}'.format(test_case, res))
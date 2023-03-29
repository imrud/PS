def solution(s):
    answer = ''
    # str = list((s.lower()).split())       ## 공백 기준으로 문자열 분리(모두 소문자로 바꾸기)
    str = s.split(" ")     ## 공백 기준 문자열 분리  (" " -> 중요)

    # for i in range(len(str)):
    #     if not str[i][0].isdigit():     ## 첫 문자가 숫자가 아니라면
    #         str[i] = str[i][0].upper() + str[i][1:]

    for i in range(len(str)):
        str[i] = str[i][:1].upper() + str[i][1:].lower()

    #answer = " ".join(str)
    return " ".join(str)





    # for ss in str:
    #     for i in range(len(ss)):
    #         if i == 0:
    #             if ss[i].islower():         ## 단어의 첫 문자가 소문자인경우우
    #                answer += ss[i].upper()  ## 대문자로 변환
    #             else:
    #                 answer += ss[i]
    #         else:
    #             if ss[i].isupper():     ## 단어 중간에 대문자가 있는 경우
    #                 answer += ss[i].lower()     ## 소문자로 변환
    #             else:
    #                 answer += ss[i]
    #
    #     answer += " "

    # return answer[:-1]



setence = ["3people unFollowed me", "for the last week"]
for s in setence:
    print(solution(s))
##def solution(participant, completion):
##
##    for p in participant:
##        print(participant)
##        print(completion)
##        
##    
##        if p in completion:
##            
##            participant.remove(p)
##            completion.remove(p)
##
##    print(participant)
##    print(completion)       
##    return participant

##def solution(s):
##    answer = ''
##    for ss in s.split():
##        for i in range(0, len(ss)):
##            if i%2:     ## 짝수일대 대문자
##                answer += ss[i].upper() 
##            else:     ## 홀수일 때 소문자
##                answer += ss[i].lower()
##        answer += ''
##    return answer


##def solution(arr1, arr2):
##    answer = [[]]
##    for row in range(len(arr1)):
##        for column in range(len(row)):
##            answer[row].append(arr1[column]+arr2[column])
##    return answer

# Key:영단어, Value=숫자
num_str = {'zero':'0', 'one':'1','two':'2', 'three':'3','four':'4', 'five':'5','six':'6', 'seven':'7','eight':'8', 'nine':'9'}
def solution(s):
    answer = 0
    for i in num_str:
        if i in s:
            s = s.replace(i, num_str[i])
    return int(s)

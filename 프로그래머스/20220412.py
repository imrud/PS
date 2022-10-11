##def solution(n):
##    count = 0
##    for i in range(2, n+1):
##        t.append(i)
##        if i in [2,3]:
##            count += 1
##        else:
##            for j in range(2, i//2+1):
##                print(i, i//2+1)
##                if i%j == 0:    ## 나눠지는 수가 하나라도 존재하면 탈출
##                    break
##                else:
##                    #print(i, j)
##
##                    count += 1           
##    return count
##
##solution(5)
##solution(10)
##def solution(strings, n):
##    answer = []
##    tmp = {}
##    
##    for i in range(len(strings)):
##        tmp[strings[i][n]] = strings[i]
##        print(tmp)
##    
####    stmp = sorted(tmp.items())
####    for i in stmp:
####        answer.append(i[1])
##        
##    return answer
##def solution(nums):
##    answer = 0
##    nSum = []
##    ## 리스트에서 3개의 합 구하기(조합)
##    for i in range(len(nums)):
##        for j in range(i+1, len(nums)):
##            for k in range(j+1, len(nums)):
##                nSum.append(nums[i]+nums[j]+nums[k])
##
##    ## 소수 개수
##    for n in nSum:
##        cnt = 0
##        for p in range(2, n+1):
##            if n%p == 0:
##                cnt += 1
##        if cnt == 1:
##            answer += 1
##
##    return answer

##def solution(participant, completion):
##    answer = ''
##    participant.sort()
##    completion.sort()
##
##    for i in range(len(completion)):    
##        if (participant[i] != completion[i]):   #비교했을 때 없으면 그게 바로 미완주자
##            return participant[i]
##
##    return participant[-1]      ## participant의 마지막사람이 미완주자일경우

##def solution(participant, completion):
##    answer = ''
##    participant.sort()
##    completion.sort()
##
##    print(participant - completion)
##    for i in range(len(completion)):    
##        if (participant[i] != completion[i]):   #비교했을 때 없으면 그게 바로 미완주자
##            return participant[i]

def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)

    for comp in completion:
        sumHash -= hash(comp)
        
    return hashDict[sumHash]
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"] , ["josipa", "filipa", "marina", "nikola"]))


 

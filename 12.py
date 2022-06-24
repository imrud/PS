#01
##n = int(input())
##nl = []
##for i in range(n):
##    nl.append(int(input()))
##nl.sort()
##
##for i in nl:
##    print(i)


#02
import sys
n = int(input())
nl = []
for i in range(n):
##    nl.append(int(input()))
    nl.append(int(sys.stdin.readline()))

for i in sorted(nl):
    print(i)


#03
##n = int(input())
##nl = []
##for i in range(n):
##    nl.append(int(input()))
##
##count = [0]*(max(nl)+1)
##
##for j in nl:
##    count[j] += 1   ## nl리스트의 각 원소에 대한 개수 카운트
##
##
##for k in range(1, len(count)):
##    count[k] += count[k-1]
##
##
##re = [0]*(len(nl))
##for p in nl:
##    idx = count[p]
##    re[idx-1] = p
##    count[p] -= 1
##print(re)
## 인터넷
##import sys
##n = int(sys.stdin.readline())
##nl = [0]*10001  ## n의 수가 10,000보다 작거나 같은 자연수로 주어
##
##for _ in range(n):
##    nl[int(sys.stdin.readline())] += 1    ## 입력받은 수를 리스트의 인덱스로
##
##for i in range(10001):
##    if nl[i] != 0:  ## 입력받은 수중 i가 없으면 출력 안함.
##        for j in range(nl[i]):      ## nl[i]의 값만큼 반복해서 출력
##            print(i)




#04
##import sys
##from collections import Counter
##n = int(sys.stdin.readline())
####n = int(input())
##nl = []
##for i in range(n):
##    nl.append(int(sys.stdin.readline()))
##
##nl.sort()   ## 오른 차순으로 정렬하기
##
##print(round(sum(nl)/n))     ## 소수점 첫째자리에서 반올림
####print(nl[round(n/2)])     ## 중앙값 출력
##print(nl[n//2])     ## 중앙값 출력
##
####count = collections.Counter(nl)
##count = Counter(nl).most_common()
##if len(nl) > 1:
##    if count[0][1] == count[1][1]:
##        print(count[1][0])
##    else:
##        print(count[0][0])
##else:
##    print(count[0][0])
##print(max(nl)-min(nl))      ## 범위: 큰 수 - 작은 수



#05
##s = input()
##nl = []
##for i in range(0, len(s)):  ##ex) 1234면 10**3으로 하기위해 범위 설정
##    n = int(s[i:i+1])
##    nl.append(s[i:i+1])
##nl.sort(reverse=True)
##print("".join(nl))



#06
##n = int(input())
##nl = []
##for _ in range(n):
##    x, y = map(str, input().split())   ##str로 둘다 입력받기
##    nl.append((int(x), int(y)))
##
#### x좌표 증가하는 순서대로
##nl.sort(key = lambda x:(x[0], x[1]))
##
##for i in nl:
##    print(i[0], i[1])


#07
##n = int(input())
##nl = []
##for _ in range(n):
##    x, y = map(str, input().split())   ##str로 둘다 입력받기
##    nl.append((int(x), int(y)))
##
#### x좌표 증가하는 순서대로
##nl.sort(key = lambda x:(x[1], x[0]))
##
##for i in nl:
##    print(i[0], i[1])




#08
##n = int(input())
##wl = []
##for _ in range(n):
##    word = input()
##    wl.append((word, len(word)))
#### 중복제거
##wl = list(set(wl))
##
#### 단어 길이 오름차순으로 정렬, 그 다음은 알파벳순서
##wl.sort(key = lambda x:(x[1], x[0]))
##
##for i in wl:
##    print(i[0])





#9
## 시간초과
##n = int(input())
##al = []     ## 나이 저장할 리스트
##nl = []     ## 이름 저장할 리스트
##
##for _ in range(n):
##    age, name = input().split()
##    al.append(int(age))
##    nl.append(name)
##
##al2 = []
##nl2 = []
##for _ in range(n):
##    t = al.index(min(al))
##    al2.append(al[t])
##    nl2.append(nl[t])
##    del al[t]
##    del nl[t]
##
##for i in range(n):
##    print(al2[i], nl2[i])
## 인터넷
##n = int(input())
##ml = []
##
##for _ in range(n):
##    age, name = map(str, input().split())   ##str로 둘다 입력받기
##    age = int(age)
##    ml.append((age, name))
##
#### 나이 오름차순으로 정렬
##ml.sort(key = lambda x:(x[0]))
##
##for i in ml:
##    print(i[0], i[1])
##    
    


#10
#시간 초과
##import sys
##n = int(sys.stdin.readline())
##nl = list(map(int,sys.stdin.readline().split()))
##
##count = []
##for i in range(n):
##    count = 0
##    for j in range(0, n):
##        if nl[i] > nl[j]:
##            count +=1
##    print(count, end=" ")
##import sys
##input = sys.stdin.readline
##
##n = int(input())
##nl = list(map(int,input().split()))
##
##nl2 = sorted(list(set(nl)))  ## 중복제거 후 오름차순 정렬
##
##dic = {nl2[i] : i for i in range(len(nl2))}
##
##for j in nl:
##    print(dic[j], end=' ')




    


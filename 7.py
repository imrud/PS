#1
##str = input()
##print(ord(str))

###2
##n = int(input())
##num = input()
##
##print(sum(map(int, str(num))))


#3
##S = input()
##alpha_list = 'abcdefghijklmnopqrstuvwxyz'
##
##for i in alpha_list:
##    if i in S:
##        print(S.index(i), end = ' ')
##    else:
##        print(-1, end = ' ')
    

#4
##내가 한 코드
##t = int(input())
##r = []      ## 반복횟수
##str = []    ## 반복할 문자열
##for i in range(t):
##    rr, s = input().split()
##    r.append(int(rr))   
##    str.append(s)
##
##
##for i in str:
##    p = []
##    for j in i:
##        for k in r:
##            p.append(j)
##    p = ''.join(p)
## 인터넷
##t = int(input())
##for i in range(t):
##    r, s = input().split()
##    r = int(r)  ## 형변환
##    s = str(s)
##
##    for i in range(len(s)):
##        print(r*s[i], end='')
##    print()


###5
##s = input()
##s = s.upper()   ## 대문자로 변환
##s_list = list(set(s))   ##  중복제거
##
##cnt = []
##for i in s_list:
##    count = s.count     ## i에 해당하는 수 카운트
##    cnt.append(count(i))
##
##if cnt.count(max(cnt)) > 1:     ## max가 2이상일때
##    print("?")
##
##else:
##    print(s_list[(cnt.index(max(cnt)))])


#6
##s = input()
##count = 0
##for i in s:
##    if i == " ":
##        count+=1
##
##count += 1      #공백 개수+1
##print(count)
##s = input().split()
##print(len(s))


#7
##n1, n2 = input().split()
##n1 = n1[::-1]
##n2 = n2[::-1]
##
##if n1 > n2:
##    print(n1)
##else:
##    print(n2)


#8
##alpha = input()
##count = 0
##
##for i in alpha:
##    count += 2  # 1 기준 2초
##    if i=='A' or i=='B' or i=='C':
##        count += 1
##    if i=='D' or i=='E' or i=='F':
##        count += 2
##    if i=='G' or i=='H' or i=='I':
##        count += 3
##    if i=='J' or i=='K' or i=='L':
##        count += 4
##    if i=='M' or i=='N' or i=='O':
##        count += 5
##    if i=='P' or i=='Q' or i=='R' or i=='S':
##        count += 6
##    if i=='T' or i=='U' or i=='V':
##        count += 7
##    if i=='W' or i=='X' or i=='Y' or i=='Z':
##        count += 8
##
##print(count)
###인터넷
##number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
##alpha = input()
##count = 0
##
##for i in range(len(alpha)):
##    for j in number:
##        if(alpha[i] in j):
##            count += number.index(j)+3
##print(count)
##            
        
    


#9
##내 풀이
##ca = ['c=', 'c-', 'dz=', 'd-', 'lj','nj','s=', 'z=']
##cstr = input()
##n = len(cstr)/2
##for i in range(n):
##    cstr[:2]
##인터넷
##ca = ['c=', 'c-', 'dz=', 'd-', 'lj','nj','s=', 'z=']
##cstr = input()
##for i in ca:
##    cstr = cstr.replace(i, '*')  ## replace이용해서 i가 cstr에 있으면 '*'로 바꿈
##print(len(cstr))
##    


#10
##n = int(input())
##count = 0
##
##for _ in range(n):
##    word = input()
##    for i in range(len(word)): ##  i+1을 실행하기 때문에 (len(word)-1)
##        if i != len(word)-1:    ## 끝까지 실행x
##            if word[i] == word[i+1]:
##                pass
##            elif word[i] in word[i+1:]: ## i+1 이후에 i가 있으면 점수 깍아
##                break
##        else:
##            count += 1
##                
##print(count)
        


    

#1
##n = int(input())
##li = list(map(int, input().split()))
##print(min(li), max(li))


###2
##n = []
##for i in range(9):
##    n.append(int(input()))
##
##print(max(n))
##print(n.index(max(n))+1)


###3
##a = int(input())
##b = int(input())
##c = int(input())
##
##m = str(a*b*c)     #곱의 결과
##
##for i in range(10):
##    n_count = m.count(str(i))
##    print(n_count)
    

#4
##list = []
##for i in range(10):             ## 수 10개 입력받기
##    n = int(input())
##    list.append(n%42)
##
##list = set(list)   ##집합으로
##print(len(list))   ## 길이 출력


#5
##n = int(input())
##s_list = list(map(int, input().split()))  ## 한 줄에 입력받기
##
##sum = 0
##for i in range(n):
##    sum += (s_list[i]/max(s_list))*100
##         
##print(sum/n)
    

#6
##n = int(input())
##
##for i in range(n):
##    o_list = input()     ## OX를 리스트 요소로 입력 받기
##    count = 0
##    sum = 0
##    for j in range(len(o_list)):
##        if o_list[j] == "O":
##            count += 1
##            sum += count
##        elif o_list[j] == "X":   ## oo나와도 중간에 x가 나오면 count 리셋
##            count = 0
##    print(sum)    
##    
    

#7
n = int(input())

for _ in range(n):
    s_list = list(map(int, input().split()))
    count = 0
    
    avg = sum(s_list[1:])/s_list[0]
    
    for i in s_list[1:]:
        if i > avg:
            count += 1
    rate = count/s_list[0]*100
    print('{:.3f}%'.format(rate))


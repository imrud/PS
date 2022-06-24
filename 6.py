#1
##def solve(a):
##    ans = 0
##    for i in a:
##        ans += i
##        
##    return ans



#2
##def d(n):
##    n = n + sum(map(int, str(n)))   ## 리스트로 자리수 분리
##    return n
##
#### 셀프 넘버가 아닌 수 들어갈 집합
##nonSelf = set()
##
#### nonSelf 집합에 들어갈 수
##for i in range(1, 10001):
##    nonSelf.add(d(i))    ## 함수 통해 nonSelf 걸러냄
##
#### 셀프 넘버 출력
##for j in range(1, 10001):
##    if j not in nonSelf:
##        print(j)


#3
def hansu(n):
    hcount = 0
    for i in range(1, n+1):
        nums = list(map(int, str(i)))
        if i<100:
            hcount += 1
        elif nums[0]-nums[1] == nums[1]-nums[2]:
            hcount += 1
    return hcount


num = int(input())
print(hansu(num))

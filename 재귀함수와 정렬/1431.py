## 백준 : 시리얼 번호
import sys
input = sys.stdin.readline

##def sum_nums(num):
##    res = 0
##    for i in num:
##        if i.isdigit():     ## 시리얼번호 구성요소가 숫자인경우
##            res += int(i)
##    return res

n = int(input())
nums = []
for _ in range(n):
    nums.append(input().rstrip())

##nums.sort(key=lambda x : (len(x), sum_nums(x), x))

for i in range(n-1):
    for j in range(i+1, n):
        if len(nums[i]) > len(nums[j]):     ## 길이순 정렬
            nums[i], nums[j] = nums[j], nums[i]

        elif len(nums[i]) == len(nums[j]):  ## 길이 같을 경우 합비교
            sum_i = 0
            sum_j = 0
            for x,y in zip(nums[i], nums[j]):
                if x.isdigit():
                    sum_i += int(x)
                if y.isdigit():
                    sum_j += int(y)
                    
            if sum_i > sum_j :      ## 합이 작은게 앞으로
                nums[i], nums[j] = nums[j], nums[i]

            elif sum_i == sum_j:    ## 합 같을 경우
                for x,y in zip(nums[i], nums[j]):
                    if x > y:       ## 사전순
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    elif x < y:
                        break

for n in nums:
    print(n)
            

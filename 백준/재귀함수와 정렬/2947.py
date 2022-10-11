## 백준 : 2947
import sys
input = sys.stdin.readline

nums = list(map(int, input().rstrip().split()))

count = 1
while count != 0:
    count = 0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1] :
            count += 1
            nums[i], nums[i+1] = nums[i+1], nums[i]
            print(*nums)

##while True:
##    for i in range(4):
##        if nums[i] > nums[i+1]:
##           nums[i], nums[i+1] = nums[i+1], nums[i]
##            print(*nums)
##    if nums == [1, 2, 3, 4, 5]:
##        break

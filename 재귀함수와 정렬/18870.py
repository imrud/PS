## 백준 : 18870
import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
sNum = sorted(list(set(nums)))  ## 중복제거 후, 오름차순 정렬

nDict = {}
for i in range(len(sNum)):
    nDict[sNum[i]] = i

for i in nums:
    print(nDict[i], end=' ')





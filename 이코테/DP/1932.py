## 백준 1932 :  정수 삼각형
import sys
input = sys.stdin.readline

n = int(input())
#arr = [[0]*n for _ in range(n)]
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
        

for i in range(1, n):
    for j in range(len(arr[i])):
        if  j == 0:
            arr[i][j] += arr[i-1][j]
           
        elif  j == len(arr[i])-1:

            arr[i][j] += arr[i-1][j-1]
        else:
##        elif 0 < j < len(arr[i]):
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])



##print(max(map(max, arr)))
print(max(arr[n-1]))    ## 마지막행에서(n-1) 최댓값 출

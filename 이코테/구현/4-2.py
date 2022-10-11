## [CH4]예제 4-2 : 시각
import sys

input = sys.stdin.readline
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1


print(count)

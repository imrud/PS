## 문자열 뒤집기
import sys
input = sys.stdin.readline

s = input().strip()

cnt0 = 0
cnt1 = 0

## 첫 번째 원소
if s[0] == "1":
    cnt0 += 1
else:
    cnt1 += 1

## 두 번째 원소부터 모든 원소 확인
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt0, cnt1))

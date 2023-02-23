import sys
from collections import deque
input = sys.stdin.readline

#MAX = 10**9
A, B = map(int, input().split())    ## A, B 입력받기
# visited = [0]*(MAX+1) ## 메모리 초과 주범이 아닐까...

deq = deque()
deq.append((A, 1))      ## (현재 값, 연산 횟수)를 deq에 넣기
#visited[A] = 1

result = -1 ## 초기화 값은 1

while deq:
    x, cnt = deq.popleft()  ## 첫 번째 값과 연산 횟수 꺼내기

    if x == B:
        result = cnt
        break

    if x > B:
        continue

    deq.append((x*2, cnt+1))    ## 2배
    deq.append((int(str(x)+'1'), cnt + 1))  ## 끝자리에 1 더해주기

    # if x == B:      ## 방금 꺼낸 값이 B와 같을 경우 종료
    #     print(visited[x])
    #     break

    # for tx in [2*x, int(str(x)+'1')]:
    #     if 0 <= tx <= B:
    #         deq.append(tx)
    #         visited[tx] = visited[x]+1


# if visited[B] == 0:
#     print(-1)
# else:
#     print(visited[B])

print(result)

### top-down 방식
## a -> b가 아니라, b -> a로

# result = 1
# while( B != A):
#     result += 1
#
#     tmp = B
#
#     if B % 10 == 1: ## 나머지가 1일때 -> 끝자리가 1인 경우
#         B //= 10
#     elif B % 2 == 0:    ## 2의 배수일 때
#         B //= 2
#
#     if tmp == B:
#         print(-1)
#         break
#
# else:
#     print(result)
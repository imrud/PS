import sys
from itertools import combinations
import heapq
input = sys.stdin.readline

n = int(input())    ## 합칠 카드 묶음의 개수
#result = 0
heap = []
for _ in range(n):
    data = int(input())
    heapq.heappush(heap,data)

result = 0

while len(heap) != 1:       ## 카드 묶음이 한 개인 경우에는 비교할 필요 X
    ## 가장 작은 2개의 카드 묶음 꺼내기
    c1 = heapq.heappop(heap)
    c2 = heapq.heappop(heap)

    ## 두 카드묶음의 합
    tmp = c1 + c2
    result += tmp
    heapq.heappush(heap, tmp)       ## 두 묶음의 합을 다시 힙에 넣기(어차피 알아서 정렬해줌

print(result)
# ## 정렬하기
# card.sort()
# if len(card) < 2:
#     print(sum(card))
# else:
#     print(sum(card)+sum(:))


## 최소 값 구하기(두 개씩 조합해서 그 중 최소값을 더하는게 구하는값)
# tmp = 0
# for p, q in combinations(card, 2):
#     if tmp == 0:
#         tmp = p+q
#     else:
#         if p+q < tmp:
#             tmp = p+q

#print(sum(card)+tmp)
## 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    ## 전체 음식 머는 시간이 k보다 작거나 같다면  -1 반환
    if sum(food_times) <= k:
        return -1

    ## 작은 음식부터 빼기 -> 우선순위 큐 이용
    que = []
    for i in range(len(food_times)):
        ## (음식 시간, 번호)
        heapq.heappush(que, (food_times[i], i+1))

    sum_time = 0    ## 이전 음식까지 다 먹은 시간
    pre_time = 0    ## 이전 음식 섭취 시간
    length = len(food_times)    ## 남은 음식 개수

    while sum_time + ((que[0][0])-pre_time) * length <= k:
        now_time = heapq.heappop(que)[0]
        sum_time += (now_time - pre_time) * length
        length -= 1
        pre_time = now_time     ## 이전 음식 섭취 시간 갱신
    
    result = sorted(que, key = lambda x: x[1])      ## 음식의 번호 기준 정렬
    return result[(k-sum_time)%length][1]

food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))

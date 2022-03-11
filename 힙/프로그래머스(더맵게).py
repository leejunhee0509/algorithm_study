#16 13
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    if len(scoville)==1:
        if scoville[0]>=K:
            return 0
        else:
            return -1
    while len(scoville)>=1:
        if scoville[0] >=K:
            return cnt
        if len(scoville)==1:
            if scoville[0]>=K:
                return cnt
            else:
                return -1
        
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        cnt+=1
    return -1
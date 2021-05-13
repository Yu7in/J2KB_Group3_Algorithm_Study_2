import heapq
        
def solution(scoville, K):
    
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1 :
        if scoville[0] >= K : 
            break
        answer += 1
        sco1 = heapq.heappop(scoville)
        sco2 = heapq.heappop(scoville)
        newSco = sco1 + sco2*2
        heapq.heappush(scoville, newSco)
    
    if scoville[0] < K : return -1
    return answer

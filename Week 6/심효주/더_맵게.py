import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while 1:
        if  len(scoville)<=1 and scoville[0]<K:
            answer = -1
            break
        if scoville[0]>=K:
            break
        fir = heapq.heappop(scoville)
        sec = heapq.heappop(scoville)
        new = fir + (sec*2)
        heapq.heappush(scoville, new)
        answer += 1

    return answer

scoville = [1,2,3,9,10,12]
K = 7
print(solution(scoville, K))

#https://liveyourit.tistory.com/191
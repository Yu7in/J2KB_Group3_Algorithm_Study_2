import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    days = deque()
    cnt = 1
    for i in range(len(progresses)):
        p = progresses[i]
        s = speeds[i]
        day = (100-p)/s

        days.append(math.ceil(day))

    std = days.popleft()

    while days:
        next = days.popleft()
        # print(std, next)
        if std >= next:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            std = next
        if len(days) == 0:
            answer.append(cnt)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))
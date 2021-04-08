def solution(n, lost, reserve):

    # 체육복을 도난당한 학생이 여벌이 있을경우를 고려하여 둘 다 제거
    real_lost = list(set(lost) - set(reserve))
    real_reserve = list(set(reserve) -set(lost))

    for i in range(len(real_reserve)):
        if real_reserve[i] -1 in real_lost:
            real_lost.remove(real_reserve[i] -1)
        elif real_reserve[i] + 1 in real_lost:
            real_lost.remove(real_reserve[i] + 1)

    answer = n - len(real_lost)
    return answer

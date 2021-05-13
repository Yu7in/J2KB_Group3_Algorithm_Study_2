def solution(n, lost, reserve):
    answer = 0

    setL = set(lost) - set(reserve)
    setR = set(reserve) - set(lost)

    for i in setR:
        if i - 1 in setL:
            setL.remove(i - 1)
        elif i + 1 in setL:
            setL.remove(i + 1)

    answer = n - len(setL)
    return answer

# n = 5
# lost = [2,4]
# reserve = [1,3,5]
# print(solution(n, lost, reserve))

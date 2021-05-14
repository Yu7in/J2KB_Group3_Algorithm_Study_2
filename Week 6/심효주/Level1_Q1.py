def solution(arr, divisor):
    answer = []
    for a in arr:
        if a%divisor == 0:
            answer.append(a)
    if len(answer)==0:
        answer.append(-1)
    answer.sort()
    return answer

arr = [3,2,6]
divisor = 10
print(solution(arr, divisor))
def solution(seoul):
    answer = '김서방은 '
    for i in range(len(seoul)):
        s = seoul[i]
        if s == "Kim":
            answer += str(i)
    answer += '에 있다'
    return answer

seoul = ["Jane", "Kim"]
print(solution(seoul))
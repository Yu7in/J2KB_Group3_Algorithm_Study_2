def solution(seoul):
    answer = '김서방은 '
    for i in range(len(seoul)):
        s = seoul[i]
        if s == 'Kim':
            answer += str(i)
    return answer + '에 있다'

seoul = ['Jane', 'Kim']
print(solution(seoul))

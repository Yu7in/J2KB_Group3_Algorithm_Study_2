def solution(answers):
    answer = []
    # 수포자는 3명: 삼인방
    # 1번 1,2, 3, 4, 5 반복
    # 2번 2, 1, 2, 3, 2, 4, 2, 5 반복
    # 3번 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 반복
    # 10,000문제니까 반복해도 되겠고 -> 아님 런타임 에러남; 
    # 마지막에 answer는 오름차순 정렬해도 되겠네 [o]

    supoja = [[1, 2, 3, 4,  5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    corrCount = [0, 0, 0]

    qCount = len(answers) # 문제 수
    for i in range(qCount):
        q = answers[i]

        if q == supoja[0][i]:
            corrCount[0] += 1

        if q == supoja[1][i]:
            corrCount[1] += 1

        if q == supoja[2][i]:
            corrCount[2] += 1

    maxCount = max(corrCount)

    for i in range(3):
        if maxCount == corrCount[i]:
            answer.append(i+1)

    answer.sort()
    return answer

answers = [1,3,2,4,2]
print(solution(answers))

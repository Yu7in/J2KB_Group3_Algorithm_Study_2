def solution(n, lost, reserve):
    answer = 0
    
    for student in range(1,n+1) :
        if student in lost and student in reserve :
            lost[lost.index(student)] = -1
            reserve[reserve.index(student)] = -1
            
    for student in range(1, n+1) :
        if student in lost :
            if student-1 in reserve :
                reserve[reserve.index(student-1)] = -1
                answer += 1
            elif student+1 in reserve :
                reserve[reserve.index(student+1)] = -1
                answer += 1
        else :
            answer += 1
        
    return answer

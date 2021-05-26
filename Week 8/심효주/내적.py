# 일부로 그런게 아닌데.. 넘 쉬운 문제 골라서 머쓱..

def solution(a, b):
    answer = 0
    len_arr = len(a)
    for i in range(len_arr):
        answer += a[i]*b[i]
    return answer

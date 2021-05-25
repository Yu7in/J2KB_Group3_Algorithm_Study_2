def solution(nums):
    answer = 0
    set_list = list(set(nums))
    
    cntSetList = len(set_list)
    selectN = len(nums)//2

    if cntSetList >= selectN:
        answer = selectN
    else:
        answer = cntSetList
    return answer

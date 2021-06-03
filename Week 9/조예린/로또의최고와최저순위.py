rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}

def solution(lottos, win_nums):
    answer = []
    
    correct = 0
    zero = 0
    for lotto in lottos :
        if lotto == 0 :
            zero += 1
            continue
        if lotto in win_nums :
            correct += 1
    
    MAX = correct + zero
    
    return [rank[MAX], rank[correct]]

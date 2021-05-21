# ㅠㅠ 시간초과 결국 해결 못했습니다

import sys
sys.setrecursionlimit(10**6)

def getChild(win, parent) :
    temp = set(win[parent])
    
    for child in win[parent] :
        temp |= getChild(win, child)
    
    return temp

def solution(n, results):
    answer = 0
    
    win = {}
    for i in range(1,n+1) :
        win[i] = []
        
    for parent, child in results :
        win[parent].append(child)
        
    CPn = [[0,0] for _ in range(n+1)] # parent, child 갯수
    
    for parent in win :
        win[parent] = list(getChild(win,parent))
        
        for child in win[parent] :
            CPn[child][0] += 1
            
        CPn[parent][1] = len(win[parent])
        
    for cp in CPn :
        if cp[0] + cp[1] == n-1 :
            answer += 1
            
    return answer

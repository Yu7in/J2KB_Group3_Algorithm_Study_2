
L = 0
UP = (-1,0)
DOWN = (1,0)
RIGHT = (0,1)
LEFT = (0,-1)

# 시계 방향으로 90도 회전하는 함수
def rotate(board) :
    res = [[0]*L for _ in range(L)]
    
    for i, row in enumerate(board) :
        for j in range(L) :
            res[j][L-i-1]= row[j]
            
    return res

def move(board, direction) :
    
    res = [[0]*L for _ in range(L)]
    (dy, dx) = direction
    
    for y in range(L) :
        for x in range(L) :
            if (0<=y+dy<L) and (0<=x+dx<L) :
                res[y+dy][x+dx] = board[y][x]
                
    return res

def isFit(key, lock) :
    
    for y in range(len(lock)) :
        for x in range(len(lock)) :
            if lock[y][x] == 0 and key[y][x] == 0 :
                return False
            if lock[y][x] == 1 and key[y][x] == 1 : # 이거 떔에 겁나 오래 디버깅함
                return False
            
    return True

def solution(key, lock):
    global L
    answer = True
    
    # key가 lock보다 작은 경우 key의 주변부 확장하기
    # 위치 좌표만 옮길까? 헷갈리니까 그러지 말자
    expandedKey = []
    
    if len(key) < len(lock) :
        expandedKey = [[0]*len(lock) for _ in range(len(lock))]
        for y in range(len(key)) :
            for x in range(len(key)) :
                expandedKey[y][x] = key[y][x]
        key = expandedKey[:]
        
    L = len(key)
    rotateNumber = 4
    rotatedBoard = key[:]
    
    for _ in range(rotateNumber) :
        
        for ud in (UP, DOWN) : 
            
            updownBoard = rotatedBoard[:]
            
            for _ in range(L) :
                
                for rl in (RIGHT, LEFT) :
                    
                    rightLeftBoard = updownBoard[:]
                    
                    for _ in range(L) :
                        
                        if isFit(rightLeftBoard, lock) :
                            return True
                        
                        rightLeftBoard = move(rightLeftBoard, rl)
                
                updownBoard = move(updownBoard, ud)
                
        rotatedBoard = rotate(rotatedBoard)
    
    return False

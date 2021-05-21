# 체크는 오른쪽+아래로만 체크합니다.
def check22(y, x, board) : 
    
    dirs = [[0,1], [1,0], [1,1]]
    
    ret = [(y,x)]
    for d in dirs :
        dy, dx = y+d[0], x+d[1]
        if not ( (0<=dy<len(board)) and (0<=dx<len(board[0])) and board[dy][dx]!='0' and board[y][x]==board[dy][dx] ) :
            return False
        else :
            ret.append((dy,dx))

    return ret # 나중에 한 번에 삭제될 거임

def dropdown(board) :
    
    for x in range(len(board[0])) :
        cnt = 0
        movable = False
        for y in range(len(board)-1, -1, -1) :
            # if y == len(board)-1 :
            #     if board[y][x] == '0' : break
            if board[y][x] == '0' :
                cnt += 1
                movable = True
            if board[y][x] != '0' and movable :
                # 위에 떠있는 블록임. cnt만큼 내리면 됨
                board[y+cnt][x] = board[y][x]
                board[y][x] = '0'
    
    return board
                
def deleteBoard(delete, board) :
    
    for delNode in delete :
        board[delNode[0]][delNode[1]] = '0'
        
    return board

def solution(m, n, board):
    answer = 0
    
    for i in range(len(board)) :
        board[i] = list(board[i])
    
    
    while True :
        
        delete = set([])
        
        for y in range(len(board)) :
            for x in range(len(board[0])) :
                tmp = check22(y, x, board)
                if tmp :
                    delete |= set(tmp)
        
        delete = list(delete)
        if not delete : break
        
        answer += len(delete)
        
        board = deleteBoard(delete, board)
        # print(board)
        board = dropdown(board)
        # print(board)
    
    return answer

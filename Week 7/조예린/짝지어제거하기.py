def solution(s):
    if len(s)%2 == 1 : return 0
    stack = []
    
    for word in s :
        # print(stack)
        if not stack or word != stack[-1] :
            stack.append(word)
        elif word == stack[-1] :
            stack.pop()
    
    # print(stack)
    if stack :
        return 0
    return 1
    

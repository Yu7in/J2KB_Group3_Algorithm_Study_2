import sys
input = sys.stdin.readline

T = int(input())

def is_vpc(str):
    ans = 'YES'
    stack = []
    p = {
        ')' : '('
    }
    for s in str:
        if s in ')':
            if not stack:
                ans = 'NO'

        if s in '(':
            stack.append(s)

        if stack:
            if s in ')':
                if stack[-1] in '(':
                    stack.pop()
    if stack:
        ans = 'NO'
    return ans


for _ in range(T):
    str = input().rstrip()
    print(is_vpc(str))

# (()())((()))
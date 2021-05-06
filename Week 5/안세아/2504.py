import sys

input = sys.stdin.readline

lists = list(input().rstrip())

#() = x2
#[] = x3

stack = []

for i in lists:
    # 닫는 괄호 종류 별로 나누고
    if i == ")":
        num = 0

        while stack:
            top = stack.pop()
            if top == "(":
                if num ==0:
                    stack.append(2)
                else:
                    stack.append(2 * num)
                break
            elif top == "[":
                print("0")
                exit(0)
            else:
                if num == 0:
                    num = int(top)
                else:
                    num = num + int(top)

    elif i == "]":
        num = 0

        while stack:
            top = stack.pop()
            if top == "[":
                if num == 0:
                    stack.append(3)
                else:
                    stack.append(3 * num)
                break
            elif top == "(":
                print("0")
                exit(0)
            else:
                if num == 0:
                    num = int(top)
                else:
                    num = num + int(top)
    else:
        stack.append(i)
result = 0

for i in stack:
    if i == "(" or i == "[":
        print(0)
        exit(0)
    else:
        result += i
print(result)
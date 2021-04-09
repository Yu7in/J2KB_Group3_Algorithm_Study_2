import sys
n = int(sys.stdin.readline())
stck = list()

def push(data):
    stck.append(data)

def pop():
    if len(stck) == 0:
        print(-1)
    else:
        print(stck.pop())

def size():
    print(len(stck))

def empty():
    if len(stck) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stck) == 0:
        print(-1)
    else:
        print(stck[-1])

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        push(cmd[1])
    elif cmd[0] == 'pop':
        pop()
    elif cmd[0] == 'size':
        size()
    elif cmd[0] == 'empty':
        empty()
    elif cmd[0] == 'top':
        top()
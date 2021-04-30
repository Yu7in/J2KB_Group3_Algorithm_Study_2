from collections import deque
import sys

input = sys.stdin.readline
subin, sister = map(int, input().split())

MAX = 100001
ans = [0] * MAX

def bfs():
    q = deque([subin])
    while q:
        now_pos = q.popleft()
        # print('now_pos: ', now_pos)
        if now_pos == sister:
            return ans[now_pos]
        for next_pos in (now_pos-1, now_pos+1, now_pos*2):
            # print('들어왔는지 확인')
            if 0<=next_pos<MAX and not ans[next_pos]:
                ans[next_pos] = ans[now_pos]+1
                q.append(next_pos)

print(bfs())


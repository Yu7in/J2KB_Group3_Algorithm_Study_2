import sys
input = sys.stdin.readline

def dfs(graph, start_node):
    stack = [start_node]
    visited = []

    while stack:
        cur_node = stack.pop()
        visited.append(cur_node)
        for node in graph[cur_node]:
            if
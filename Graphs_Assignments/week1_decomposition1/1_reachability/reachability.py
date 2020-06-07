# Uses python3

'''
------------------------------------------------------------------------------------------------------------------------
Case #1/16:

Input:
4 3
1 2
3 2
4 3
1 4

Correct output:
1
------------------------------------------------------------------------------------------------------------------------
'''

import sys


def explore(adj_list, x_node, y_node, visited):
    visited[x_node] = True
    for vertex in adj_list[x_node]:
        if vertex == y_node:
            visited[y_node] = True
            break
        if not visited[vertex]:
            explore(adj_list, vertex, y_node, visited)


def reach(adj_list, x_node, y_node) -> int:
    # write your code here
    visited = [False for _ in range(len(adj_list))]
    explore(adj_list, x_node, y_node, visited)
    if visited[y]:
        return 1
    return 0


if __name__ == '__main__':
    user_input = sys.stdin.read()
    data = list(map(int, user_input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))

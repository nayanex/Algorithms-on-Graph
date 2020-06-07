# Uses python3

import sys
from typing import List


def explore(adj_list: List[List[int]], vertex: int, visited: List[bool], cc: int, cc_num: List[int]):
    visited[vertex] = True
    cc_num[vertex] = cc
    for node in adj_list[vertex]:
        if not visited[node]:
            explore(adj_list, node, visited, cc, cc_num)


def dfs(adj_list: List[List[int]]) -> List[int]:
    visited = [False for _ in range(len(adj))]
    cc_num = [False for _ in range(len(adj))]
    for vertex_neighbors in adj_list:
        cc = 1
        for vertex in vertex_neighbors:
            if not visited[vertex]:
                explore(adj_list, vertex, visited, cc, cc_num)
                cc += 1
    return cc_num


def number_of_components(adj_list: List[List[int]]) -> int:
    result = 0
    # write your code here
    cc_num = dfs(adj_list)
    result = len(set(cc_num))

    return result


if __name__ == '__main__':
    user_input = sys.stdin.read()
    data = list(map(int, user_input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))

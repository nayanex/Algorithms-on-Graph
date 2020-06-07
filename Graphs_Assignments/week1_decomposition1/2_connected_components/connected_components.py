# Uses python3

'''
Case #5/16:

Input:
100 100
27 96
6 9
81 98
21 94
22 68
76 100
8 50
38 86
71 75
32 93
16 50
71 84
6 72
22 58
7 19
19 76
44 75
24 76
31 35
11 89
42 98
63 92
37 38
20 98
45 91
23 53
37 91
76 93
67 90
12 22
43 52
23 56
67 68
1 21
17 83
63 72
30 32
7 91
50 69
38 44
55 89
15 23
11 72
28 42
22 69
56 79
53 58
5 83
13 72
7 93
20 54
21 55
66 89
2 91
18 88
26 64
11 61
28 59
12 86
42 95
17 82
50 66
66 99
40 71
20 40
5 66
92 95
32 46
7 36
44 94
6 31
19 67
26 57
53 84
10 68
28 74
34 94
25 61
71 88
10 89
28 52
72 79
39 73
11 80
44 79
13 77
30 96
30 53
10 39
1 90
40 91
62 71
44 54
15 17
69 74
13 67
24 69
34 96
21 50
20 91

Correct output:
19
'''

import sys


def explore(adj_list: list, vertex: int, visited: list, cc: int, cc_num: list):
    visited[vertex] = True
    cc_num[vertex] = cc
    for node in adj_list[vertex]:
        if not visited[node]:
            explore(adj_list, node, visited, cc, cc_num)


def dfs(adj_list: list) -> list:
    visited = [False for _ in range(len(adj))]
    cc_num = [False for _ in range(len(adj))]
    for vertex_neighbors in adj_list:
        cc = 1
        for vertex in vertex_neighbors:
            if not visited[vertex]:
                explore(adj_list, vertex, visited, cc, cc_num)
                cc += 1
    return cc_num


def number_of_components(adj_list: list) -> int:
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

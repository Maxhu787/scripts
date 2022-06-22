def dfs(x):
    visited[x] = True
    farthest = (0, x)
    for to in edges[x]:
        if not visited[to]: # traversal all not-visited point(s).
            to_len, to_end = dfs(to)
            farthest = max(farthest, (to_len + 1, to_end))

    return farthest

n = int(input())

# n is the count of points.

edges = [[] for i in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split(' '))
    edges[a].append(b)
    edges[b].append(a)

# edge[x] is a list consist of all destination from x.

# First, Do a depth-first search to find the farthest from 0. It is one of the endpoint of the longest-path.
visited = [False] * n  # Initialize the visited record of first DFS
(_, endpoint) = dfs(0)

# Secondly, find the farthest point from "endpoint" also by DFS. The point is also an endpoint of the longest-path.
visited = [False] * n  # Initialize the visited record of second DFS
(ans, _) = dfs(endpoint)

print(ans)

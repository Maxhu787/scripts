# 血緣關係 -1
n = int(input())
edges = [[] for i in range(n)]
visited = [False] * n

def dfs(x):
    visited[x] = True
    far = 0, x
    for to in edges[x]:
        if not visited[to]:
            to_len, to_end = dfs(to)
            if to_len >= far[0]:
                far = to_len + 1, to_end

    return far


for i in range(n - 1):
    a, b = map(int, input().split(' '))
    edges[a].append(b)
    edges[b].append(a)

_, endpoint = dfs(0)
visited = [False] * n
ans, _ = dfs(endpoint)

print(ans)

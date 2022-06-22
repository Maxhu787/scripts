def dfs(x):
    visited[x] = True           # 設定 list[x] = True 代表造訪過
    farthest = (0, x)           # father 是 Tuple
    for to in edges[x]:
        if not visited[to]:     # 造訪所有未訪問過的節點.
            (to_len, to_end) = dfs(to)  # (to_len, to_end) 是 Tuple
            farthest = max(farthest, (to_len + 1, to_end))
    return farthest

n = int(input())                # 輸入節點數
edges = [[] for i in range(n)]  # edges 是 list

# edge [x]是一個列表，其中包含x的所有元素
# 輸入節點內函值
for i in range(n - 1): 
    a, b = map(int, input().split(' '))
    edges[a].append(b)
    edges[b].append(a)


# 首先:進行深度優先搜索(DFS)以找到距離0最遠的位置。它是最長路徑的端點之一。
visited = [False] * n          # 初始設定第一個DFS的訪問記錄
(_, endpoint) = dfs(0)         # (_, endpoint) 是 Tuple       

# 其次:同樣透過DFS找尋離“端點”最遠的點。 該點也是最長路徑的端點。
visited = [False] * n          # 初始化第二次DFS的訪問記錄
(ans, _) = dfs(endpoint)       # (ans, _) 是 Tuple， 找到最原距離放入 ans

print(ans)  # 印出最原距離

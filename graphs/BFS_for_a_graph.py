from collections import deque


def bfs(adj, s):
    visited = [False] * len(adj)
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        s = q.popleft()
        print(s, end=" ")
        for u in adj[s]:
            if visited[u] is False:
                q.append(u)
                visited[u] = True


s = 0
adj = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [1, 2, 4], [2, 3]]
bfs(adj, s)



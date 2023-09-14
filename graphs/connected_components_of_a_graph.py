from collections import deque


def bfs(adj, s, visited):
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        s = q.popleft()
        for u in adj[s]:
            if visited[u] is False:
                q.append(u)
                visited[u] = True


def countConnected(adj):
    visited = [False] * len(adj)
    count = 0
    for u in range(len(adj)):
        if visited[u] is False:
            count += 1
            bfs(adj, u, visited)
    return count


adj = [[1, 2], [0, 2], [0, 1], [4], [3], [6, 7], [5], [5]]
print(countConnected(adj))

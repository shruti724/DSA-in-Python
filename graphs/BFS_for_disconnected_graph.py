from collections import deque


def BFSRec(adj, s, visited):
    q = deque()
    q.append(s)
    visited[s] = True
    s = q.popleft()
    print(s, end=" ")
    while q:
        for u in adj[s]:
            if visited[u] is False:
                q.append(u)
                visited[u] = True


def BFSdis(adj):
    visited = [False] * len(adj)
    for u in range(len(adj)):
        if visited[u] is False:
            BFSRec(adj, u, visited)


adj = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [1, 2, 4], [2, 3]]
BFSdis(adj)

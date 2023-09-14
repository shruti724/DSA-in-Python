class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

def krushkal_MST():
    pass


n = int(input())
E = int(input())
adj = [([] for i in range(E)) for j in range(n)]
# edge = Edge(0, 1, 1)
print(adj)

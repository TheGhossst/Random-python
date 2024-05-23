class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def findset(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.findset(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.findset(u)
        root_v = self.findset(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    edges.sort()
    ds = DisjointSet(n)
    mst = []
    total_weight = 0

    for weight, u, v in edges:
        if ds.findset(u) != ds.findset(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

def is_minimum_spanning_tree(n, edges, given_tree):
    mst_edges, mst_weight = kruskal(n, edges)
    given_tree_weight = sum(weight for _, _, weight in given_tree)

    mst_set = set((min(u, v), max(u, v)) for u, v, _ in mst_edges)
    given_tree_set = set((min(u, v), max(u, v)) for u, v, _ in given_tree)
    
    return mst_set == given_tree_set and mst_weight == given_tree_weight


n = 4 
edges = [
    (1, 0, 1),
    (3, 0, 2),
    (4, 0, 3),
    (2, 1, 2),
    (5, 2, 3)
]

given_tree = [
    (0, 1, 1),
    (1, 2, 2),
    (2, 3, 5)
]

print(is_minimum_spanning_tree(n, edges, given_tree)) 

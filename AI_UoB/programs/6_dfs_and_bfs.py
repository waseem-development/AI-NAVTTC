from collections import deque

class Graph:
    def __init__(self, vertex):
        self.mat = [[0]*vertex for x in range(vertex)]
        self.size = vertex

    def add_edge(self, src, dest):
        if ((0 <= src < self.size) and (0 <= dest < self.size)):
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else:
            print("Invalid Edge")

    def remove_edge(self, src, dest):
        if((0 <= src < self.size) and (0 <= dest < self.size)):
            self.mat[src][dest] = 0
            self.mat[dest][src] = 0  # ← fixed bug (was src,dest twice)
        else:
            print("Invalid Edge")

    def dfs(self, src):
        visited = [False] * self.size
        stack = [src]
        while stack:
            v = stack.pop()
            if visited[v] == False:
                print(v, end=" -> ")
                visited[v] = True
                for i in range(self.size):
                    if self.mat[v][i] == 1 and visited[i] == False:
                        stack.append(i)

    def bfs(self, src):
        visited = [False] * self.size
        queue = deque([src])
        visited[src] = True
        while queue:
            v = queue.popleft()
            print(v, end=" -> ")
            for i in range(self.size):
                if self.mat[v][i] == 1 and visited[i] == False:
                    visited[i] = True
                    queue.append(i)

    def print_graph(self):
        print("  ", end="")
        for i in range(self.size):
            print(i, end=" ")
        print()
        for i, row in enumerate(self.mat):
            print(i, ' '.join(map(str, row)))

if __name__ == "__main__":
    g = Graph(6)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)

    print("Adjacency Matrix:")
    g.print_graph()

    print("\nDFS from vertex 0: ", end="")
    g.dfs(0)

    print("\nBFS from vertex 0: ", end="")
    g.bfs(0)

    print("\n\nRemoving edge 0-1...")
    g.remove_edge(0, 1)
    g.print_graph()
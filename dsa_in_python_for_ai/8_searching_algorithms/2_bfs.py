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
        if ((0 <= src < self.size) and (0 <= dest < self.size)):
            
            self.mat[src][dest] = 0
            self.mat[dest][src] = 0

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
            v = queue.popleft() # Takeout the very first item from the queue so that it can be printed and processed.
            print(v, end = " ")

            for i in range(self.size):
                if self.mat[v][i] == 1 and visited[i] == False:
                    visited[i] = True
                    queue.append(i) # appending neighbors so thet can e visited and processed later 

        
            
    def print_graph(self):

        for row in self.mat:

            print(' '.join(map(str, row)))


g = Graph(7)  # 7 nodes: 0,1,2,3,4,5,6
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(5,6)

g.print_graph()

print("\nDFS Traversal:")

g.bfs(0)   # start from node 1
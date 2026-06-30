def bfs(graph, start, target):
    queue = [start]
    visited = set()
    traversal_order = []
    
    while queue:
        node = queue.pop(0)
        
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)

            if node == target:
                return traversal_order, True
            
            for neighbor in graph[node]:
                queue.append(neighbor)
    return traversal_order, False

def input_graph():
    graph = {}
    while True:
        try:
            num_nodes = int(input("Enter the number of nodes: "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    for _ in range(num_nodes):
        node = input("Enter the node: ")
        neighbors = input(f"Enter the neighbors of {node} (comma separated): ").split(",")
        graph[node] = [n.strip() for n in neighbors if n.strip()]

    return graph
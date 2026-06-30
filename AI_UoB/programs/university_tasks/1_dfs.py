def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    traversal_order = []

    while stack:
        node, path = stack.pop()
        
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)

            if node == goal:
                break

            for neighbor in reversed(graph.get(node, [])):
                stack.append((neighbor, path + [neighbor]))
    return traversal_order

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

if __name__ == "__main__":
    graph = input_graph()
    start = input("Enter the starting node: ")
    target = input("Enter the target node: ")

    traversal = dfs(graph, start, target)
    print("\n DFS traversal")
    print(" -> ".join(traversal))
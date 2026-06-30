def depth_limited_search(graph, node, goal, depth_limit, visited):
    if node == goal:
        return [node]

    if depth_limit == 0:
        return None

    visited.add(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            result = depth_limited_search(
                graph,
                neighbor,
                goal,
                depth_limit - 1,
                visited
            )

            if result:
                return [node] + result

    visited.remove(node)  
    return None


def iterative_deepening_search(graph, start, goal, max_depth):
    for depth_limit in range(max_depth + 1):
        visited = set()  
        result = depth_limited_search(
            graph,
            start,
            goal,
            depth_limit,
            visited
        )

        if result:
            return result

    return None


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
        neighbors = input(
            f"Enter the neighbors of {node} (comma separated): "
        ).split(",")

        graph[node] = [n.strip() for n in neighbors if n.strip()]

    return graph


if __name__ == "__main__":
    graph = input_graph()

    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    max_depth = int(input("Enter the maximum depth: "))

    path = iterative_deepening_search(
        graph,
        start_node,
        goal_node,
        max_depth
    )

    if path:
        print(f"\nGoal '{goal_node}' found!")
        print("Path:", " -> ".join(path))
    else:
        print(f"\nGoal '{goal_node}' not found within depth {max_depth}.")
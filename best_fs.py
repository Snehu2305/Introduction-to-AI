from queue import PriorityQueue


def best_first_search(graph, start, goal, heuristic):
    visited = set()  
    pq = PriorityQueue()

    print("Best First Search Path:")

    while not pq.empty():
        (h, current_node) = pq.get()
        print(current_node, end=" ")

        if current_node == goal:
            print("\nGoal reached!")
            return

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

    print("\nGoal not reachable.")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}


heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 0  # Goal node
}


best_first_search(graph, 'A', 'G', heuristic)

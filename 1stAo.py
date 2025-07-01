class Graph:
    def __init__(self, graph, heuristics):
        self.graph = graph
        self.heuristics = heuristics
        self.solution_graph = {}

    def get_neighbors(self, node):
        return self.graph.get(node, [])

    def a_star_search(self, start_node):
        open_set = set([start_node])
        visited = set()
        current_node = start_node
        self.solution_graph = {}

        while open_set:
            if visited is None:
                visited = set()

            visited.add(current_node)
            min_cost = float('inf')
            best_path = []

            for neighbor, cost in self.get_neighbors(current_node):
                if neighbor not in visited:
                    total_cost = cost + self.heuristics[neighbor]
                    if total_cost <= min_cost:
                        min_cost = total_cost
                        best_path = neighbor
                        self.solution_graph[current_node] = neighbor

            if not best_path:
                break

            current_node = best_path
            open_set = set([current_node])

        return self.solution_graph


# Graph and heuristics
graph = {
    'A': [('B', 1), ('C', 7)],
    'B': [('D', 1), ('E', 1)],
    'C': [('F', 1)],
    'D': [('G', 1), ('H', 2)],
    'E': [('I', 1)],
    'F': [('J', 2)],
    'G': [('J', 3)],
    'H': [('J', 2)],
    'I': [('J', 0)],
    'J': []
}

heuristics = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}

# Run A* Search
a_star = Graph(graph, heuristics)
root_node = 'A'
solution = a_star.a_star_search(root_node)

# Output the solution graph
print("Solution Graph:", solution)

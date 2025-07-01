import random

# Distance matrix representing distances between cities
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def total_distance(path):
    """Calculate total distance of the given path (including return to start)."""
    total = 0
    for i in range(len(path) - 1):
        total += distance_matrix[path[i]][path[i + 1]]
    total += distance_matrix[path[-1]][path[0]]  # Return to start
    return total

def hill_climbing_tsp(num_cities, max_iterations=10000):
    current_path = list(range(num_cities))  # Start with default ordered path
    random.shuffle(current_path)  # Shuffle to start with a random solution
    current_distance = total_distance(current_path)

    for _ in range(max_iterations):
        # Create neighbor by swapping two random cities
        neighbor_path = current_path.copy()
        i, j = random.sample(range(num_cities), 2)
        neighbor_path[i], neighbor_path[j] = neighbor_path[j], neighbor_path[i]

        neighbor_distance = total_distance(neighbor_path)

        # Move to neighbor if better
        if neighbor_distance < current_distance:
            current_path = neighbor_path
            current_distance = neighbor_distance
            # Optional: Print when improvement is found
            # print(f"Improved path: {current_path} with distance: {current_distance}")

    return current_path, current_distance

def main():
    num_cities = 4
    best_path, best_distance = hill_climbing_tsp(num_cities)

    print("Optimal path:", best_path)
    print("Total distance:", best_distance)

if __name__ == "__main__":
    main()

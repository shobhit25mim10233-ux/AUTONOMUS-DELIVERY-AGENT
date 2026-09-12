import heapq
from collections import deque

# =================================================================
# Heuristic Function for A* Search
# =================================================================
def manhattan_distance(point_a, point_b):
    """
    Returns the Manhattan distance between two points on a grid.
    This helps A* estimate how far it is from the goal.
    """
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

# =================================================================
# Breadth-First Search (BFS)
# =================================================================
def bfs(grid, start, goal):
    """
    Finds the shortest path from start to goal using BFS.
    Explores the grid layer by layer.
    Returns a list of steps or None if no path exists.
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [start])])
    visited = {start}
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path

        for dr, dc in directions:
            neighbor = (current[0]+dr, current[1]+dc)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
    return None

# =================================================================
# Depth-First Search (DFS)
# =================================================================
def dfs(grid, start, goal):
    """
    Finds a path from start to goal using DFS.
    Explores deeply before backtracking.
    Returns a list of steps or None if no path exists.
    """
    rows, cols = len(grid), len(grid[0])
    stack = [(start, [start])]
    visited = {start}
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while stack:
        current, path = stack.pop()
        if current == goal:
            return path

        for dr, dc in reversed(directions):
            neighbor = (current[0]+dr, current[1]+dc)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, path + [neighbor]))
    return None

# =================================================================
# A* Search
# =================================================================
def a_star_search(grid, start, goal):
    """
    Finds the most fuel-efficient path using A* search.
    Each step costs 1 fuel unit.
    Returns a list of steps or None if no path exists.
    """
    rows, cols = len(grid), len(grid[0])
    open_list = [(manhattan_distance(start, goal), 0, start, [start])]
    min_fuel = {start: 0}
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while open_list:
        _, fuel_used, current, path = heapq.heappop(open_list)
        if current == goal:
            return path

        for dr, dc in directions:
            neighbor = (current[0]+dr, current[1]+dc)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 0:
                    new_fuel = fuel_used + 1
                    if new_fuel < min_fuel.get(neighbor, float('inf')):
                        min_fuel[neighbor] = new_fuel
                        f_score = new_fuel + manhattan_distance(neighbor, goal)
                        heapq.heappush(open_list, (f_score, new_fuel, neighbor, path + [neighbor]))
    return None

# =================================================================
# Grid Visualization
# =================================================================
def visualize_path(grid, path, start, goal, algorithm_name):
    """
    Prints the grid and highlights the path.
    S = Start, G = Goal, # = Obstacle, . = Path
    """
    print(f"\n--- {algorithm_name} ---")
    if not path:
        print("No path found.")
        return

    display = [row[:] for row in grid]

    for r, c in path:
        display[r][c] = '.'

    display[start[0]][start[1]] = 'S'
    display[goal[0]][goal[1]] = 'G'

    for row in display:
        print(" ".join(str(cell).replace('1', '#').replace('0', ' ') for cell in row))

    print(f"Steps: {len(path)-1}, Fuel used: {len(path)-1}")

# =================================================================
# Main Interactive Menu
# =================================================================
def main_menu():
    grid = [
        [0,0,0,0,1,0,0,0],
        [0,1,1,0,1,0,1,0],
        [0,0,0,0,0,0,0,0],
        [1,1,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0]
    ]
    start = (0,0)
    goal = (4,7)

    print("Autonomous Delivery Agent Pathfinding Simulator")

    while True:
        print("\n1. A* Search (Fuel Optimized)")
        print("2. Breadth-First Search (BFS)")
        print("3. Depth-First Search (DFS)")
        print("4. Run All")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            path = a_star_search(grid, start, goal)
            visualize_path(grid, path, start, goal, "A* Search")
        elif choice == '2':
            path = bfs(grid, start, goal)
            visualize_path(grid, path, start, goal, "BFS")
        elif choice == '3':
            path = dfs(grid, start, goal)
            visualize_path(grid, path, start, goal, "DFS")
        elif choice == '4':
            path = a_star_search(grid, start, goal)
            visualize_path(grid, path, start, goal, "A* Search")

            path = bfs(grid, start, goal)
            visualize_path(grid, path, start, goal, "BFS")

            path = dfs(grid, start, goal)
            visualize_path(grid, path, start, goal, "DFS")

            print("\nA* and BFS find the shortest path. DFS finds a valid path but may be longer.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()

import matplotlib.pyplot as plt
import numpy as np
import heapq

def create_grid_map(rows, cols, obstacles=[], robot_start=(0, 0), goal=(0, 0)):
    grid_map = np.zeros((rows, cols))
    for obstacle in obstacles:
        row, col = obstacle
        grid_map[row][col] = 1
    robot_row, robot_col = robot_start
    grid_map[robot_row][robot_col] = 2
    goal_row, goal_col = goal
    grid_map[goal_row][goal_col] = 4
    return grid_map

def visualize_grid_map(grid_map):
    plt.imshow(grid_map, cmap='binary', interpolation='none')
    plt.colorbar()
    start = np.where(grid_map == 2)
    goal = np.where(grid_map == 4)
    plt.scatter(start[1][0], start[0][0], color='red', marker='s', label='Start')
    plt.scatter(goal[1][0], goal[0][0], color='green', marker='s', label='Goal')
    path = np.where(grid_map == 5)
    if path[0].size > 0:
        path = list(zip(path[1], path[0]))
        plt.plot(path[:, 0], path[:, 1], color='blue', linewidth=2, label='Path')
    plt.legend()
    plt.show()

def possible_moves(robot_position, grid_map):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # up, down, right, left
    valid_moves = []

    for move in moves:
        new_row, new_col = robot_position[0] + move[0], robot_position[1] + move[1]
        if 0 <= new_row < grid_map.shape[0] and 0 <= new_col < grid_map.shape[1] and grid_map[new_row][new_col] == 0:
            valid_moves.append(move)

    return valid_moves

def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def find_path(grid_map, start, goal):
    frontier = [(euclidean_distance(start, goal), 0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while frontier:
        _, current_cost, current = heapq.heappop(frontier)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path = path[::-1]
            for point in path:
                grid_map[point[0]][point[1]] = 5
            return path, grid_map

        for move in possible_moves(current, grid_map):
            neighbor = (current[0] + move[0], current[1] + move[1])
            new_cost = current_cost + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + euclidean_distance(neighbor, goal)
                heapq.heappush(frontier, (priority, new_cost, neighbor))
                came_from[neighbor] = current

    return [], grid_map

rows = 10
cols = 10
obstacles = [(2, 2), (3, 4), (5, 7)]
start = (0, 1)
goal = (8, 8)

grid_map = create_grid_map(rows, cols, obstacles, start, goal)
path, grid_map = find_path(grid_map, start, goal)
visualize_grid_map(grid_map)




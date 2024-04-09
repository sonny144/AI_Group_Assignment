import math

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()  # Set of coordinates of obstacles

    def add_obstacle(self, x, y):
        self.obstacles.add((x, y))

    def is_obstacle(self, x, y):
        return (x, y) in self.obstacles

    def get_possible_actions(self, x, y):
        actions = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.width and 0 <= new_y < self.height and not self.is_obstacle(new_x, new_y):
                actions.append((dx, dy))
        return actions

    def cost_function(self, action):
        # Simple unit cost function
        return 1

    def heuristic_function(self, current_pos, target_pos):
        # Calculate Euclidean distance considering obstacles
        min_distance = float('inf')
        for obstacle in self.obstacles:
            obstacle_distance = math.sqrt((current_pos[0] - obstacle[0])**2 + (current_pos[1] - obstacle[1])**2)
            min_distance = min(min_distance, obstacle_distance)
        remaining_distance = math.sqrt((current_pos[0] - target_pos[0])**2 + (current_pos[1] - target_pos[1])**2)
        return remaining_distance + min_distance

    def astar_search(self, start_pos, target_pos):
        open_list = [(start_pos, 0, self.heuristic_function(start_pos, target_pos), [], 0)]  # Include cost in the tuple
        closed_list = set()

        while open_list:
            current_pos, g, h, path, total_cost = min(open_list, key=lambda x: x[1] + x[2])
            open_list.remove((current_pos, g, h, path, total_cost))
            closed_list.add(current_pos)

            if current_pos == target_pos:
                return path + [current_pos], total_cost  # Return the path and total cost when the target is reached

            for action in self.get_possible_actions(*current_pos):
                next_pos = (current_pos[0] + action[0], current_pos[1] + action[1])
                if next_pos in closed_list:
                    continue

                new_g = g + self.cost_function(action)
                new_h = self.heuristic_function(next_pos, target_pos)
                new_path = path + [current_pos]
                new_total_cost = total_cost + self.cost_function(action)  # Update total cost

                if (next_pos, g, h, path, total_cost) not in open_list or new_g + new_h < h:
                    open_list.append((next_pos, new_g, new_h, new_path, new_total_cost))

        return None, None  # No path found

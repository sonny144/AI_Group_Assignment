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
        if x > 0 and not self.is_obstacle(x - 1, y):
            actions.append((-1, 0))  # Move left
        if x < self.width - 1 and not self.is_obstacle(x + 1, y):
            actions.append((1, 0))   # Move right
        if y > 0 and not self.is_obstacle(x, y - 1):
            actions.append((0, -1))  # Move up
        if y < self.height - 1 and not self.is_obstacle(x, y + 1):
            actions.append((0, 1))   # Move down
        return actions

    def cost_function(self, action):
        # Simple unit cost function
        return 1

    def heuristic_function(self, current_pos, target_pos):
        # Simple Manhattan distance heuristic
        return abs(current_pos[0] - target_pos[0]) + abs(current_pos[1] - target_pos[1])

    def astar_search(self, start_pos, target_pos):
        open_list = [(start_pos, 0, self.heuristic_function(start_pos, target_pos), [])]
        closed_list = set()

        while open_list:
            current_pos, g, h, path = min(open_list, key=lambda x: x[1] + x[2])
            open_list.remove((current_pos, g, h, path))
            closed_list.add(current_pos)

            if current_pos == target_pos:
                return path + [current_pos]

            for action in self.get_possible_actions(*current_pos):
                next_pos = (current_pos[0] + action[0], current_pos[1] + action[1])
                if next_pos in closed_list:
                    continue

                new_g = g + self.cost_function(action)
                new_h = self.heuristic_function(next_pos, target_pos)
                new_path = path + [current_pos]

                if (next_pos, g, h, path) not in open_list or new_g + new_h < h:
                    open_list.append((next_pos, new_g, new_h, new_path))

        return None  # No path found

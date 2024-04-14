import math #we import the math module which gives us access to different functions

class Environment: # create a class called environment which will act as the blueprint with its height and width
    def __init__(self, width, height): #defines class constructor method _init_. is a special method in Python classes that is automatically called when an object of the class is created.
        self.width = width #gives current instance of environment class
        self.height = height
        self.obstacles = set()  # Set of coordinates of obstacles

    def add_obstacle(self, x, y): # function to add obstacles
        self.obstacles.add((x, y)) # takes in the x and y coordinates of the obstacle

    def is_obstacle(self, x, y): # function to confirm that the obstacle exists
        return (x, y) in self.obstacles # it will return true if the coordinates exist in the tuple

    def get_possible_actions(self, x, y): #function that defines what actions we can take to move
        actions = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #Iterates over a list of tuples, where each tuple represents a change in position (movement) in the x and y directions. This allows movement in four directions: left, right, up, and down.
            new_x, new_y = x + dx, y + dy # calcuate new postion based on change
            if 0 <= new_x < self.width and 0 <= new_y < self.height and not self.is_obstacle(new_x, new_y): # makes sure they are valid coordinates
                actions.append((dx, dy)) #adds to actions list.
        return actions

    def cost_function(self, action): #sets the cost of every action to one.
        # Simple unit cost function
        return 1

    def heuristic_function(self, current_pos, target_positions):
        min_distance = float('inf') # variable min_distance is initialized to positive infinity. Keep track of minimun distance from current position to any obstacle
        for obstacle in self.obstacles: #iterates over different obstacles
            obstacle_distance = math.sqrt((current_pos[0] - obstacle[0])**2 + (current_pos[1] - obstacle[1])**2)#calculates  Euclidean distance.
            min_distance = min(min_distance, obstacle_distance) # sets min_distance to minimum of current value. Ensures it is the smallest distance
        
        if isinstance(target_positions, tuple):
            target_positions = [target_positions]  # checks first to see if its a tuple, if not convert to list if it's a single position
        
        remaining_distance = float('inf') #track the shortest distance from the current position to any of the target positions.
        for target_pos in target_positions:
            target_distance = math.sqrt((current_pos[0] - target_pos[0])**2 + (current_pos[1] - target_pos[1])**2) #euclidean distance
            remaining_distance = min(remaining_distance, target_distance)
        return remaining_distance + min_distance #returns the heuristic value 

    def astar_search(self, start_pos, target_positions): #defines a*function
        open_list = [(start_pos, 0, self.heuristic_function(start_pos, target_positions), [], 0)] #pq containing nodes to be evaluated
        closed_list = set() # stores visited positions

        while open_list: #continues until list is empty meaning all valid positions have been checked
            current_pos, g, h, path, total_cost = min(open_list, key=lambda x: x[1] + x[2]) #finds node with the minimum cost
            open_list.remove((current_pos, g, h, path, total_cost))
            closed_list.add(current_pos)

            if current_pos in target_positions:
                return path + [current_pos], total_cost  # Returns the path and total cost when one of the targets is reached

            for action in self.get_possible_actions(*current_pos): # it loops through all the possible actions
                next_pos = (current_pos[0] + action[0], current_pos[1] + action[1])#This calculates the next position by adding the action's delta values to the current position's coordinates
                if next_pos in closed_list: #checks if the position was already evaluated
                    continue

                new_g = g + self.cost_function(action) #This calculates the new cost (new_g) by adding the cost of the action to the current cost (g).
                new_h = self.heuristic_function(next_pos, target_positions)# calculates the new heuristic value (new_h) for the next position based on its estimated distance to the target positions
                new_path = path + [current_pos]
                new_total_cost = total_cost + self.cost_function(action)  #his calculates the new total cost (new_total_cost) by adding the cost of the action to the current total cost (total_cost).

                if (next_pos, g, h, path, total_cost) not in open_list or new_g + new_h < h: #checks if value is less than previous h(n)
                    open_list.append((next_pos, new_g, new_h, new_path, new_total_cost))

        return None, None  # No path found

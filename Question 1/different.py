import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define the size of the grid
grid_size = 10

# Create an empty grid
grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

# Define the starting position of the robot
robot_pos = [0, 0]

# Define the direction the robot is facing (0: up, 1: right, 2: down, 3: left)
robot_dir = 1

# Define a function to move the robot in the grid
def move_robot(grid, robot_pos, robot_dir, dx, dy):
    # Calculate the new position of the robot
    new_pos = [robot_pos[0] + dx, robot_pos[1] + dy]
    
    # Check if the new position is within the grid
    if 0 <= new_pos[0] < grid_size and 0 <= new_pos[1] < grid_size:
        # Update the grid with the new position of the robot
        grid[robot_pos[0]][robot_pos[1]] = ' '
        grid[new_pos[0]][new_pos[1]] = 'R'
        robot_pos = new_pos
    else:
        print("Error: Robot cannot move outside the grid")
    
    # Update the direction of the robot
    if dx == 1:
        robot_dir = 1
    elif dx == -1:
        robot_dir = 3
    elif dy == 1:
        robot_dir = 2
    elif dy == -1:
        robot_dir = 0
    
    return grid, robot_pos, robot_dir

# Define a function to visualize the grid
def visualize_grid(grid):
    # Create a new figure
    plt.figure(figsize=(10, 10))
    
    # Create a new axes
    ax = plt.axes()
    
    # Plot the grid
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 'R':
                ax.add_patch(patches.Rectangle((j, i), 1, 1, fill=True, color='red'))
            else:
                ax.add_patch(patches.Rectangle((j, i), 1, 1, fill=True, color='white'))
    
    # Set the limits of the axes
    plt.xlim(0, grid_size)
    plt.ylim(0, grid_size)
    
    # Remove the axes labels
    plt.axis('off')
    
    # Show the plot
    plt.show()

# Move the robot in the grid
grid, robot_pos, robot_dir = move_robot(grid, robot_pos, robot_dir, 1, 0)

# Visualize the grid
visualize_grid(grid)
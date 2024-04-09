from environment import Environment
from visualization import Visualization

# Create an instance of the Environment class
env = Environment(30, 30)
env.add_obstacle(4, 0) 
env.add_obstacle(20,1)# Add obstacle 

# Define the starting and target positions
start_pos = (0, 0)
target_pos = (27, 2)

# Perform A* search to find the optimal path
path = env.astar_search(start_pos, target_pos)

# Visualization
visualization = Visualization(env)
visualization.plot_environment()  # Plot the environment

if path is not None:
    visualization.plot_path(path)  # Plot the optimal path
else:
    print("No valid path found from the starting position to the target position.")

visualization.plot_robot(start_pos)  # Plot the robot's initial position
visualization.show()  # Display the visualization

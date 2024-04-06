from environment import Environment
from visualization import Visualization

# Test environment and A* search
env = Environment(6, 6)
env.add_obstacle(2, 2)


start_pos = (0, 0)
target_pos = (3, 4)
path = env.astar_search(start_pos, target_pos)

# Visualization
visualization = Visualization(env)
visualization.plot_environment()
visualization.plot_path(path)
visualization.plot_robot(start_pos)
visualization.show()
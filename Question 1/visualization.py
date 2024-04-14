import numpy as np
import matplotlib.pyplot as plt

class Visualization:
    def __init__(self, environment):
        self.env = environment
        self.fig, self.ax = plt.subplots()

    def plot_environment(self):
        # Plot the environment as a grid
        grid = np.zeros((self.env.height, self.env.width))
        for obstacle in self.env.obstacles:
            grid[obstacle[1], obstacle[0]] = 1

        self.ax.imshow(grid, cmap='binary', interpolation='nearest', extent=[0, self.env.width, 0, self.env.height])
        self.ax.grid(True, color='black')

    def plot_path(self, path, color='blue'):  
        if path is not None:
            for i, pos in enumerate(path):
                if i > 0:
                    prev_pos = path[i-1]
                    g_value = self.env.cost_function((pos[0] - prev_pos[0], pos[1] - prev_pos[1]))
                    h_value = self.env.heuristic_function(pos, path[-1])
                    self.ax.add_patch(plt.Rectangle((pos[0], pos[1]), 1, 1, color=color))
                    self.ax.text(pos[0] + 0.5, pos[1] + 0.5, f"g={g_value:.1f}, h={h_value:.1f}", fontsize=8, ha='center', va='center')

    def plot_robot(self, position):
        self.ax.plot(position[0] + 0.5, position[1] + 0.5, marker='s', color='red')

    def show(self):
        plt.gca().invert_yaxis()  
        plt.show()
import numpy as np
import matplotlib.pyplot as plt

class Visualization:
    def __init__(self, environment):
        self.env = environment
        self.fig, self.ax = plt.subplots()

    def plot_environment(self):
        grid = np.zeros((self.env.height, self.env.width))
        for obstacle in self.env.obstacles:
            grid[obstacle[1], obstacle[0]] = 1

        self.ax.imshow(grid, cmap='binary')

    def plot_path(self, path, color='blue'):  # Updated to accept a color argument
        if path is not None:
            for pos in path:
                self.ax.plot(pos[0], pos[1], marker='o', color=color)

    def plot_robot(self, position):
        self.ax.plot(position[0], position[1], marker='s', color='red')

    def show(self):
        plt.gca().invert_yaxis()  # Invert y-axis to match grid coordinates
        plt.show()

import numpy as np # numpy is used for numerical computations
import matplotlib.pyplot as plt # Matplotlib is a plotting library for Python.

class Visualization:
    def __init__(self, environment):
        self.env = environment
        self.fig, self.ax = plt.subplots() #fig represents the entire figure, and ax represents a subplot within the figure.

    def plot_environment(self):
        #  Here we plot the environment as a grid
        grid = np.zeros((self.env.height, self.env.width)) #Creates a NumPy array of zeros with dimensions specified by the height and width of the environment.
        for obstacle in self.env.obstacles:
            grid[obstacle[1], obstacle[0]] = 1

        self.ax.imshow(grid, cmap='binary', interpolation='nearest', extent=[0, self.env.width, 0, self.env.height]) #Displays the grid using Matplotlib's imshow() function. The cmap parameter specifies the colormap
        self.ax.grid(True, color='black') #colors obtacles black

    def plot_path(self, path, color='blue'):  
        if path is not None:
            for i, pos in enumerate(path):
                if i > 0:
                    prev_pos = path[i-1]
                    g_value = self.env.cost_function((pos[0] - prev_pos[0], pos[1] - prev_pos[1])) #Computes the cost of moving from the previous position to the current position using the environment's cost_function().
                    h_value = self.env.heuristic_function(pos, path[-1]) #Computes the heuristic value for the current position using the environment's heuristic_function().
                    self.ax.add_patch(plt.Rectangle((pos[0], pos[1]), 1, 1, color=color))
                    self.ax.text(pos[0] + 0.5, pos[1] + 0.5, f"g={g_value:.1f}, h={h_value:.1f}", fontsize=8, ha='center', va='center')

    def plot_robot(self, position):
        self.ax.plot(position[0] + 0.5, position[1] + 0.5, marker='s', color='red')

    def show(self):
        plt.gca().invert_yaxis()  
        plt.show() #display plot
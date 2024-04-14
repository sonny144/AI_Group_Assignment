from environment import Environment
from visualization import Visualization

def test_simple_environment(): #define function to test
    # Test case 1 for environment with 2 obstacles
    env1 = Environment(6, 6) #creates environment with height and width of 6,6
    env1.add_obstacle(2, 2) #adds obstacle coordinates
    env1.add_obstacle(5, 3)
    start_pos1 = (1, 1) # starting position
    target_positions1 = [(5,5)]  #target position

    path_manhattan1, cost_manhattan1 = env1.astar_search(start_pos1, target_positions1) # calculates the path and cost using Manhattan heuristic.
    path_obstacle_aware1, cost_obstacle_aware1 = env1.astar_search(start_pos1, target_positions1)#uses obstacle aware heuristic now

    print("Total Cost for Simple Environment with Obstacles (Manhattan Heuristic):", cost_manhattan1)
    print("Total Cost for Simple Environment with Obstacles (Obstacle-aware Heuristic):", cost_obstacle_aware1)

    # Visualization
    visualization1 = Visualization(env1) # creates instance of visualization with env1 as argument
    visualization1.plot_environment()
    visualization1.plot_path(path_obstacle_aware1, color='blue')  # sets Different color for each path. This one is blue
    visualization1.plot_robot(start_pos1)
    visualization1.show()

def test_complex_environment():
    # Test case 2 environment with 3 obstacles
    env2 = Environment(8, 8)
    env2.add_obstacle(2, 2)
    env2.add_obstacle(3, 3)
    env2.add_obstacle(7,6)
    start_pos2 = (0, 0)
    target_positions2 = [(7, 7)]  #target position

    path_manhattan2, cost_manhattan2 = env2.astar_search(start_pos2, target_positions2)
    path_obstacle_aware2, cost_obstacle_aware2 = env2.astar_search(start_pos2, target_positions2)

    print("Total Cost for Complex Environment with Obstacles (Manhattan Heuristic):", cost_manhattan2)
    print("Total Cost for Complex Environment with Obstacles (Obstacle-aware Heuristic):", cost_obstacle_aware2)

    # Visualization
    visualization2 = Visualization(env2)
    visualization2.plot_environment()
    visualization2.plot_path(path_obstacle_aware2, color='red')  # Different color for each path.This one is red
    visualization2.plot_robot(start_pos2)
    visualization2.show()

def test_moderate_environment():
    # Test case 3
    env3 = Environment(10, 10)
    env3.add_obstacle(2, 2)
    env3.add_obstacle(4, 4)
    env3.add_obstacle(6, 4)
    start_pos3 = (0, 0)
    target_positions3 = [(8, 9)]  # target

    path_manhattan3, cost_manhattan3 = env3.astar_search(start_pos3, target_positions3)
    path_obstacle_aware3, cost_obstacle_aware3 = env3.astar_search(start_pos3, target_positions3)

    print("Total Cost for Moderate Environment with Obstacles (Manhattan Heuristic):", cost_manhattan3)
    print("Total Cost for Moderate Environment with Obstacles (Obstacle-aware Heuristic):", cost_obstacle_aware3)

    # Visualization 
    visualization3 = Visualization(env3)
    visualization3.plot_environment()
    visualization3.plot_path(path_obstacle_aware3, color='green')  # Different color for each path. This is green
    visualization3.plot_robot(start_pos3)
    visualization3.show()

# Execute the test cases
if __name__ == "__main__": #checks if it is run as the main program
    test_simple_environment()
    test_complex_environment()
    test_moderate_environment()
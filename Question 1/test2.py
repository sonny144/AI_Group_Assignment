from environment import Environment
from visualization import Visualization

def test_simple_environment():
    # Test case 1: Simple Environment
    env1 = Environment(6, 6)
    env1.add_obstacle(2, 2)
    start_pos1 = (0, 0)
    charging_station_pos1 = (5, 5)

    path_manhattan1, cost_manhattan1 = env1.astar_search(start_pos1, charging_station_pos1)
    path_obstacle_aware1, cost_obstacle_aware1 = env1.astar_search(start_pos1, charging_station_pos1)

    print("Total Cost for Simple Environment with Obstacles (Manhattan Heuristic):", cost_manhattan1)
    print("Total Cost for Simple Environment with Obstacles (Obstacle-aware Heuristic):", cost_obstacle_aware1)

    # Visualization (optional)
    visualization1 = Visualization(env1)
    visualization1.plot_environment()
    visualization1.plot_path(path_obstacle_aware1, color='blue')  # Different color for each path
    visualization1.plot_robot(start_pos1)
    visualization1.show()

def test_complex_environment():
    # Test case 2: Complex Environment
    env2 = Environment(8, 8)
    env2.add_obstacle(2, 2)
    env2.add_obstacle(3, 3)
    start_pos2 = (0, 0)
    charging_station_pos2 = (7, 7)

    path_manhattan2, cost_manhattan2 = env2.astar_search(start_pos2, charging_station_pos2)
    path_obstacle_aware2, cost_obstacle_aware2 = env2.astar_search(start_pos2, charging_station_pos2)

    print("Total Cost for Complex Environment with Obstacles (Manhattan Heuristic):", cost_manhattan2)
    print("Total Cost for Complex Environment with Obstacles (Obstacle-aware Heuristic):", cost_obstacle_aware2)

    # Visualization (optional)
    visualization2 = Visualization(env2)
    visualization2.plot_environment()
    visualization2.plot_path(path_obstacle_aware2, color='red')  # Different color for each path
    visualization2.plot_robot(start_pos2)
    visualization2.show()

def test_moderate_environment():
    # Test case 3: Moderate Environment
    env3 = Environment(10, 10)
    env3.add_obstacle(2, 2)
    env3.add_obstacle(4, 4)
    start_pos3 = (0, 0)
    charging_station_pos3 = (9, 9)

    path_manhattan3, cost_manhattan3 = env3.astar_search(start_pos3, charging_station_pos3)
    path_obstacle_aware3, cost_obstacle_aware3 = env3.astar_search(start_pos3, charging_station_pos3)

    print("Total Cost for Moderate Environment with Obstacles (Manhattan Heuristic):", cost_manhattan3)
    print("Total Cost for Moderate Environment with Obstacles (Obstacle-aware Heuristic):", cost_obstacle_aware3)

    # Visualization (optional)
    visualization3 = Visualization(env3)
    visualization3.plot_environment()
    visualization3.plot_path(path_obstacle_aware3, color='green')  # Different color for each path
    visualization3.plot_robot(start_pos3)
    visualization3.show()

# Execute the test cases
if __name__ == "__main__":
    test_simple_environment()
    test_complex_environment()
    test_moderate_environment()

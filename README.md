# AUTONOMUS-DELIVERY-AGENT
An Autonomous Delivery Agent uses AI to plan delivery routes, avoid obstacles, optimize schedules, and make real-time decisions. It aims to deliver packages efficiently with minimal human intervention while improving delivery time, cost, and reliability.
Autonomous Delivery Agent Pathfinding Simulator Project Overview

In today’s world, autonomous systems like delivery robots and self-driving vehicles rely heavily on efficient pathfinding to reach their destinations. This project simulates a simple Autonomous Delivery Agent that navigates through a grid-based environment while avoiding obstacles and finding the best possible route to its destination.

The main goal of this project is to understand and compare different pathfinding algorithms and observe how they behave in the same environment.

Problem Statement

The challenge is to design an intelligent agent that can move from a starting point to a goal location in a grid while:

Avoiding obstacles Minimizing distance (or fuel consumption) Choosing an efficient path Approach & Methodology

To solve this problem, three well-known search algorithms were implemented:

A* Search Algorithm

A* is used to find the most efficient path by combining:

The actual cost from the start (g(n)) An estimated cost to the goal using Manhattan Distance (h(n))

This makes A* both optimal and efficient, especially for grid-based navigation.

Breadth-First Search (BFS)

BFS explores the grid level by level and guarantees the shortest path in an unweighted environment. However, it may explore many unnecessary nodes, making it less efficient than A*.

Depth-First Search (DFS)

DFS explores as deep as possible before backtracking. It is simple but does not guarantee the shortest path, making it less reliable for optimal navigation.

Environment Representation

The environment is represented as a 2D grid:

0 → Free space 1 → Obstacle S → Start position G → Goal position . → Path taken by the agent

How the System Works
The grid is predefined with obstacles. The agent starts at position (0,0) and aims to reach (4,7). The user selects an algorithm from the menu. The chosen algorithm computes a path. The result is displayed visually in the console.

How to Run the Program
Make sure Python 3 is installed Save the file (e.g., pathfinding.py) Run the program: python pathfinding.py Choose an option from the menu to run a specific algorithm or all of them.

#Output Description

The program prints the grid showing:

The selected path Number of steps taken Fuel used (equal to steps)

Example:

--- A* Search --- S . . . # . . .

# . # . # .
. . . . . . .

# . # # # . .
. . . . . . G

Steps: 11, Fuel used: 11 Key Observations A* and BFS always find the shortest path A* is more efficient due to heuristic guidance DFS may find longer or less optimal paths

Applications
This project demonstrates concepts used in:

Autonomous delivery robots Self-driving cars Game AI navigation Robotics path planning Future Enhancements Add diagonal movement Introduce weighted paths (different fuel costs) Create a graphical interface (GUI) Simulate real-time movement of the agent

Conclusion
This project successfully demonstrates how different pathfinding algorithms work in a grid-based environment. It highlights the importance of choosing the right algorithm for efficiency and optimality in real-world autonomous systems

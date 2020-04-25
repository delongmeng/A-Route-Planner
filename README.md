# A* Route Planner

In this project, I built a route planner based on the A* algorithm, like the one used in Google Maps, to calculate the shortest path between two points on a map. Unlike the uniform cost search or greedy best-first search algorithms, A* tries to optimize with both the shortest path and the goal in mind. It works by minimizing f = g + h, where f is the total cost, g is path cost so far, and h (the heuristic function) is estimated distance to the goal. As a result, this search strategy finds the shortest length path while expanding minimum number of paths possible.     

http://htmlpreview.github.io/?https://github.com/delongmeng/A-Route-Planner/blob/master/project_notebook.html
(The map cannot be displayed for technical reasons, but all of the 'boring' codes are there.)

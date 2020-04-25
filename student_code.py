

# helper function to return distance
def distance(M,node1, node2):
    
    import math
    x1,y1 = M.intersections[node1][0], M.intersections[node1][1]
    x2,y2 = M.intersections[node2][0], M.intersections[node2][1]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def shortest_path(M,start,goal):

    import heapq

    # initialization of variables
    path = []  # shortest path
    explored_nodes = set()
    path_list = []
    start_path = [start]
    start_path_cost = 0
    start_est_distance = distance(M, start, goal)
    start_total_cost = start_path_cost + start_est_distance
    
    start_record = [total_cost_start, path_cost_start, est_distance_start_goal, start_path]
    heapq.heappush(path_list, start_record)

    while len(path_list)>0:
        
        # use a heap structure to pop out the path with the shortest total cost so far
        current_record = heapq.heappop(path_list)
        current_path = current_record[3]
        current_path_cost = current_record[1]
        current_node = current_record[3][-1]
        explored_nodes.add(current_node)
        
        # goal test
        if current_node == goal:
            path = current_path
            break

        # explore all of the new nodes that is connected with the current node
        for new_node in M.roads[current_node]:
            # ignore the ones already explored
            if new_node not in explored_nodes:
                # generate new paths for next round of exploration
                new_path = current_path + [new_node]
                new_path_cost = current_path_cost + distance(M, current_node, new_node)
                new_est_distance = distance(M, new_node, goal)
                new_total_cost = new_path_cost + new_est_distance
                new_record = [new_total_cost, new_path_cost, new_est_distance, new_path]
                heapq.heappush(path_list, new_record)

    print("shortest path called")
    return path


















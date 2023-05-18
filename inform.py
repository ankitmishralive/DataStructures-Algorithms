import heapq

graph = {

  'A':[('B',2),('C',3)],
  'B':[('D',4)],
  'C':[('D',1)],
  'D':[('E',5)],
  'E':[]
}

heuristic = {
    'A':9,
    'B':7,
    'C':5,
    'D':3,
    'E':0
}

def astar(start,goal):
    visited = set() 
    queue = []

    heapq.heappush(queue,(heuristic[start],start,[start],0))
    while queue:
        a,current,path,cost = heapq.heappop(queue)
        if current == goal:
            return path,cost 
        if current in visited:
            continue 
        visited.add(current)

    for neighbour, neighbour_cost in graph[current]:
        total_cost = cost + neighbour_cost 
        h = heuristic[neighbour]
        heapq.heappush(queue,(total_cost+h,neighbour,path+[neighbour],total_cost))


    return None 
start_node = str(input("Enter start node : ")).upper()
goal_node = str(input("Enter goal node : ")).upper()
path, cost = astar(start_node, goal_node)
print("\nPath :", path)
print("Path Cost :", cost)
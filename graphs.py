from collections import deque

def dfs_iter(graph, source):
    stack = list(source)
    while stack:
        vertex = stack.pop()
        print(vertex)
        stack.extend(x for x in graph[vertex])

def dfs_recursive(graph, source):
    print(source)
    for x in graph[source]:
        dfs_recursive(graph,x) 

def bfs_iter(graph, source):
    stack = deque(list(source))
    while stack:
        vertex = stack.popleft()
        print(vertex)
        stack.extend(x for x in graph[vertex])


def acyclic_graph_search_recursive(graph, src, des):
    if src == des:
        return True
    for x in graph[src]:
        if acyclic_graph_search_recursive(graph, x, des):
            return True
    return False

def cyclic_graph_search_recursive(graph, src, des, visited: set):  
    if src == des:
        return True
    if src in visited:
        return False
    visited.add(src)
    for x in graph[src]:
        if cyclic_graph_search_recursive(graph, x, des, visited):
            return True
    return False

def cyclic_graph_search_dfs_iter(graph, src, des, visited: set):  
    stack = list(src)
    
    while stack:
        current = stack.pop()
        if current not in visited:
            if current == des:
                return True
            visited.add(current)
            stack.extend(graph[current])
    return False

def cyclic_graph_search_bfs_iter(graph, src, des, visited: set):  
    stack = deque(list(src))
    
    while stack:
        current = stack.popleft()
        if current not in visited:
            if current == des:
                return True
            visited.add(current)
            stack.extend(graph[current])
    return False
   

def build_graph(edges):
    graph = {}
    for edge in edges:
        a,b = edge
        if a not in graph.keys():
            graph[a] = []
        if b not in graph.keys():
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def number_of_connected_graphs_dfs_iter(graph):  
    visited = set()
    count = 0
    for x in graph.keys():
        stack = list(x)
        initLength = len(visited)
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                stack.extend(graph[current])
        if len(visited) > initLength:
            count += 1
    return count

def number_of_connected_graphs_dfs_recursive(graph):  
    visited = set()
    count = 0
    for x in graph.keys():
        if explore(graph, x, visited):
            count += 1
    return count   

def explore(graph, current, visited):
    if current in visited:
        return False

    visited.add(current)
    for x in graph[current]:
        explore(graph, x, visited)
    return True

def largest_component_dfs_iter(graph):  
    visited = set()
    largest = 0
    for x in graph.keys():
        stack = list(x)
        initLength = len(visited)
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                stack.extend(graph[current])
        if len(visited) > initLength:
            largest = max(largest, len(visited) - initLength)
    return largest

def largest_component_dfs_recursive(graph):  
    visited = set()
    largest = 0
    for x in graph.keys():
        largest = max(largest, explore_size(graph, x, visited))
    return largest

def explore_size(graph, current, visited):
    if current in visited:
        return 0

    visited.add(current)
    size = 1
    for x in graph[current]:
        size += explore_size(graph, x, visited)
    return size

def shortest_path_bfs_iter(graph, src, des):  
    visited = set()
    stack = deque(list([[src,0]]))
    while stack:
        current, weight = stack.popleft()
        if current == des:
            return weight
        if current not in visited:
            visited.add(current)
            stack.extend([x, weight + 1] for x in graph[current])
    return "No path"

def number_of_islands(grid):
    visited = set()
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1 and (x,y) not in visited:
                print(x,y)
                stack = [(x,y)]
                initLength = len(visited)
                while stack:
                    print(stack)
                    print(visited)
                    current = stack.pop()
                    if current not in visited:
                        i,j = current
                        visited.add(current)
                        if i - 1 >= 0:
                            if grid[i-1][j] == 1:
                                stack.append((i-1,j))
                        if j - 1 >= 0:
                            if grid[i][j-1] == 1:
                                stack.append((i,j-1))
                        if i + 1 < len(grid[x]):
                            if grid[i+1][j] == 1:
                                stack.append((i+1,j))
                        if j + 1 < len(grid):
                            if grid[i][j+1] == 1:
                                stack.append((i,j+1))
                    
                if len(visited) > initLength:
                    count += 1
                    print(count)
    return count

def number_of_islands_recursive(grid):
    # Time complexity: O(M*N)
    # Space complexity: O(M*N)
    if grid == None or len(grid) == 0:
        return 0
    m = len(grid)
    n = len(grid[0])
    totalIslands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                totalIslands += computePaths(grid, i, j, m, n)
    return totalIslands

def computePaths(grid, i, j, m, n):
    if (i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0):
        return 0
    grid[i][j] = 0
    left = computePaths(grid, i, j-1, m, n)
    right = computePaths(grid, i, j+1, m, n)
    up = computePaths(grid, i+1, j, m, n)
    down = computePaths(grid, i-1, j, m, n)
    return 1

def number_of_distinct_islands(grid):
    # X = starting position
    # O = out of bounds or water
    # L = left
    # R = right
    # U = up
    # D = down
    # Time complexity: O(M*N)
    # Space complexity: O(M*N)
    if grid == None or len(grid) == 0:
        return 0
    visited = set()
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                path = computeDistinctPaths(grid, i, j, m, n, "X")
                visited.add(path)
    return len(visited)

def computeDistinctPaths(grid, i,j,m,n,direction:str):
    if (i<0 or j<0 or i>=m or j>=n or grid[i][j] == 0):
        return "O"
    grid[i][j] = 0
    left: str = computeDistinctPaths(grid, i, j-1, m, n, "L")
    right: str = computeDistinctPaths(grid, i, j+1, m, n, "R")
    up: str = computeDistinctPaths(grid, i+1, j, m, n, "U")
    down: str = computeDistinctPaths(grid, i-1, j, m, n, "D")
    return direction + left + right + up + down

def max_area_of_islands(grid):
    # Time complexity: O(M*N)
    # Space complexity: O(M*N)
    if grid == None or len(grid) == 0:
        return 0
    m = len(grid)
    n = len(grid[0])
    maxArea = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                maxArea = max(maxArea, computeAreaPaths(grid, i, j, m, n))
    return maxArea

def computeAreaPaths(grid, i, j, m, n, total = 0):
    if (i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0):
        return 0
    grid[i][j] = 0
    left = computeAreaPaths(grid, i, j-1, m, n, total)
    right = computeAreaPaths(grid, i, j+1, m, n, total)
    up = computeAreaPaths(grid, i+1, j, m, n, total)
    down = computeAreaPaths(grid, i-1, j, m, n, total)
    return total + left + right + up + down + 1

def remove_islands_on_borders(grid):
    # Time complexity: O(M*N)
    # Space complexity: O(M*N)
    if grid == None or len(grid) == 0:
        return 0
    m = len(grid)
    n = len(grid[0])
    newGrid = None
    for i in range(m):
        for j in range(n):
            if (i ==0 or j == 0 or i == m-1 or j == n-1) and grid[i][j] == 1:
                newGrid = computeRemovePaths(grid, i, j, m, n)
    return newGrid

def computeRemovePaths(grid, i, j, m, n):
    if (i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0):
        return 0
    grid[i][j] = 0
    computeRemovePaths(grid, i, j-1, m, n)
    computeRemovePaths(grid, i, j+1, m, n)
    computeRemovePaths(grid, i+1, j, m, n)
    computeRemovePaths(grid, i-1, j, m, n)
    return grid

def number_of_closed_islands(grid):
    # Time complexity: O(M*N)
    # Space complexity: O(M*N)
    if grid == None or len(grid) == 0:
        return 0
    m = len(grid)
    n = len(grid[0])
    totalIslands = 0
    for i in range(1,m):
        for j in range(1,n):
            if grid[i][j] == 0:
                if computeClosedPaths(grid, i, j, m, n):
                    totalIslands += 1
    return totalIslands

def computeClosedPaths(grid, i, j, m, n):
    if grid[i][j] == -1 or grid[i][j]:
        return True
    if i == 0 or j == 0 or i == m-1 or j == n-1:
        return False
    grid[i][j] = -1
    left = computeClosedPaths(grid, i, j-1, m, n)
    right = computeClosedPaths(grid, i, j+1, m, n)
    up = computeClosedPaths(grid, i+1, j, m, n)
    down = computeClosedPaths(grid, i-1, j, m, n)
    return left and right and up and down

graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
} 

edges = [['a', 'b'], ['b', 'c'], ['d', 'e'], ['f', 'g'],['g', 'h'], ['h','i'], ['i', 'j']]

grid = [
    [1,1,0,1,1],
    [1,1,0,1,1],
    [0,0,1,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]
]

grid1 = [
    [1,0,0,0,0,0],
    [0,1,0,1,1,1],
    [0,0,1,0,1,0],
    [1,1,0,0,1,0],
    [1,0,1,1,0,0],
    [1,0,0,0,0,1]
]

grid2 = [
    [1,0,0,0,0,0],
    [0,1,0,1,1,1],
    [1,0,1,0,1,0],
    [1,1,0,0,1,0],
    [1,0,1,1,0,0],
    [1,1,0,0,0,1]
]

# bfs_iter(graph, 'a')

# print(cyclic_graph_search_bfs_iter(build_graph(edges), 'a', 'f', set()))

# print(number_of_connected_graphs_dfs_recursive(build_graph(edges)))

# print(largest_component_dfs_iter(build_graph(edges)))

# print(largest_component_dfs_recursive(build_graph(edges)))

# print(shortest_path_bfs_iter(build_graph(edges), 'f', 'j'))

# print(number_of_islands_recursive(grid))

# print(number_of_distinct_islands(grid))

# print(max_area_of_islands(grid))

# print(remove_islands_on_borders(grid1))

print(number_of_closed_islands(grid2))

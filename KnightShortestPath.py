
import collections
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

DIRECTIONS = [
    (-2, -1), (-2, 1), (-1, 2), (1, 2),
    (2, 1), (2, -1), (1, -2), (-1, -2),
]

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        queue = collections.deque([(source.x, source.y)])
        distance = {(source.x, source.y) : 0 }
      
        
        #BFS
        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)]
            
            for delta_x, delta_y in DIRECTIONS:
                next_x, next_y = delta_x + x, delta_y + y 
            
                if (next_x, next_y) in distance:
                    continue
                if not self.is_valid(next_x, next_y, grid):
                    continue 
                distance[(next_x, next_y)] = distance[(x, y)] + 1 
            
                queue.append((next_x, next_y))
        
        return -1 
    
    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        
        if not (0 <= x < n and 0 <= y < m):
            return False
        
        return not grid[x][y]
    
if __name__ =='__main__':
    grid = [[0,0,0],
            [0,0,0],
            [0,0,0]]
            
    source = Point(2, 0)
    destination = Point(2, 2)
    solution = Solution()
    x = solution.shortestPath(grid, source, destination)
    print(x)

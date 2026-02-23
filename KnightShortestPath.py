
from collections import deque
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
        #x is row position, y is column position
        #put the start source point into queue
        queue = deque([(source.x, source.y)])
        #we use a dictionary to figure out the distance
        #initize source to source, the distance is 0
        #key is matrix's position, value is the distance to the source point
        distance = {(source.x, source.y): 0}
        
        
        #BFS starts here, while queue is not None
        while queue:
            #pop out from the queue
            x, y = queue.popleft()
            # if this point equals to the destination's position, return distance
            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)]
            #if (x, y) != (destination.x, destination.y), we move one step further
            #according to the chess rule
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                #sometimes, the point can move back the old point, so, we just skip
                #eg. (x, y)= (0, 1) can move to (2, 0), but (2, 0) alreay in
                #distance, so, we continue when we ran into old point 
                if (next_x, next_y) in distance:
                    continue
                #if it is a new move, we need to check whether it is a valid point 
                # or not 
                #if it is not valid, we skip the rest code 
                if not self.is_valid(next_x, next_y, grid):
                    continue
                #if it is a valid new move, we calculate the new distance based on 
                #(x, y) point, and we put this point in queue
                #这是hashmap 的一种写法distance[], []中写key , 等于的是这个key对应
                #的value, 那么这个新点（next_x, next_y) 就是上一个点（x, y)距离+ 1
                distance[(next_x, next_y)] = distance[(x, y)] + 1
                queue.append((next_x, next_y))
        return -1
        
    def is_valid(self, x, y, grid):
        # n is matrix row number, m is matrix column number
        n, m = len(grid), len(grid[0])

        # if x, y outside the boundary condition, return False 
        if not (0 <= x < n and 0 <= y < m):
            return False
        # reach this step, it means the new move is valid 
        # 这里要写not grid[x][y], 走到这一步，说明这个点是valid, 那么这个点会返回
        # 到44 行， 44 行的判断，如果不符合，就skip, 但是如果返回的是not grid[x][y]
        # 那么双否定表肯定，表明这个点是valid, 不skip the rest code, we acculate 
        # distance + 1 and put it in queue
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

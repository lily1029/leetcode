from collections import deque
DIRECTIONS = [(0, -1), (0, 1), (1, 0), (-1, 0)]
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0 
        #visited is a global variable, it can make sure the same point that we 
        #don't BFS twice
        visited = set()
        islands = 0
        #go through the whole matrix, i means rows, j means columns
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #if grid[i][j] = 1 and not in visited, we do BFS for this point
                if grid[i][j] == 1 and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1 
        return islands

    
    def bfs(self, grid, x, y, visited):
        # we put this point(x,y) in a queue
        queue = deque([(x, y)])
        # we mark this point as visited by adding it in visited set
        visited.add((x, y))

        #while go through the queue
        while queue:
            #pop up this point
            x, y = queue.pop()
            # check 4 neighbours next to this point
            for delta_x, delta_y in DIRECTIONS:
                new_x, new_y = x + delta_x, y + delta_y

                #for each neighbor , we check it is valid or not
                #if the neighbor is not valid, we continue all the rest code
                if not self.is_valid(grid, new_x, new_y, visited):
                    continue 
                
                # if the neighbor is valid , we put it in queue and set it as visited
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
    
    #we define a method to check it is valid or not
    def is_valid(self, grid, x, y, visited):
        # matrix n means matrix rows, m means matrix column
        n, m = len(grid), len(grid[0])
        # we check whether x, y is outside the boundary of m, n
        #if outside the boundary, we return False
        if not (0 <= x < n and 0 <= y < m):
            return False 
        # if (x, y) is already visited, we return False
        if (x, y) in visited:
            return False 
        #这里如果grid[x][y] == 1就返回true, 如果grid[x][y]== 0就返回false
        return grid[x][y] == 1
if __name__ =='__main__':
    island = Solution()
    grid = [
            [1,1,0,0,0],
            [0,1,0,0,1],
            [0,0,0,1,1],
            [0,0,0,0,0],
            [0,0,0,0,1]
            ]
    x = island.numIslands(grid)
    y = print(x)

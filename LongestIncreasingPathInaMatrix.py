from typing import (
    List,
)

DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
class Solution:
    """
    @param matrix: an integer matrix
    @return: the length of the longest increasing path
    """
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        #base case
        if not matrix or not matrix[0]:
            return 0
        #here we store result
        sequence = []
        #go through the whole matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                #we use tupple to store each position
                sequence.append((matrix[i][j], i, j))
        #we sort the sequence by the first number
        sequence.sort()
        
        #here we use hashmap to count how long the path for each position
        check = {}
        #go through each sequence
        for h, x, y in sequence:
            #get the current position
            cur_pos = (x, y)
            #check the cur_pos is not in check, we put it, one position count 1 distance
            if cur_pos not in check:
                check[cur_pos] = 1
            cur_path = 0
            #here we go through 4 directions
            for dx, dy in DIRECTIONS:
                #here we check whether the new position is valid or not, it is increasing than before
                if self.is_valid(x+dx, y+dy, matrix, h): #if it is valid
                    cur_path = max(cur_path, check[(x+dx, y+dy)]) #we update the cur_path to the max of two paths
            check[cur_pos] += cur_path 
        
        vals = check.values()
        return max(vals)
    
    def is_valid(self, x, y, matrix, h):
        #here we check the boundary conditions
        row, col = len(matrix), len(matrix[0])
        #here check the boundary and increasing point
        return x >= 0 and x < row and y >= 0 and y < col and matrix[x][y] < h
if __name__ == '__main__':
    ll = Solution()
    matrix = [[1,2],[4,3]]
    x = ll.longestIncreasingPath(matrix)
    print(x)


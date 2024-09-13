class Solution:
    def funcMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return []
        
        n = len(matrix)
        m = len(matrix[0])

        maxRows = []
        for i in range(n):
            maxElement = matrix[i][0]
            maxIndex = 0
            for j in range(1, m):
                if matrix[i][j] > maxElement:
                    maxElement = matrix[i][j]
                    maxIndex = j
            maxRows.append((i, maxIndex, maxElement))


        maxVal = 0
        # for i, j, value in maxRows:
        #     SmallestColumn = all(matrix[k][j] >= value for k in range(n))
        #     if SmallestColumn:
        #         maxVal = value
        # return maxVal

         # Check if each row maximum is also the smallest in its column
        for i, j, value in maxRows:
            # Create a generator expression to check if the value is the smallest in the column
            is_smallest_in_column = True
            for k in range(n):
                if matrix[k][j] < value:
                    is_smallest_in_column = False
                    break

            # If the value is the smallest in its column, update maxVal
            if is_smallest_in_column:
                maxVal = value
        
        return maxVal
if __name__ == '__main__':
    ll = Solution() 
    cc = [
            [2, 2],
            [1, 2],
            [3, 4]
            ]
    x = ll.funcMatrix(cc)
    print(x)

        
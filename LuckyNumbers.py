class Solution:

    def lucky_numbers(self, matrix):
        min_in_rows = {min(row) for row in matrix}
        max_in_columns = {max(col) for col in zip(*matrix)}
        
        return list(min_in_rows & max_in_columns)


if __name__ =='__main__':
    ll = Solution()
    matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    x = ll.lucky_numbers(matrix)
    print(x)
    
# Method to solve this problem is as below:

# Finding Minimum in Rows: We use a set comprehension to find the minimum element in each row.
# Finding Maximum in Columns: We use zip(*matrix) to transpose the matrix and then find the maximum element in each column.
# Finding Intersection: The intersection of these two sets gives the lucky numbers.

# The zip(*matrix) expression is a way to transpose a matrix in Python. Transposing a matrix means converting its rows to columns and its columns to rows.


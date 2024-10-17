class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        # Write your code here
        for i in range(len(source) - len(target) + 1):
            if source[i : i + len(target)] == target:
                return i 
        return -1  
if __name__ =='__main__':
        solution = Solution()
        source = "abcdabcdefg"
        target = "bcd"

        x = solution.str_str(source, target)
        print(x)


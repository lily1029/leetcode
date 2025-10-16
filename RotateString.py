class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        return len(s) == len(goal) and goal in s + s
        
if __name__ =='__main__':
        solution = Solution()
        s = "abcde"
        goal = "cdeab"
        x = solution.rotateString(s, goal)
        print(x)
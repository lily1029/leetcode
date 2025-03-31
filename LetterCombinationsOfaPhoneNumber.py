#使用深度优先搜索算法。
KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # if no digits, we return []
        if not digits:
            return []
        
        # we use results to store final results    
        results = []

        # we call dfs method 
        self.dfs(digits, 0, [], results)
        
        return results
    
    #index is for digits' index, we use chars to 
    #temporary to store each result 
    def dfs(self, digits, index, chars, results):

        if index == len(digits):
            results.append(''.join(chars))
            return
        
        #digits[0]= 2 , KEYBOARD[2] = abc , so 
        # letter is a 
        for letter in KEYBOARD[digits[index]]:

            # we put a in chars 
            chars.append(letter)

            #对下一个index (e.g 1),进行DFS,也就是3里面的
            #字母一个一个排列
            self.dfs(digits, index + 1, chars, results)
            #backtracking
            chars.pop()

if __name__ == '__main__':
    ll = Solution()
    digits = "23"
    x = ll.letterCombinations(digits)
    print(x)



class Solution:
    def funcSubstring(self, inputStr):
        def expand_around_center(left, right):
            while left >= 0 and right < len(inputStr) and inputStr[left] == inputStr[right]:
                left -= 1
                right += 1
            return inputStr[left + 1 : right]
        
        if not inputStr or len(inputStr) == 1:
            return "None"
        
        longest = ""

        for i in range(len(inputStr)):
            odd_palindrome = expand_around_center(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome

            even_palindrome = expand_around_center(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
            
        # You might want to return an empty string or the longest palindrome, not "None"
        if len(longest) == 1:
            return "None"
        
        return longest
    
if __name__ == '__main__':
    ll = Solution()  # Fixed typo here
    x = "YABCCBAZ"
    print(ll.funcSubstring(x))  # Call the method and print the result

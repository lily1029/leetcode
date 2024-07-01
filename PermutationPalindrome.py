class Solution:
    def perm_palindrome(self, s):
        from collections import Counter
        
        # Count the frequency of each character in the string
        char_count = Counter(s)
        
        # Count how many characters have an odd frequency
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        # For a string to have a permutation that is a palindrome:
        # If the length is even, no characters should have an odd frequency (odd_count should be 0)
        # If the length is odd, only one character should have an odd frequency (odd_count should be 1)
        return odd_count <= 1

# Example usage:
# print(perm_palindrome("civic"))  # Output: True (as "civic" is already a palindrome)
# print(perm_palindrome("ivicc"))  # Output: True (as "civic" or "icvci" are palindromes)
# print(perm_palindrome("hello"))  # Output: False (no permutation forms a palindrome)
# print(perm_palindrome("aabbccdd"))  # Output: True (as "abcdcdba" is a palindrome)
if __name__ == '__main__':
    ll = Solution()
    s = "ivicc"
    x = ll.perm_palindrome(s)
    print(x)
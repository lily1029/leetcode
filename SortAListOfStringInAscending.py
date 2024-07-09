class Solution:
    def bubble_sort(self, strings):

        n = len(strings)
        
        for i in range(n):
            for j in range(0, n-i-1):
                if strings[j] > strings[j+1]:
                    strings[j], strings[j+1] = strings[j+1], strings[j]
        
        return strings

if __name__ == '__main__':
    ll = Solution()

    # Example usage:
    strings = ["banana", "apple", "cherry", "date"]
    x = ll.bubble_sort(strings)
    print(x)

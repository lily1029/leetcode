class Solution:
    def is_prime(self, num):
        """ Helper function to check if a number is prime. """
        if num <= 1:
            return False
        if num == 2:
            return True  # 2 is a prime number
        if num % 2 == 0:
            return False  # Even numbers greater than 2 are not prime
        
        # Check for factors from 3 up to the square root of num
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        
        return True

    def find_prime_numbers(self, nums):
        """ Function to find and return all prime numbers in an array. """
        prime_numbers = []
        for num in nums:
            if self.is_prime(num):
                prime_numbers.append(num)
        
        return prime_numbers
if __name__ == '__main__':
    ll = Solution()
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = ll.find_prime_numbers(arr1)
    print(x)

# Example usage:
# arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arr2 = [4, 6, 8, 9, 10]
# arr3 = [2, 3, 5, 7, 11]

# print(find_prime_numbers(arr1))  # Output: [2, 3, 5, 7]
# print(find_prime_numbers(arr2))  # Output: []
# print(find_prime_numbers(arr3))  # Output: [2, 3, 5, 7, 11]

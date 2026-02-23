class Solution:
    
    def fizz_buzz(self, i):
        result = []
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        return result

    
if __name__ == '__main__':
    ll = Solution()

    i = 30
    x =  ll.fizz_buzz(i)

    print(x)




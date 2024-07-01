class Solution:
   
    def reverseInteger(self, n):
        #here is the reversed num
        num = 0
        #make sure every number is positive num
        a = abs(n)
        
        #go through each num
        while a != 0:
            #here we can get the last digit
            temp = a % 10
            #make the last digit as the first digit
            num = num * 10 + temp
            #get the front number except the last digit
            a = int(a / 10)
     
        
        if n > 0 and num < 2147483647:
            return num
        elif n < 0 and num <= 2147483647:
            return -num
        else:
            return 0
if __name__ == '__main__':
    ll = Solution()
    n = 123
    x = ll.reverseInteger(n)
    print(x)
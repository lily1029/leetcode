class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        #corner case 
        if num <= 0:
            return False
        #题目 给出 1 是 ugly number
        if num == 1:
            return True  
        #乘法因子为2， 3， 5，   
        while num >= 2 and num % 2 == 0:
            num /= 2;  
        while num >= 3 and num % 3 == 0:
            num /= 3;  
        while num >= 5 and num % 5 == 0:
            num /= 5;  

        #如果是ugly numner 最后都整除后变成1 
        return num == 1
if __name__ == '__main__':
    ll = Solution()
    #num = 9 
    num  = 14
    x = ll.isUgly(num)
    print(x)



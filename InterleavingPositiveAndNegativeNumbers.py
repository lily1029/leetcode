class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
       
        #这里的k是为了交换而设置的，k把负数换到左边,当交换完一个后，k+1
        k = 0

        #这个for循环将数组分成了负负负正正正
        for i in range(len(A)):
            if A[i] < 0:
                A[i], A[k] = A[k], A[i]
                k += 1

        #负数的个数        
        neg_count = k 
        #这里是postive数的个数
        pos_count = len(A) - k 
        
        #这里设置一个flag. 如果正数大于负数 isPos为正
        #这里考虑到了flag的用法，如果负数多，设置起初flag为False开始
        #如果正数多，设置起初的flag为True开始
        isPos = pos_count > neg_count 
        
        #此for循环使正负交替出现， 用flag控制正负交替出现，条件在下方
        for i in range(len(A)):
            #当flag是false，这个数是负数，，不用交换， 
            #当flag是true,  这个数又是负数时，需要交换
            #当flag为true,  这个数大于0，不用交换
            #当flag为false, 这个数大于0，需要交换
            if (isPos and A[i] < 0) or (not isPos and A[i] > 0): 
                #和第一个k的值为正数的值交换，然后k+1                  
                A[i], A[k] = A[k], A[i]  
                k += 1
            
            #这里翻转flag
            isPos = not isPos
            
        return A
if __name__ == '__main__':
    ll = Solution()
    # A = [-1, -2, -3, 4, 5, 6, 7]
    # A = [5, -1, -2, 3]
    A = [-1, -2, 3, 4, 5, 6, 7]
    x = ll.rerange(A)
    print(x)
class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
       
        #这里的k是为了交换而设置的，k把负数换到左边,正数到右边
        #当交换完一个后，k+1
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
        #这里正负数相差不到1，如果是正数多e.g: [-1, -2, 4, 5, 6] 
        #程序执行后变成：[4, -2, 5, -1, 6],这时候我们需要把最初的
        #isPos设置为正， 因为[正， 负，正， 负， 正]，正出现3次，
        #这样才能让它们交替出现，此时条件isPos and A[i] < 0，
        #isPos 为正，A[i] < 0，进行交换

        #这里考虑到了flag的用法，如果负数多，设置起初flag为False开始
        #e.g [-1, -2, -3, 4, 5]程序执行后变成[-1,4,-3,5,-2]
        #因为[负，正，负，正，负]，所以在负数多时开始要先负，
        #所以isPos and A[i] < 0， isPos为负数，A[i] < 0 不交换
        #如果正数多，设置起初的flag为True开始
        isPos = pos_count > neg_count 
        
        #此for循环使正负交替出现， 用flag控制正负交替出现，条件在下方
        for i in range(len(A)):
            #负数多，最初flag是false，这个数是负数，不用交换， 
            #正数多，当flag是true,  这个数又是负数时，需要交换
            if (isPos and A[i] < 0): 
                #和第一个k的值为正数的值交换，然后k+1， k向前走一步                 
                A[i], A[k] = A[k], A[i]  
                k += 1
            
            #这里翻转flag
            isPos = not isPos
            
        return A
if __name__ == '__main__':
    ll = Solution()
    # A = [-1, -2, -3, 4, 5, 6]
    # A = [5, -1, -2, 3]
    A = [-1, -2, 3, 4, 5, 6, 7]
    x = ll.rerange(A)
    print(x)
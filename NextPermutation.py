# 解法：
# 1. 现在list里找到最大的降序排列 e.g [1, 2, 5, 4, 3], 这里的降序是 5， 4， 3， 
# 这里的2 是reverse point 
# 2. 从序列最后一个元素开始和reverse point 比较，找到第一个比reverse point 大的交换 
#【1， 3， 5， 4， 2】
# 3. 对剩下的 5， 4，2， 进行逆序排序 【1， 3， 2， 4， 5】
class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
       
        #look for a reverse point 
        for i in range(len(num)-2, -1, -1):
            if num[i] < num[i+1]:
                break
        else:
            num.reverse()
            return num
            
        #从末尾找到比reverse point 大的最近的数，进行交换
        for j in range(len(num)-1, i, -1):
            if num[j] > num[i]:
                num[i], num[j] = num[j], num[i]
                break

        #reverse 剩下的elements to ascending order变成最近的下一个next permutation
        # num[i+j+1]是reverse point 的下一个数字
        # num[len(num)-j-1] 是剩下reverse 数组里的最后一个最右边要交换的数字，
        #它俩进行交换，因为它们在剩下的数组
        #本身是降序的 e.g: [5, 4, 2], 要换成【2， 4， 5】，才是它的下一个最接近的permutation
        #(len(num) - i)//2 这个是算剩下的数组还要 进行几次交换 
        #可以理解成，len(nums)长度 - i 位置的长度，然后每次换两个数，所以 // 2   
        for j in range(0, (len(num) - i)//2):
            num[i+j+1], num[len(num)-j-1] = num[len(num)-j-1], num[i+j+1]
        return num

if __name__ == '__main__':
    ll = Solution()
    # num = [1,3,2,3]
    num = [1, 2, 5, 4, 3]
    x = print(ll.nextPermutation(num))
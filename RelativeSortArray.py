from collections import Counter

class Solution:
    #这道题用的是counting sort method, 先count 出
    #arr1里每个数字出现几次
    def relativeSortArray(self, arr1, arr2):
        #e.g: Counter = {2:3, 3:2, 1:1, 4:1, 6:1,....}
        #arr1里3 个2， 2 个 3 
        counts = Counter(arr1)

        #这里是最后的结果
        res = []

        #这里go through每一个数在arr2里，并且extend res list
        #每一个数乘以它在arr1里出现几次，放到res里
        #e.g 2 在 arr1里出现3次，所以: res = [2, 2, 2,....]，arr2
        #的下一个数是 1， 就 1 * 1， 1 在arr2里出现了一次，依此类推
        #然后我们及时把这个放入的数在Counter里删了
        for num in arr2:
            # e.g num = 2 , 2 * 3 = [2, 2, 2]
            res.extend([num] * counts[num])
            del counts[num]
        
        #sort 剩下的只在arr1里出现，每在arr2里出现的，并且放入res里
        for num in sorted(counts.keys()):
            res.extend([num] * counts[num])
        
        return res
        

if __name__ == '__main__':
    ll = Solution()
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    x = ll.relativeSortArray(arr1, arr2)
    print(x)